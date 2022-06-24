
class PANAlreadyExistsError(Exception):
    def __init__(self,message):
        self.message=message

class PANDoesNotExistsError(Exception):
    def __init__(self,message):
        self.message=message
