import unittest
import enigma
import string
import random

abcs = [i for i in string.ascii_lowercase]

class TestStringMethods(unittest.TestCase):

    def test_encrypt_decrypt(self):
        input = "This is a test"
        keys = random.choices(abcs, k=1)
        encrypted_message = enigma.main(input, keys)
        decrypted_message = enigma.main(encrypted_message, keys)

        print(f"{keys}\n{encrypted_message}\n{decrypted_message}")

        self.assertEqual(decrypted_message, input)


if __name__ == '__main__':
    unittest.main()