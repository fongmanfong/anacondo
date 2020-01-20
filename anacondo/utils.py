


	def update(dict, **kwargs):
		return dict.update((k, kwargs[k]) for k in set(kwargs).intersection(self.__dict__))