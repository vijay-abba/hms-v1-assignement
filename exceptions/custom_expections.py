class HMSBaseException(Exception):
    def __init__(self, message="An error occured in the HMS"):
        self.message = f"\033[1;31m ❌ {message} \033[0m"
        super().__init__(self.message)


class DatabaseConnectionError(HMSBaseException):
    def __init__(self, message="Failed to connect to the database"):
        self.message = message
        super().__init__(self.message)


class DuplicateRecordError(HMSBaseException):
    def __init__(self, entity, field, value):
        self.message = f"{entity}, with {field} = {value} already exits."
        super().__init__(self.message)
