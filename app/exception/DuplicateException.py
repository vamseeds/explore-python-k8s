class DuplicateException(Exception):
    error_code = 409

    def __init__(self, message):
        super().__init__(message)
        self.details = message
