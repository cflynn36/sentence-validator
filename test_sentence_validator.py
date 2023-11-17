import unittest
from sentence_validator import SentenceValidator


class TestSentenceValidator(unittest.TestCase):

    def test_is_valid(self):
        # Check if the entire is_valid function correctly detects a valid sentence.
        validator = SentenceValidator("The quick brown fox said “hello Mr lazy dog”.")
        self.assertTrue(validator.is_valid())

        # Check if the entire is_valid function correctly detects an invalid sentence.
        validator = SentenceValidator("The quick brown fox said \"hello Mr. lazy dog\".")
        self.assertFalse(validator.is_valid())


    def test_begins_with_capital(self):
        # Check if begins_with_capital() correctly detects a sentence that starts with a capital letter.
        validator = SentenceValidator("The quick brown fox.")
        self.assertTrue(validator.begins_with_capital())

        # Check if begins_with_capital() correctly detects a sentence that does not start with a capital letter.
        validator = SentenceValidator("the quick brown fox.")
        self.assertFalse(validator.begins_with_capital())

    def test_has_even_number_of_quotes(self):
        # Check if has_even_number_of_quotes() correctly detects a sentence with an even number of quotes.
        validator = SentenceValidator('"One lazy dog"')
        self.assertTrue(validator.has_even_number_of_quotes())

        # Check if has_even_number_of_quotes() correctly detects a sentence with an odd number of quotes.
        validator = SentenceValidator('""One lazy dog"')
        self.assertFalse(validator.has_even_number_of_quotes())

    def test_has_correct_termination_character(self):
        # Check if has_correct_termination_character() correctly detects a sentence with a correct termination char.
        validator = SentenceValidator("How many lazy dogs?")
        self.assertTrue(validator.has_correct_termination_character())

        # Check if has_correct_termination_character() correctly detects a sentence with an incorrect termination char.
        validator = SentenceValidator("How many lazyz dogs")
        self.assertFalse(validator.has_correct_termination_character())

    def test_has_no_extra_periods(self):
        # Check if has_no_extra_periods() correctly detects a sentence with no extra periods.
        validator = SentenceValidator("My lazy dog.")
        self.assertTrue(validator.has_no_extra_periods())

        # Check if has_no_extra_periods() correctly detects a sentence with extra periods.
        validator = SentenceValidator("My lazy dog..")
        self.assertFalse(validator.has_no_extra_periods())

    def test_numbers_spelled_out(self):
        # Check if numbers_spelled_out() correctly detects a sentence with numbers below max_digits spelled out.
        validator = SentenceValidator("There are twelve lazy dogs.")
        self.assertTrue(validator.numbers_spelled_out())

        # Check if numbers_spelled_out() correctly detects a sentence with numbers below max_digits not spelled out.
        validator = SentenceValidator("There are 12 lazy dogs.")
        self.assertFalse(validator.numbers_spelled_out())

# Run the unit tests when this script is executed as the main program.
if __name__ == "__main__":
    unittest.main()
