import os
import shutil

def purge_and_copy(start_path:str, dest_path:str) -> None:
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    else:
        os.makedirs(dest_path)
    if not os.path.exists(start_path):
        raise FileNotFoundError(f"")
    shutil.copytree(start_path, dest_path, dirs_exist_ok=True)