class NotFoundException(Exception):
    error_code = 404

    def __init__(self, message):
        super().__init__(message)
        self.details = message
