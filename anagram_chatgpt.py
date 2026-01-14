def are_anagrams(str1, str2):
    # Remove any spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")



def test_anagram():
    test_cases = [
        # Test case format: (str1, str2, expected_output)
        ("listen", "silent", True),           # Basic anagram
        ("triangle", "integral", True),       # Basic anagram with different letters
        ("hello", "bello", False),            # Not an anagram
        ("Dormitory", "Dirty room", True),    # Anagram with spaces and different cases
        ("School master", "The classroom", True),  # Anagram with spaces and different cases
        ("Astronomer", "Moon starer", True),  # Another complex anagram
        ("Astronomers", "No more stars", True), # Edge case with a plural word
        ("apple", "pale", False),             # Not an anagram
        ("a gentleman", "elegant man", True), # Anagram with spaces
        ("aabbcc", "abcabc", True),           # Repeating characters
        ("123", "321", True),                 # Numbers as anagrams
        ("", "", True),                       # Empty strings
        ("abc", "abcd", False),               # Different lengths
    ]
    
    for i, (str1, str2, expected) in enumerate(test_cases, 1):
        result = are_anagrams(str1, str2)
        assert result == expected, f"Test case {i} failed: {str1}, {str2} -> Expected {expected}, but got {result}"
        print(f"Test case {i} passed.")

# Run the tests
test_anagram()
