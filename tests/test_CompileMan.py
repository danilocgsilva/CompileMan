import unittest
import sys
import os
import tempfile
import shutil
sys.path.insert(1, "..")
from compileman.CompileMan import CompileMan

class test_CompileMan(unittest.TestCase):

    def setUp(self):
        self.compileman = CompileMan()

    def test_is_node_module_exists(self):
        self.go_to_tmp()
        self.empty_folder()
        os.makedirs('node_modules')
        self.assertTrue(self.compileman.is_node_module_exists())

    def test_is_node_module_exists_false(self):
        self.go_to_tmp()
        self.empty_folder()
        self.assertFalse(self.compileman.is_node_module_exists())

    def test_is_vendor_exists(self):
        self.go_to_tmp()
        os.makedirs('vendor')
        self.assertTrue(self.compileman.is_vendor_exists())

    def test_is_vendor_exists_false(self):
        self.go_to_tmp()
        self.empty_folder()
        self.assertFalse(self.compileman.is_vendor_exists())

    def test_guess_action_clean(self):
        self.empty_folder()
        os.makedirs('node_modules')
        os.makedirs('vendor')
        expected_result = 'clean'
        self.assertEqual(expected_result, self.compileman.guess_action())

    def test_guess_action_compile(self):
        self.empty_folder()
        expected_result = 'compile'
        self.assertEqual(expected_result, self.compileman.guess_action())

    def test_guess_action_doubt_node_modules(self):
        self.empty_folder()
        os.makedirs('node_modules')
        expected_result = ''
        self.assertEqual(expected_result, self.compileman.guess_action())

    def test_guess_action_doubt_vendor(self):
        self.empty_folder()
        os.makedirs('vendor')
        expected_result = ''
        self.assertEqual(expected_result, self.compileman.guess_action())

    def test_execute_wrong_command(self):
        with self.assertRaises(Exception):
            self.compileman.execute('non_existent')

    def test_cancompile(self):
        # Here the command will checks composer command line against composer.json and npm command line against package.json.
        # If the project is php, must have composer installed and can procceed
        # If the project is node, must have npm installed and can procceed
        # If both, must have both command line and procceed
        # Otherwise return false
        # I suggests to check the output of which command in posix and it's equivalents in Windows, so the output result can be mocked to test
        self.assertTrue(False)

    def go_to_tmp(self):
        tmp_place = tempfile.gettempdir()
        os.chdir(tmp_place)
        
    def empty_folder(self):
        if os.path.exists('node_modules'):
            shutil.rmtree('node_modules')
        if os.path.exists('vendor'):
            shutil.rmtree('vendor')
