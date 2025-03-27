import unittest
import unit_test_cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'jawad'
		result = unit_test_cap.cap_text(text)
		self.assertEqual(result, 'Jawad')
	
	def test_multiple_words(self):
		text = 'monty python'
		result = unit_test_cap.cap_text(text)
		self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
	unittest.main()
	