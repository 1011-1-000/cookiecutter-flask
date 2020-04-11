from datetime import date, datetime


class DictMixin(object):
	"""docstring for DictMixin"""

	@staticmethod
	def to_dict(cls, exlcude=[]):

		attrs = cls.__dict__
		attrs_dict = {}

		for key, value in attrs.items():
			if key.startswith('_') or key in exlcude:
				pass
			elif isinstance(value, date):
				attrs_dict[key] = date.strftime(value, '%Y-%m-%d')
			elif isinstance(value, datetime):
				attrs_dict[key] = datetime.strftime(value, '%Y-%m-%d %H:%M:%S')
			else:
				attrs_dict[key] = value

		return attrs_dict

	@staticmethod			
	def from_dict(cls, attrs):
		"""
		set the attributes of the cls.
		Also, will create a new instance if not an instance be provided
		"""
		if isinstance(cls, type):
			cls_instance = cls()
		else:
			cls_instance = cls

		for key, value in attrs.items():
			if hasattr(cls_instance, key):
				setattr(cls_instance, key, value)

		return cls_instance
