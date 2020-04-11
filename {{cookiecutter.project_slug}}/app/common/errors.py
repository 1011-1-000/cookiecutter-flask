from jwt import ExpiredSignatureError as _ExpiredSignatureError
from jwt import InvalidTokenError as _InvalidTokenError


class Error(Exception):
    pass


class UserAlreadyExistError(Error):

    def __init__(self):
        self.message = 'User already exists'

class UserDoesNotExistError(Error):

    def __init__(self):
        self.message = "User doesn't exist"

class TokenBlackListedError(Error):

    def __init__(self):
        self.message = 'This token has been added to black list, please login again!'

class NotMatchOrUserDoesNotExistsError(Error):

    def __init__(self):
        self.message = "User name and password does't match, or user doesn't exists"

class TokenMissedError(Error):

    def __init__(self):
        self.message = "Token is not exist, please login!"

class ParameterMissingError(Error):

    def __init__(self):
        self.message = "The parameters has not been setted correctly!"

class PermissionDeniedDataAccessException(Error):

    def __init__(self):
        self.message = "Data access failed due to insufficient permissions"

class DataRetrievalFailureException(Error):

    def __init__(self):
        self.message = "Data could not be retrieved"
        

ExpiredSignatureError = _ExpiredSignatureError
InvalidTokenError = _InvalidTokenError
