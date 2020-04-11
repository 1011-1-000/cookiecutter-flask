import importlib


def get_instance_of_attr(path):
	module, function = path.rsplit('.', maxsplit=1)
	module_instance = importlib.import_module(module)
	if hasattr(module_instance, function):
		return getattr(module_instance, function)
	else:
		raise AttributeError
