

def read_file(path: str, setting: str):
    with open(path, setting) as opened_file:
        return opened_file.read()