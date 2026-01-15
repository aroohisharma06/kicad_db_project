import os

def to_virtual_path(abs_path, base_dir):
    """
    Convert absolute path → virtual path (relative to base_dir)
    """
    return os.path.relpath(str(abs_path), str(base_dir))
