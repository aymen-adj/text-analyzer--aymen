# Text Analyzer

A Python utility that analyzes text files and provides statistics including word count, sentence count, and the most frequent words.

## Features

- **Word Count**: Counts all words in the text (ignoring punctuation)
- **Sentence Count**: Counts sentences based on sentence-ending punctuation
- **Top 10 Frequent Words**: Identifies the 10 most commonly used words with their frequencies

## Requirements

This project relies entirely on the Python Standard Library. No external packages are required.

## Installation & Usage

1.  Clone this repository:

```bash
git clone <your-repo-url>
cd text-analyzer
```

2. Run the analyzer on the provided sample text:

```bash
python main.py
```

The script will read `sample_text.txt` from the current directory and display the analysis results.

## How It Works

1. **Sentence Counting**: Splits text on sentence-ending punctuation (`.`, `!`, `;`, `?`) followed by space, with a placeholder for ellipses to prevent false positives.
2. **Word Extraction**: Uses regex to extract words while handling:
   - Emails and URLs, so they aren't mangled by general word-finding rules.
   - Symbols, such as $100, 50%, #hashtags, @tags, etc.
   - Decimal numbers (e.g., 3.14)
   - Hyphenated words (e.g., end-to-end, tool-calling)
   - A final step to capture standard alphanumeric words and contractions (e.g., "don't").
3. **Frequency Analysis**: Uses Python's `Counter` to count word occurrences

## Files

- `main.py` - Main analyzer script with core functionality
- `README.md` - This file
- `requirements.txt` - Python dependencies (empty - uses standard library only)
- `sample_text.txt` - Sample text for testing
