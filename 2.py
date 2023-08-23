"""
A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.

    For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.

You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence.

Note that all prices will contain at most 10 digits.
"""

def format_sentence(sentence: str, discount: int) -> str:
    words = sentence.split()
    modified_words = []
    
    for word in words:
        if word.startswith('$') and word[1:].isdigit():
            price = int(word[1:])
            discounted_price = price * (100 - discount) / 100
            modified_word = f"${discounted_price:.2f}"
        else:
            modified_word = word
        modified_words.append(modified_word)
    
    return ' '.join(modified_words)