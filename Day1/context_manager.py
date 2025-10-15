class LogManager:
    """
    Context manager to handle file opening and closing.
    Ensures logs are safely written and file is closed automatically.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
