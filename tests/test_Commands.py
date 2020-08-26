import unittest
import sys
sys.path.insert(1, "..")
from compileman.Commands import Commands

class test_Commands(unittest.TestCase):

    def test_is_command_given_true(self):
        commands = Commands(['cman', 'compile'])
        self.assertTrue(commands.is_command_given())

    def test_is_command_given_false(self):
        commands = Commands(['cman'])
        self.assertFalse(commands.is_command_given())

    def test_get_command_given_compile(self):
        commands = Commands(['cman', 'compile'])
        expected_result = 'compile'
        self.assertEqual(expected_result, commands.get_command_given())

    def test_get_command_given_clean(self):
        commands = Commands(['cman', 'clean'])
        expected_result = 'clean'
        self.assertEqual(expected_result, commands.get_command_given())

    def test_give_non_existent_command(self):
        with self.assertRaises(Exception):
            Commands(['cman', 'nonexistent'])
