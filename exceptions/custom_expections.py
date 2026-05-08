class HMSBaseException(Exception):
    def __init__(self, message="An error occured in the HMS"):
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionError(HMSBaseException):
    def __init__(self, message="Failed to connect to the database"):
        self.message = message
        super().__init__(self.message)


class DubplicateRecordError(HMSBaseException):
    def __init__(self, entity, field, value):
        self.message = f"{entity}, with {field} = {value} already exits."
        super().__init__(self.message)
