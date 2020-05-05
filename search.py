import unittest


def binary_search(mylist, item):
    low = 0
    high = len(mylist)-1
    count = 0
    while low <= high:
        count += 1
        print(count)
        mid = (low + high)//2
        guess = mylist[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


class TestSearch(unittest.TestCase):

    @unittest.expectedFailure
    def test_binary_search(self):
        self.assertNotEqual(binary_search([1, 2, 3, 4, 5, 6], 3), 3-1)


if __name__ == "__main__":
    unittest.main()
