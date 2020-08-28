import os
import subprocess
import shutil
from sys import platform
from compileman.Compile_Result import Compile_Result


class CompileMan:

    def __init__(self):

        self.current_folder_list_content = os.listdir()
        self.npm_exists = False if self.check_for_app_placement('npm') == "" else True
        self.composer_exists = False if self.check_for_app_placement('composer') == "" else True
        self.cannot_compile_reasons = []
        self.compiling_types = []

    def guess_action(self):
        if not self.is_node_module_exists() and not self.is_vendor_exists():
            return 'compile'
        if self.is_node_module_exists() and self.is_vendor_exists():
            return 'clean'
        return ''

    def is_node_module_exists(self):
        return 'node_modules' in self.current_folder_list_content

    def is_vendor_exists(self):
        return 'vendor' in self.current_folder_list_content

    def get_project_types(self):
        compiling_types = []
        for file in self.current_folder_list_content:
            if file == 'package.json':
                compiling_types.append('node')
            if file == 'composer.json':
                compiling_types.append('php')
        return compiling_types

    def cancompile(self, compilations: list) -> bool:

        if len(compilations) == 0:
            return False

        for compilation_type in compilations:

            if not compilation_type in ['node','php']:
                raise Exception("Compilation type provided not exists.")

            if compilation_type == 'node':
                if self.npm_exists:
                    can_compile = True
                else:
                    self.cannot_compile_reasons.append('The project is of node type, but npm is not installed in the system.')

            if compilation_type == 'php':
                if self.composer_exists:
                    can_compile = True
                else:
                    self.cannot_compile_reasons.append('The project is of php type, but composer is not installed in the system.')

        self.compiling_types = compilations

        return can_compile if len(self.cannot_compile_reasons) == 0 else False

    def check_for_app_placement(self, app: str) -> str:
        if self.is_posix(platform):
            process = subprocess.Popen(['which', app], stdout=subprocess.PIPE)
            out, err = process.communicate()
            return str(out)
        else:
            status_exec = subprocess.call('where ' + app + ' > NUL', shell=True)
            if status_exec == 0:
                return app
            else:
                return ""

    def get_cannot_compile_reasons(self) -> list:
        return self.cannot_compile_reasons

    def compile(self, project_type: str):
        if project_type == 'node':
            self.universal_subprocess_call(['npm', 'install'], platform)
        if project_type == 'php':
            self.universal_subprocess_call(['composer', 'install'], platform)

    def clean_project_type(self, project_type: str):

        if not project_type in ['php','node']:
            raise Exception('The parameters provided in clean method is not valid.')

        compile_result = Compile_Result()

        correlation = {
            "node": "node_modules",
            "php": "vendor"
        }
        
        if os.path.exists(correlation[project_type]):
            shutil.rmtree(correlation[project_type])
            return compile_result.setSuccess()
        else:
            return compile_result.setError("The folder " + correlation[project_type] + " already does not exists. The directory is already cleaned.")

    def is_posix(self, platform: str):
        self.exception_wrong_platform(platform)
        if platform == "linux" or platform == "linux2":
            return True
        elif platform == "darwin":
            return True
        elif platform == "win32":
            return False

    def universal_subprocess_call(self, subprocess_arguments: list, platform):
        self.exception_wrong_platform(platform)
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            subprocess.call(subprocess_arguments)
        elif platform == "win32":
            subprocess.call(subprocess_arguments, shell=True)

    def exception_wrong_platform(self, platform):
        if platform not in ['linux', 'linux2', 'win32', 'darwin']:
            raise Exception('The platform name give is invalid.')
