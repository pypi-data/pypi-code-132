import importlib
import pkgutil

# Recursively import all the submodule structure.
# https://stackoverflow.com/questions/3365740/how-to-import-all-submodules/25083161#25083161

def import_submodules(package):
    """
    Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """

    if isinstance(package, str):
        package = importlib.import_module(package)
    
    results = {}
    
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):

        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)

        if is_pkg:
            results.update(import_submodules(full_name))
    
    
    return results

import_submodules(__name__)

del importlib, pkgutil, import_submodules