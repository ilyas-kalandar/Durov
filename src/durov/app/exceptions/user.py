from durov.app.exceptions.base import AppException


class UserNotFound(AppException):
    """If user not found."""
