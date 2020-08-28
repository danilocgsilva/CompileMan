class Compile_Result:

    def __init__(self):
        self.success = None
        self.message = None

    def setSuccess(self):
        self.success = True

    def setError(self, message: str):
        self.success = False
        self.message = message

    def getResult(self) -> bool:
        return self.success

    def getErrorMessage(self) -> str:
        return self.message
