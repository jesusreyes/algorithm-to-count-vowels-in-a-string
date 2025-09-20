def count_vowels(text: str) -> int:
    """Count the number of vowels in a given string."""

    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    sample_string = "Hello, how many vowels are in this sentence? maybe 10?"
    print(f"Number of vowels in the sample string: {count_vowels(sample_string)}")