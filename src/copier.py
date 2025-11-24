import os
import shutil

def purge_and_copy_from_static_to_public() -> None:
    public_dir = "public"
    static_dir = "static"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    else:
        os.makedirs(public_dir)
    if not os.path.exists(static_dir):
        raise FileNotFoundError(f"")
    shutil.copytree(static_dir, public_dir, dirs_exist_ok=True)