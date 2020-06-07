import pytest

from sorting.Sorting import Sort


@pytest.fixture(scope="function")
def sort() -> Sort:
    return Sort()


class TestSort:

    def test_add_even_numbers(self, sort):
        sort.add_number_to_list(2)
        sort.add_number_to_list(4)
        sort.add_number_to_list(6)

        assert sort.even_numbers == [2, 4, 6]
        assert not sort.uneven_numbers

    def test_add_uneven_numbers(self, sort):
        sort.add_number_to_list(1)
        sort.add_number_to_list(3)
        sort.add_number_to_list(5)

        assert sort.uneven_numbers == [1, 3, 5]
        assert not sort.even_numbers

    def test_non_int_raises(self, sort):
        with pytest.raises(TypeError):
            sort.add_number_to_list(1.)

    def test_cartesian_product(self, sort):
        sort.add_number_to_list(1)
        sort.add_number_to_list(2)
        sort.add_number_to_list(3)
        sort.add_number_to_list(4)

        assert sort.cartesian_product() == [2, 4, 6, 12]
