import unittest
import TestRunner
from kyu7 import FriendOrFoe, RegexValidatePinCode, HighestAndLowest, VowelCount
from random import choice, randint, shuffle, choices, sample
from string import ascii_letters as abc


class FriendOrFoeTests(unittest.TestCase):

    def test_basic_cases(self):
        self.assertListEqual(FriendOrFoe.friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])
        self.assertListEqual(FriendOrFoe.friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
        self.assertListEqual(FriendOrFoe.friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]),
                             ["Jimm", "Cari", "aret"])
        self.assertListEqual(FriendOrFoe.friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"])
        self.assertListEqual(FriendOrFoe.friend(["Hell", "Is", "a", "badd", "word"]), ["Hell", "badd", "word"])
        self.assertListEqual(FriendOrFoe.friend(["Issa", "Issac", "Issacs", "ISISS"]), ["Issa"])
        self.assertListEqual(FriendOrFoe.friend(["Robot", "Your", "MOMOMOMO"]), ["Your"])
        self.assertListEqual(FriendOrFoe.friend(["Your", "BUTT"]), ["Your", "BUTT"])
        self.assertListEqual(FriendOrFoe.friend(["Hello", "I", "AM", "Sanjay", "Gupt"]), ["Gupt"])
        self.assertListEqual(FriendOrFoe.friend(["This", "IS", "enough", "TEst", "CaSe"]),
                             ["This", "TEst", "CaSe"])
        self.assertListEqual(FriendOrFoe.friend([]), [])

    def random_string(self,friend=False):
        return "".join(choice(abc) for _ in range(friend and 4 or randint(0, 20)))

    def random_input(self):
        return [self.random_string(randint(0, 100) % 4 == 0) for _ in range(randint(0, 20))]

    def solution(self,l):
        return [w for w in l if len(w) == 4]

    def test_random_cases(self):
        for _ in range(100):
            ri = self.random_input()
            expected = self.solution(ri)
            self.assertListEqual(FriendOrFoe.friend(ri), expected)


class RegexValidatePinCodeTests(unittest.TestCase):
            
    def test_false_for_invalid_length(self):
            # should return False for pins with length other than 4 or 6
            self.assertEqual(RegexValidatePinCode.validate_pin("1"), False, "Wrong output for '1'")
            self.assertEqual(RegexValidatePinCode.validate_pin("12"), False, "Wrong output for '12'")
            self.assertEqual(RegexValidatePinCode.validate_pin("123"), False, "Wrong output for '123'")
            self.assertEqual(RegexValidatePinCode.validate_pin("12345"), False, "Wrong output for '12345'")
            self.assertEqual(RegexValidatePinCode.validate_pin("1234567"), False, "Wrong output for '1234567'")
            self.assertEqual(RegexValidatePinCode.validate_pin("-1234"), False, "Wrong output for '-1234'")
            self.assertEqual(RegexValidatePinCode.validate_pin("-12345"), False, "Wrong output for '-12345'")
            self.assertEqual(RegexValidatePinCode.validate_pin("1.234"), False, "Wrong output for '1.234'")
            self.assertEqual(RegexValidatePinCode.validate_pin("00000000"), False, "Wrong output for '00000000'")

    def test_false_for_invalid_characters(self):
            self.assertEqual(RegexValidatePinCode.validate_pin("a234"), False, "Wrong output for 'a234'")
            self.assertEqual(RegexValidatePinCode.validate_pin(".234"), False, "Wrong output for '.234'")

    def test_valid_inputs(self):
        self.assertEqual(RegexValidatePinCode.validate_pin("1234"), True, "Wrong output for '1234'")
        self.assertEqual(RegexValidatePinCode.validate_pin("0000"), True, "Wrong output for '0000'")
        self.assertEqual(RegexValidatePinCode.validate_pin("1111"), True, "Wrong output for '1111'")
        self.assertEqual(RegexValidatePinCode.validate_pin("123456"), True, "Wrong output for '123456'")
        self.assertEqual(RegexValidatePinCode.validate_pin("098765"), True, "Wrong output for '098765'")
        self.assertEqual(RegexValidatePinCode.validate_pin("000000"), True, "Wrong output for '000000'")
        self.assertEqual(RegexValidatePinCode.validate_pin("123456"), True, "Wrong output for '123456'")
        self.assertEqual(RegexValidatePinCode.validate_pin("090909"), True, "Wrong output for '090909'")


class HighestAndLowestTests(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(HighestAndLowest.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
        self.assertEqual(HighestAndLowest.high_and_low("1 -1"), "1 -1");
        self.assertEqual(HighestAndLowest.high_and_low("1 1"), "1 1");
        self.assertEqual(HighestAndLowest.high_and_low("-1 -1"), "-1 -1");
        self.assertEqual(HighestAndLowest.high_and_low("1 -1 0"), "1 -1");
        self.assertEqual(HighestAndLowest.high_and_low("1 1 0"), "1 0");
        self.assertEqual(HighestAndLowest.high_and_low("-1 -1 0"), "0 -1");
        self.assertEqual(HighestAndLowest.high_and_low("42"), "42 42");

    def test_random_cases(self):
        for t in range(10):
            lo = randint(-500, 500)
            hi = lo + 3000 + randint(1, 100)
            arg = [hi, lo] + [str(lo + randint(1, 2999)) for i in range(20)]
            shuffle(arg)
            arg = " ".join(str(a) for a in arg)
            exp = "%i %i" % (hi, lo)

            self.assertEqual(HighestAndLowest.high_and_low(arg), exp)

class VowelCountTests(unittest.TestCase):

    vowels = "aeiou"
    nonvowels = "bcdfghjklmnpqrstvwxyz"

    def test_all_vowels(self):
        self.assertEqual(VowelCount.getCount("aeiou"), 5, f"Incorrect answer for \"aeiou\"")

    def test_only_y(self):
        self.assertEqual(VowelCount.getCount("y"), 0, f"Incorrect answer for \"y\"")

    def test_no_vowels(self):
        self.assertEqual(VowelCount.getCount("bcdfghjklmnpqrstvwxz y"), 0,
                           f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")

    def test_string_empty(self):
        self.assertEqual(VowelCount.getCount(""), 0, f"Incorrect answer for empty string")

    def test_abracadabra(self):
        self.assertEqual(VowelCount.getCount("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")
    
    def generate_tests(self, generator, count):
        return [generator() for _ in range(count)]

    def generate_no_vowels(self):
        word_count = randint(1, 10)
        words = ["".join(choices(self.nonvowels, k=randint(1, 8))) for _ in range(word_count)]
        sentence = " ".join(words)
        return (sentence, 0)

    def generate_only_vowels(self):
        word_count = randint(1, 10)
        words = ["".join(choices(self.vowels, k=randint(1, 8))) for _ in range(word_count)]
        sentence = " ".join(words)
        return (sentence, sum(len(word) for word in words))

    def generate_mixed(self):
        word_count = randint(1, 10)
        vowel_parts = ["".join(choices(self.vowels, k=randint(1, 3))) for _ in range(word_count)]
        nonvowel_parts = ["".join(choices(self.nonvowels, k=randint(1, 8))) for _ in range(word_count)]
        words = ["".join(sample(v + nv, k=len(v + nv))) for v, nv in zip(vowel_parts, nonvowel_parts)]
        sentence = " ".join(words)
        return (sentence, sum(len(word) for word in vowel_parts))
    
    def test_random(self):
        test_cases = self.generate_tests(self.generate_no_vowels, 10) + \
                     self.generate_tests(self.generate_only_vowels, 10) + \
                     self.generate_tests(self.generate_mixed, 80)
        shuffle(test_cases)

        for input, expected in test_cases:
            actual = VowelCount.getCount(input)
            self.assertEqual(actual, expected, 
                             f"Incorrect answer for input: \"{input}\"\nActual: {actual}\nExpected: {expected}")


if __name__ == '__main__':
    unittest.main(testRunner = TestRunner.TestRunner())