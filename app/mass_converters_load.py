import os
import glob
import ast


def get_converters():
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    CONVERTERS_PATH = ROOT_PATH + "/app/converters/"
    converters = set()
    for file in glob.glob(os.path.join(os.path.dirname(CONVERTERS_PATH), "*.py")):
        source = open(file, "r").read()
        p = ast.parse(source)
        for item in [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]:
            converters.add(item)

    return converters