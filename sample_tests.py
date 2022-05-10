import unittest

from main import Code
from tree import LeafNode, InnerNode


class SampleTests(unittest.TestCase):

    code = Code()

    def test_example_string(self):
        result = self.code.create_code("abacaca")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("b", 1),
                                 LeafNode("c", 2)
                             ),
                             LeafNode("a", 4)
                         ))

    def test_one_letter(self):
        result = self.code.create_code("aaaaa")
        self.assertEqual(result, LeafNode("a", 5))
       
unittest.main()