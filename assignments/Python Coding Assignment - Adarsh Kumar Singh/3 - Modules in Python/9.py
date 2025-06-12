import importlib

module_name = "module1"
function_name = "add"

module = importlib.import_module(module_name)
function = getattr(module, function_name)

result = function(5, 3)
print(f"Result: {result}")
