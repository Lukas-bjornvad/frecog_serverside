import platform
import re

def os_parse_path(path):
    print(f"path: {path}")
    if(platform.system() == 'Windows'):
        path = re.sub(r'\\\\', '/', path)
    else:
        path = re.sub(r'\/', '\\', path)
    print(path)
    return path
