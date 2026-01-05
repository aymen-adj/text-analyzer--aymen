import re
from collections import Counter
from typing import Dict

def analyze_text(text: str) -> Dict:
    """
    Analyze text and return
    - Word count
    - Sentence count
    - Top 10 most frequent words, ignoring punctuation
    
    Args:
        text: The input text string to analyze
        
    Returns:
        Dictionary containing:
            - word_count: Total number of words
            - sentence_count: Total number of sentences
            - top_words: List of tuples (word, frequency) for top 10 words
    """

    #! ----- Sentences count -----
    # replace ellipses with a placeholder
    placeholder = "ELLIPSIS_PLACEHOLDER"
    text_temp = text.replace("...", placeholder)

    # split by punctuation
    sentences = re.split(r'[.!?;]+\s+', text_temp)
    # filter out empty strs
    sentences = [s.strip() for s in sentences if s.strip()]

    sentence_count = len(sentences)

    #! ----- Word count -----
    words = []
    
    #* Find emails and URLs
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    url_pattern = r"https?://[^\s]+|www\.[^\s]+"
    
    emails = re.findall(email_pattern, text)
    urls = re.findall(url_pattern, text)

    words += emails + urls

    # Remove emails and URLs
    text_temp = re.sub(email_pattern, "", text)
    text_temp = re.sub(url_pattern, "", text_temp)
    
    #* Symbols
    # find "$"
    dollar_pattern = r"\$\d+\b" # a number with $ at the beginning
    dollars = re.findall(dollar_pattern, text_temp)
    words += dollars
    text_temp = re.sub(dollar_pattern, "", text_temp)

    # find "%"
    percent_pattern = r"\b\d+%" # a number with % at the end
    precents = re.findall(percent_pattern, text_temp)
    words += precents
    text_temp = re.sub(percent_pattern, "", text_temp)

    # # and @
    hashtag_at_pattern = r"(?:[@#]\w+)"
    hashtag_ats = re.findall(hashtag_at_pattern, text_temp)
    words += hashtag_ats
    text_temp = re.sub(hashtag_at_pattern, "", text_temp)

    #* Decimal numbers
    decimal_number_pattern = r"\b\d+[\.,]\d+\b"
    decimal_numbers = re.findall(decimal_number_pattern, text_temp)
    words += decimal_numbers
    text_temp = re.sub(decimal_number_pattern, "", text_temp)

    #* Hyphenated words
    hyphen_pattern = r"\b\w+(?:[—-]\w+)+\b"
    hyphenated_words = re.findall(r"\b\w+(?:-\w+)+\b", text_temp)
    words += hyphenated_words
    text_temp = re.sub(hyphen_pattern, "", text_temp)

    #* The rest
    pattern = r"\b\w+(?:['’]\w+)?\b"
    words += re.findall(pattern, text_temp)

    word_count = len(words)
    
    #! ----- Top 10 most frequent words -----
    word_freq = Counter(words)
    top_words = word_freq.most_common(10)
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'top_words': top_words
    }

def main():
    try:
        with open('sample_text.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        
        results = analyze_text(text)
        
        print("Text Analysis Results")
        print("---------------------")
        print(f"Word count: {results['word_count']}")
        print(f"Sentence count: {results['sentence_count']}")
        print("\nTop 10 most frequent words:")
        for i, (word, freq) in enumerate(results["top_words"], 1):
            print(f"{i:2d}. {word:20s} - {freq:3d} occurrences")

        
    except FileNotFoundError:
        print("Error: sample_text.txt not found!")
        print("Please ensure the file exists in the same directory as this script.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
