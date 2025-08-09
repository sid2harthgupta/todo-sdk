"""Extract docstrings to JSON for documentation"""
import json
import inspect
from src.todo_sdk_python.todo_sdk import TodoClient


def extract_class_docs(cls):
    docs = {
        "class": cls.__name__,
        "description": inspect.getdoc(cls),
        "methods": {}
    }

    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if not name.startswith('_'):
            signature = inspect.signature(method)
            docs["methods"][name] = {
                "description": inspect.getdoc(method),
                "signature": str(signature),
                "params": {
                    param: str(signature.parameters[param].annotation)
                    if signature.parameters[param].annotation != inspect._empty
                    else "Any"
                    for param in signature.parameters
                    if param != 'self'
                }
            }

    return docs


if __name__ == "__main__":
    docs = extract_class_docs(TodoClient)
    print(json.dumps(docs, indent=2))
