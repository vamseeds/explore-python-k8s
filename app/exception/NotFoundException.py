class NotFoundException(Exception):

    def __init__(self, message, error_code):
        super().__init__(message)
        self.details = message
        self.error_code = error_code
