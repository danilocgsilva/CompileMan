import os
import subprocess


class CompileMan:

    def __init__(self):

        # print(self.check_for_app_placement('npm'))
        # print(self.check_for_app_placement('composer'))

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
        process = subprocess.Popen(['which', app], stdout=subprocess.PIPE)
        out, err = process.communicate()
        return str(out)

    def get_cannot_compile_reasons(self) -> list:
        return self.cannot_compile_reasons

    def compile_all(self):
        print('lets compile')
        for compilling_type in self.compiling_types:
            if compilling_type == "php":
                subprocess.call(['composer', 'install'])
            if compilling_type == "node":
                subprocess.call(['npm', 'install'])

    def clean(self, compiling_types: list):

        for compile_type in compiling_types:
            if not compile_type in ['php','node']:
                raise Exception('The parameters provided in clean method is not valid.')
        
