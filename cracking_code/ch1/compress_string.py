import unittest


class Test(unittest.TestCase):

    def test_compressed(self):

        strings = ['aabccccaa', 'hey']
        compressed = ['a2b1c4a2', 'hey']

        for i in range(len(strings)-1):
            self.assertEquals(compressed[i], compress_string(strings[i]))


def compress_string(s):

    counter = 0
    compressed_s = []
    for i, char in enumerate(s):
        counter += 1
        if (i >= len(s) - 1) or (s[i+1] != char):
            compressed_s.append(char)
            compressed_s.append(str(counter))
            counter = 0
    return s if len(s) <= len(compressed_s) else ''.join(compressed_s)


if __name__ == '__main__':
    unittest.main()
