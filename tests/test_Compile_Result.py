import unittest
import sys
sys.path.insert(1, "..")
from compileman.Compile_Result import Compile_Result


class test_Compile_Result(unittest.TestCase):

    def setUp(self):
        self.compile_result = Compile_Result()

    def test_setSuccess_status(self):
        self.compile_result.setSuccess()
        result = self.compile_result.getResult()
        self.assertTrue(result)

    def test_setSuccess_message(self):
        self.compile_result.setSuccess()
        message = self.compile_result.getErrorMessage()
        self.assertEqual(None, message)

    def test_setError(self):
        self.compile_result.setError("Folder not exists when trying to remove.")
        result = self.compile_result.getResult()
        self.assertFalse(result)

    def test_setError_message(self):
        error_message = "Folder not exists when trying to remove."
        self.compile_result.setError(error_message)
        message_returned = self.compile_result.getErrorMessage()
        self.assertEqual(error_message, message_returned)
