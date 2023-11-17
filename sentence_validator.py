class SentenceValidator:
    """
    Class for validating a sentence based on the following criteria:
            String starts with a capital letter.
            String has an even number of quotation marks.
            String ends with one of the following sentence termination characters: ".", "?", "!"
            String has no period characters other than the last character.
            Numbers below 13 are spelled out ( ”one”, “two”, "three”, etc…).
    """

    def __init__(self, sentence_to_check):
        # Initialize the SentenceValidator with a sentence to check.
        self.sentence_to_check = sentence_to_check

    def is_valid(self):
        # Run all of the above sentence checks and return a bool indicating pass or fail.
        return all([
            self.begins_with_capital(),
            self.has_even_number_of_quotes(),
            self.has_correct_termination_character(),
            self.has_no_extra_periods(),
            self.numbers_spelled_out()
            ])

    def begins_with_capital(self):
        # Check if string starts with a capital letter.
        return self.sentence_to_check[0].isupper()

    def has_even_number_of_quotes(self):
        # Check if string has an even number of quotation marks.
        return self.sentence_to_check.count('"') % 2 == 0

    def has_correct_termination_character(self):
        # Check if string ends with one of the following sentence termination characters: '.', '?', '!'.
        return self.sentence_to_check.endswith(('!', '.', '?'))

    def has_no_extra_periods(self):
        # Check if string has no period characters other than the last character.
        return self.sentence_to_check[:-1].count('.') == 0

    def numbers_spelled_out(self):
        # Check if numbers below max_digit are spelled out ('one', 'two', 'three', etc.).
        max_digit = 13
        words = self.sentence_to_check.split()

        for word in words:
            if word.isdigit() and int(word) < max_digit:
                return False

        return True



