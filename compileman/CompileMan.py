import os
import subprocess
import shutil
from sys import platform


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
            raise Exception('Still not implemented in systems that are not Posix (Mac Os or Linux)')


    def get_cannot_compile_reasons(self) -> list:
        return self.cannot_compile_reasons

    def compile(self, project_type: str):
        if project_type == 'node':
            subprocess.call(['npm', 'install'])
        if project_type == 'php':
            subprocess.call(['composer', 'install'])

    def clean_project_type(self, project_type: str):

        if not project_type in ['php','node']:
            raise Exception('The parameters provided in clean method is not valid.')
        
        if project_type == 'node':
            shutil.rmtree('node_modules')

        if project_type == 'php':
            shutil.rmtree('vendor')

    def is_posix(self, platform: str):
        if platform == "linux" or platform == "linux2":
            return True
        elif platform == "darwin":
            return True
        elif platform == "win32":
            return False
