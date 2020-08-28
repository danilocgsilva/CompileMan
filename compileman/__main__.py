import sys
from compileman.Commands import Commands
from compileman.CompileMan import CompileMan


def cman():
    compileman = CompileMan()

    commands = Commands(sys.argv)
    
    if not commands.is_command_given():
        command = compileman.guess_action()
    else:
        command = commands.get_command_given()

    if command == '':
        print('You have not provided any command and it was not possible to guess. Tell if you want to compile or clean the compiled assets typing \'compile\' or \'clean\'.')
        exit()

    project_types = compileman.get_project_types()

    if command == 'compile':
        can_compile = compileman.cancompile(project_types)
        if not can_compile:
            for reasons in compileman.get_cannot_compile_reasons():
                print(reasons)
        else:
            for project_type in project_types:
                print("Compiling to project type of " + project_type)
                compileman.compile(project_type)

    if command == 'clean':
        for compilling_type in project_types:
            print("Removing project of type " + compilling_type)
            results = compileman.clean_project_type(compilling_type)

            if results.getResult():
                resultMessage = "The project " + compilling_type + " has been removed."
            else:
                resultMessage = results.getErrorMessage()

            print(resultMessage)


