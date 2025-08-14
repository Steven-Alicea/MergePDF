import os
import sys



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    print(f"BASE_PATH =  {base_path}")
    print(f"RELATIVE_PATH = {relative_path}")
    return os.path.join(base_path.strip("src\\"), relative_path)