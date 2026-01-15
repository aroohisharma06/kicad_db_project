import os

def to_virtual_path(abs_path, base_dir):
    """
    Convert absolute path → virtual path (relative to base_dir)
    """
    return os.path.relpath(abs_path , base_dir).replace(os.sep, "/")
