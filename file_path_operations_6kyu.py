class FileMaster():
    def __init__(self, filepath):
        self.path = filepath
        self.dot = self.path.rfind('.')
    def extension(self):
        return self.path[self.dot + 1:len(self.path)]
    def filename(self):
        return self.path[self.path.rfind('/') + 1:self.dot]
    def dirpath(self):
        return self.path[:self.path.rfind('/') + 1]
