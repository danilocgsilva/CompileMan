class Compile_Result:

    def __init__(self):
        self.success = None
        self.message = None

    def setSuccess(self):
        self.success = True
        return self

    def setError(self, message: str):
        self.success = False
        self.message = message
        return self

    def getResult(self) -> bool:
        return self.success

    def getErrorMessage(self) -> str:
        return self.message
