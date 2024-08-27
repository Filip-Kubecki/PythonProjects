import tools
import unittest


class TestTools(unittest.TestCase):

    def test_index_to_posistion(self):
        self.assertEqual(tools.index_to_position(0), (0, 0))
        self.assertEqual(tools.index_to_position(1199), (780, 580))

    def test_position_to_index(self):
        result = tools.position_to_index((680, 0))
        self.assertEqual(result, 34)


if __name__ == '__main__':
    unittest.main()
