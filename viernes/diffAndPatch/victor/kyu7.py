class FriendOrFoe:
    # Make a program that filters a list of strings and returns a list with only your friends name in it.
    # If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
    #
    # Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
    #
    # i.e.
    # friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
    #
    # Note: keep the original order of the names in the output.

    @staticmethod
    def friend(x):
        return [f for f in x if len(f) == 4]


class RegexValidatePinCode:
    # ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
    #
    # If the function is passed a valid PIN string, return true, else return false.
    # Examples (Input --> Output)
    #
    # "1234"   -->  true
    # "12345"  -->  false
    # "a234"   -->  false

    @staticmethod
    def validate_pin(pin):
        return all(x.isdigit() for x in pin) and len(pin) in (4,6)

class HighestAndLowest:
    # In this little assignment you are given a string of space separated numbers,
    # and have to return the highest and lowest number.
    #
    # Example:
    #
    # high_and_low("1 2 3 4 5")  # return "5 1"
    # high_and_low("1 2 -3 4 5") # return "5 -3"
    # high_and_low("1 9 3 4 -5") # return "9 -5"
    #
    # Notes:
    #
    #     All numbers are valid Int32, no need to validate them.
    #     There will always be at least one number in the input string.
    #     Output string must be two numbers separated by a single space, and highest number is first.

    @staticmethod
    def high_and_low(numbers):
        nums = numbers.split(" ")
        mas_alto = nums[0]
        mas_bajo = nums[0]
        for num in nums:
            if int(num) > int(mas_alto):
                mas_alto = num
            if int(num) < int(mas_bajo):
                mas_bajo = num
        return mas_alto + ' ' + mas_bajo


class VowelCount:
    # Return the number (count) of vowels in the given string.
    # We will consider a, e, i, o, u as vowels for this Kata (but not y).
    # The input string will only consist of lower case letters and/or spaces.

    @staticmethod
    def getCount(sentence):
        num_vowels = 0
        for char in sentence:
            if char in "aeiou":
                num_vowels = num_vowels + 1
        return num_vowels
