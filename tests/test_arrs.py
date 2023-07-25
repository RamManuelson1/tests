from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
def test_slice_with_negative_start_index():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, 4) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]

def test_slice_with_negative_end_index():
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, -1) == [2, 3, 4]

def test_slice_with_negative_indices_out_of_range():
    assert arrs.my_slice([1, 2, 3, 4, 5], -7, -6) == []

    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 10) == [3, 4, 5]

def test_slice_with_default_arguments():
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([]) == []
