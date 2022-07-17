class InternalServerError(Exception):
    error_code = 500

    def __init__(self, message):
        super().__init__(message)
        self.details = message
