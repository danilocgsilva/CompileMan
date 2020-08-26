import sys
from compileman.Commands import Commands
from compileman.CompileMan import CompileMan


def cman():
    compileman = CompileMan()

    commands = Commands(sys.argv)
    
    if not commands.is_command_given():
        command = compileman.guess_action()
    else:
        command = command.get_command_given()

    if command == '':
        print('You have not provided any command and it was not possible to guess. Tell if you want to compile or clean the compiled assets typing \'compile\' or \'clean\'.')
        exit()

    compileman.cancompile()
