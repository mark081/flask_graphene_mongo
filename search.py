import unittest
from collections import deque


def binary_search(mylist, item):
    low = 0
    high = len(mylist)-1
    while low <= high:
        mid = (low + high)//2
        guess = mylist[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def breadth_first_search(graph, item, func):
    search_queue = deque()
    search_queue += graph[item]
    searched = []
    while search_queue:
        item = search_queue.popleft()
        if item not in searched:
            if func(item):
                print(item + " found")
                return True
            else:
                searched += item
                search_queue += graph[item]
    return False


class TestSearch(unittest.TestCase):

    test_graph = {}

    def setUp(self):
        self.test_graph["you"] = ["lori", "david", "alex"]
        self.test_graph["david"] = ["jheran", "jen"]
        self.test_graph["lori"] = ["jessica"]
        self.test_graph["alex"] = ["john", "michael"]
        self.test_graph["jheran"] = []
        self.test_graph["jen"] = []
        self.test_graph["jessica"] = []
        self.test_graph["john"] = []
        self.test_graph["michael"] = []

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 3), 3-1)

    def test_breadth_first_search(self):

        def person_is_seller(name):
            return name[-1] == 'a'

        self.assertTrue((self.test_graph, "you", person_is_seller))


if __name__ == "__main__":
    unittest.main()
