class BadRequestException(Exception):
    error_code = 400

    def __init__(self, message):
        super().__init__(message)
        self.details = message
