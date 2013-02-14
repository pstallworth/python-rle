import sys
from rle import encode
from rle import decode
import unittest

class TestRLE(unittest.TestCase):

	def test_encoder(self):
		self.assertEqual("10ab10c",encode("aaaaaaaaaabcccccccccc"))
	def test_decoder(self):
		self.assertEqual("aaaaaaaabbbbbcccd", decode("8a5b3cd"))
	def test_single_encode(self):
		self.assertEqual("a",encode("a"))
	def test_single_decode(self):
		self.assertEqual("a",decode("a"))

if __name__ == '__main__':
	unittest.main()
