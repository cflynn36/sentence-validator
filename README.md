# Sentence Validator

Sentence Validator is an OOP style Python project that allows you to validate an inputted sentence based on a number of criteria such as:

- Capitalization: Check if the sentence starts with a capital letter.
- Quotation Marks: Check if the sentence has an even number of quotation marks.
- Termination Characters: Check if the sentence ends with one of the following sentence termination characters: '.', '?', '!'.
- Periods: Check if the sentence has no period characters other than the last character.
- Number Spelling: Check if numbers below max_digit are spelled out ('one', 'two', 'three', etc.).


### Installation

1. **Prerequisites**:

   Before you begin, make sure you have the following prerequisites installed on your system:

   - Git: If you don't have Git installed, download and install it from [Git's official website](https://git-scm.com/downloads).


2. **Clone the Repository**:

   Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Use the following command to clone the repository:

   ```bash
   git clone https://github.com/cflynn36/sentence-validator.git
   ```
   
## Usage

The Sentence Validator module provides a `SentenceValidator` class with various methods for sentence validation. To use it, follow these steps:

### Import the `SentenceValidator` class:

   ```python
   from sentence_validator import SentenceValidator
   ```
Create an instance of the SentenceValidator class with the sentence you want to validate
   ```python
   sentence = "The quick brown fox jumps over the lazy dog."
   validator = SentenceValidator(sentence)
   ```
   Check if the sentence meets the validation criteria using the is_valid method:
```python
   if validator.is_valid():
       print("The sentence is valid.")
   else:
       print("The sentence is not valid.")
```