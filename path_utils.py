import os

def normalize_path(path):
    return path.replace('\\', '/')

def get_depth(file_path, root_directory):
    relative_path = os.path.relpath(file_path, root_directory)
    return relative_path.count(os.sep)

def is_excluded(file_path, exclude_dirs, exclude_files):
    for dir in exclude_dirs:
        if dir in file_path:
            return True
    return os.path.basename(file_path) in exclude_files
