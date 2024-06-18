from aiogram.types.error_event import ErrorEvent

class UserException(Exception):
    
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
        
    @classmethod
    def isinstance(cls, exception: ErrorEvent) -> bool:
        return isinstance(exception.exception, cls)

class TokenDoesNotDefined(UserException):

    def __init__(self, message="Token is not defined"):
        self.message = message
        super().__init__(self.message)

class InvalidEnvException(UserException):
    
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)