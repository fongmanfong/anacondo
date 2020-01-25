


	def update(self, **kwargs):
		self.__dict__.update((k, kwargs[k]) for k in set(kwargs).intersection(self.__dict__))