class AlgorithmException(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message

class InputAlgorithmException(AlgorithmException):
    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message

class ImpossibilityAlgorithmException(AlgorithmException):
    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message
