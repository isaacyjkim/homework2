class Array:

	def __init__(self, capacity):
		""" Capacity is the static size of the array. Each index is initialized to None """
		self._logical_size = 0

		self._items = []
		for i in range(capacity):
			self._items.append(None)

	def logical_size(self):
		return self._logical_size

	def __len__(self):
		""" Returns the capacity of this Array """

		return len(self._items)

	def __str__(self):
		""" Returns a string representation of this Array """

		return str(self._items)

	def __iter__(self):
		""" Returns an iterator over the Array """

		return iter(self._items)

	def __getitem__(self, index):
		""" Return the item at the given index """

		return self._items[index]

	def __eq__(self,other):
		"""Checks if other data type is an Array. If yes, then checks
		for the same logical size. """
		if (type(self)!=type(other)):
			return False
		elif (self._logical_size!=other._logical_size):
			return False

		# Checks the indexes in both arrays to see if they are the same
		for n in range(self._logical_size):
			if (self._items[n]!=other._items[n]):
				return False

		return True




	def __setitem__(self, index, new_item):
		""" Adds the value 'new_item' to the array at the given index """
		# Checks to see if the user wants to assign "None" value:
		# if true, next statement checks to see if the user assigns to the last
		# logical index. If so, assign None to the index and reduce logical size by 1.
		if (new_item == None):
			if (index!=self._logical_size-1):
				raise IndexError(f"Must assign 'none' to most outside index")
			else:
				self._items[index] = new_item
				self._logical_size-=1
				return

		# Checks to see if the user is changing the proper index.
		# If not, raise IndexError
		if ((index)>self._logical_size):
			raise IndexError("Cannot update index that is not the first logically empty index")

		try:
			self._items[index] = new_item
			if (index==self._logical_size):
				self._logical_size+=1
		except IndexError:
			raise IndexError("Array does not have an index " + str(index))
