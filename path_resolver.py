import os
from typing import List, Optional

class PathResolver:
    """A simple, generic path resolution utility with no project assumptions."""
    
    def __init__(self, base_dirs: Optional[List[str]] = None):
        """
        Initialize PathResolver with optional base directories.
        
        Args:
            base_dirs: List of base directories to search in. 
                      Defaults to [current_working_dir]
        """
        self.base_dirs = base_dirs or [os.getcwd()]
    
    def resolve(self, path: str, search_dirs: Optional[List[str]] = None) -> str:
        """
        Resolve a path with fallback priorities.
        
        Args:
            path: The path to resolve (can be relative or absolute)
            search_dirs: Optional list of directories to search in. 
                        Defaults to instance base_dirs
        
        Returns:
            Resolved absolute path (first existing path or default fallback)
        """
        if os.path.isabs(path):
            return path
        
        search_dirs = search_dirs or self.base_dirs
        candidates = [os.path.join(search_dir, path) for search_dir in search_dirs]
        
        # Return first existing path, or default to first candidate
        return next((candidate for candidate in candidates if os.path.exists(candidate)), candidates[0])
    
    def ensure_directory(self, file_path: str) -> None:
        """Ensure the directory for a file path exists."""
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
    
    def add_base_dir(self, directory: str) -> None:
        """Add a base directory to search in."""
        if directory not in self.base_dirs:
            self.base_dirs.append(directory)
    
    def get_base_dirs(self) -> List[str]:
        """Get the current base directories."""
        return self.base_dirs.copy()