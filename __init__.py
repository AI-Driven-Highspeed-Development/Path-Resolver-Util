"""
ADHD Path Resolver Package

A centralized path resolution utility for ADHD project template.
Handles path resolution, directory creation, and file operations across different environments.

Usage:
    from utils.path_resolver import PathResolver
    
    ## Basic usage
    pr = PathResolver()
    resolved_path = pr.resolve('config.json')
    
    ## Ensure directory exists
    pr.ensure_directory('/path/to/directory')
    
    ## Get various path types
    abs_path = pr.get_absolute_path('relative/path')
    project_path = pr.get_project_relative_path('some/file')
"""