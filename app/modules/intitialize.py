
'''Carrega todos os módulos em um diretório.'''

import os
import importlib.util

def load_all_modules_in_dir(dir_path: str):
    """
    Carrega todos os módulos em um diretório.
    """
    for file in os.listdir(dir_path):
        if file.endswith(".py") and not file.startswith("_"):
            file_path = os.path.join(dir_path, file)
            spec = importlib.util.spec_from_file_location(file.replace(".py", ""), file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

load_all_modules_in_dir(os.path.dirname(__file__))
