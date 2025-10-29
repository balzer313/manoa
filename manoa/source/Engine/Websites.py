from os import *
from os.path import isfile, join


class Websites:  # יוצר websites מהsample texts
    def __init__(self, files_path):
        self.websites = self.make_websites(files_path)

    def get_websites(self):
        return self.websites

    def make_websites(self, files):
        return [f for f in listdir(files) if isfile(join(files, f)) and f.lower().endswith(".txt")]
