import unittest


def reverse_integer(num):
    abs_num = abs(num)
    result = 0
    while abs_num != 0:
        pop = abs_num % 10
        abs_num //= 10
        result = result*10 + pop

    return result if num > 0 else -1*result


class test(unittest.TestCase):

    def test_rev(self):
        test_vals = [1234, -678, 0]
        expected_vals = [4321, -876, 0]

        actual_vals = [reverse_integer(v) for v in test_vals]

        for i, ev in enumerate(expected_vals):
            assert(ev == actual_vals[i])


if __name__ == '__main__':
    unittest.main()
