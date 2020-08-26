import os


class CompileMan:

    def guess_action(self):
        if not self.is_node_module_exists() and not self.is_vendor_exists():
            return 'compile'
        if self.is_node_module_exists() and self.is_vendor_exists():
            return 'clean'
        return ''

    def is_node_module_exists(self):
        content_list = os.listdir()
        return 'node_modules' in content_list

    def is_vendor_exists(self):
        content_list = os.listdir()
        return 'vendor' in content_list

