class Sort:

    def __init__(self):
        self._even_numbers = list()
        self._uneven_numbers = list()

    @property
    def even_numbers(self):
        return self._even_numbers

    @property
    def uneven_numbers(self):
        return self._uneven_numbers

    def add_number_to_list(self, number: int):
        if not isinstance(number, int):
            raise TypeError("wrong type provided")
        if number % 2 == 0:
            self._even_numbers.append(number)
        else:
            self._uneven_numbers.append(number)

    def cartesian_product(self):
        return [i * j for i in self._uneven_numbers for j in self._even_numbers]
