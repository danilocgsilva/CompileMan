import unittest
import sys
import os
import tempfile
import shutil
sys.path.insert(1, "..")
from compileman.CompileMan import CompileMan
from compileman.Compile_Result import Compile_Result

class test_CompileMan(unittest.TestCase):

    def setUp(self):
        self.go_to_tmp()

    def test_is_node_module_exists(self):
        self.empty_folder()
        os.makedirs('node_modules')
        compileman = CompileMan()
        self.assertTrue(compileman.is_node_module_exists())

    def test_is_node_module_exists_false(self):
        self.empty_folder()
        compileman = CompileMan()
        self.assertFalse(compileman.is_node_module_exists())

    def test_is_vendor_exists(self):
        self.empty_folder()
        os.makedirs('vendor')
        compileman = CompileMan()
        self.assertTrue(compileman.is_vendor_exists())

    def test_is_vendor_exists_false(self):
        self.empty_folder()
        compileman = CompileMan()
        self.assertFalse(compileman.is_vendor_exists())

    def test_guess_action_clean(self):
        self.empty_folder()
        os.makedirs('node_modules')
        os.makedirs('vendor')
        compileman = CompileMan()
        expected_result = 'clean'
        self.assertEqual(expected_result, compileman.guess_action())

    def test_guess_action_compile(self):
        self.empty_folder()
        expected_result = 'compile'
        compileman = CompileMan()
        self.assertEqual(expected_result, compileman.guess_action())

    def test_guess_action_doubt_node_modules(self):
        self.empty_folder()
        os.makedirs('node_modules')
        compileman = CompileMan()
        expected_result = ''
        self.assertEqual(expected_result, compileman.guess_action())

    def test_guess_action_doubt_vendor(self):
        self.empty_folder()
        os.makedirs('vendor')
        compileman = CompileMan()
        expected_result = ''
        self.assertEqual(expected_result, compileman.guess_action())

    def test_execute_wrong_command(self):
        with self.assertRaises(Exception):
            self.compileman.execute('non_existent')

    def test_cancompile_empty_compilations(self):
        compileman = CompileMan()
        can_compile = compileman.cancompile([])
        self.assertFalse(can_compile)

    def test_cancompile_wrong_data(self):
        compileman = CompileMan()
        with self.assertRaises(Exception):
            compileman.cancompile(['not_valid'])

    def test_check_project_types(self):
        compileman = CompileMan()
        project_types = compileman.get_project_types()
        expected_project_types = []
        self.assertListEqual(expected_project_types, project_types)

    def test_clean_wrong_type(self):
        compileman = CompileMan()
        with self.assertRaises(Exception):
            compileman.clean(['non_existent'])

    def test_clean_project_type_node(self):
        os.makedirs('node_modules')
        os.makedirs('vendor')
        compileman = CompileMan()
        compileman.clean_project_type('node')
        files_in_directory = os.listdir()
        cleaned = not 'node_modules' in files_in_directory
        self.assertTrue(cleaned)

    def test_clean_project_type_node_vendor_kept(self):
        self.empty_folder()
        os.makedirs('node_modules')
        os.makedirs('vendor')
        compileman = CompileMan()
        compileman.clean_project_type('node')
        files_in_directory = os.listdir()
        kept = 'vendor' in files_in_directory
        self.assertTrue(kept)

    def test_clean_project_type_php(self):
        self.empty_folder()
        os.makedirs('node_modules')
        os.makedirs('vendor')
        compileman = CompileMan()
        compileman.clean_project_type('php')
        files_in_directory = os.listdir()
        cleaned = not 'vendor' in files_in_directory
        self.assertTrue(cleaned)

    def test_clean_project_type_php_node_kept(self):
        self.empty_folder()
        os.makedirs('node_modules')
        os.makedirs('vendor')
        compileman = CompileMan()
        compileman.clean_project_type('php')
        files_in_directory = os.listdir()
        kept = 'node_modules' in files_in_directory
        self.assertTrue(kept)

    def test_clean_project_type_return(self):
        compileman = CompileMan()
        clean_compile_result = compileman.clean_project_type('php')
        self.assertTrue(isinstance(clean_compile_result, Compile_Result))

    def test_is_posix_false(self):
        compileman = CompileMan()
        is_posix_result = compileman.is_posix('win32') 
        self.assertFalse(is_posix_result)

    def test_is_posix_true(self):
        compileman = CompileMan()
        is_posix_result = compileman.is_posix('linux') 
        self.assertTrue(is_posix_result)

    def test_is_posix_true_2(self):
        compileman = CompileMan()
        is_posix_result = compileman.is_posix('linux2') 
        self.assertTrue(is_posix_result)

    def test_is_posix_true_3(self):
        compileman = CompileMan()
        is_posix_result = compileman.is_posix('darwin') 
        self.assertTrue(is_posix_result)

    def test_is_posix_exception_invalid_name(self):
        compileman = CompileMan()
        with self.assertRaises(Exception):
            compileman.is_posix('not_valid')

    def test_universal_subprocess_call_exception(self):
        compileman = CompileMan()
        with self.assertRaises(Exception):
            compile.universal_subprocess_call(['dir'], 'unknown_platform')

    def test_exception_wrong_platform_invalid(self):
        compileman = CompileMan()
        platform = 'unknown_platform'
        with self.assertRaises(Exception):
            compileman.exception_wrong_platform(platform)

    def go_to_tmp(self):
        tmp_place = tempfile.gettempdir()
        os.chdir(tmp_place)
        
    def empty_folder(self):
        if os.path.exists('node_modules'):
            shutil.rmtree('node_modules')
        if os.path.exists('vendor'):
            shutil.rmtree('vendor')
