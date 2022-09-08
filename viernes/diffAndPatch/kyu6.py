from string import ascii_lowercase

class DetectPangram:
    # A pangram is a sentence that contains every single letter of the alphabet at least once.
    # For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
    # because it uses the letters A-Z at least once (case is irrelevant).
    # Given a string, detect whether or not it is a pangram.
    # Return True if it is, False if not. Ignore numbers and punctuation.

    @staticmethod
    def is_pangram(s):
        return False

    @staticmethod
    def is_pangram(s):
        letter_list = [ch for ch in sorted(set(list(s.lower()))) if ch in ascii_lowercase]
        return letter_list == list(ascii_lowercase)