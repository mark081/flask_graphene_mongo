import unittest


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(0, len(arr)):
        new_arr.append(arr.pop(find_smallest(arr)))
    return new_arr


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_subarray = [x for x in arr[1:] if x <= pivot]
        greater_subarray = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_subarray) + [pivot] + quick_sort(greater_subarray)


class TestSort(unittest.TestCase):

    def test_find_smallest(self):
        rev_array = [x for x in range(1, 10)]
        rev_array.reverse()
        self.assertEqual(find_smallest(rev_array), 8)

    def test_selection_sort(self):
        array = [5, 9, 2, 8, 7, 7]
        self.assertEqual(selection_sort(array), [2, 5, 7, 7, 8, 9])

    def test_quick_sort(self):
        array = [5, 9, 2, 8, 7, 7]
        self.assertEqual(quick_sort(array), [2, 5, 7, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
