class Commands:

    def __init__(self, arguments_commandline: list):

        commands_allowed = ['compile', 'clean']

        if len(arguments_commandline) > 1:
            command = arguments_commandline[1]
            if not command in commands_allowed:
                raise Exception("You give an invalid command")

        self.arguments_commandline = arguments_commandline

    def is_command_given(self):
        return len(self.arguments_commandline) > 1

    def get_command_given(self):
        return self.arguments_commandline[1]
