class AppException(Exception):
    """Base for all exceptions"""

    def __init__(self, message: str):
        self.message = message
