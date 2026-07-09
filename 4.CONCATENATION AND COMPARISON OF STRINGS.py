class word:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
    def __eq__(self, other):
        return self.value == other.value
str1_input = input("Enter first string: ")
str2_input = input("Enter second string: ")
s1 = word(str1_input)
s2 = word(str2_input)
concatenated = s1 + s2
print("Concatenated String:", concatenated)
if s1 == s2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")
