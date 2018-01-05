# Crossword generator
Program to generate crosswords algorithmically using Guardian Quick Crossword clues

## 1. Scraper
Script to scrape clues/solutions from the Guardian website.

1. Starting at the oldest online id (9251), load each crossword page in turn (URL format https://www.theguardian.com/crosswords/quick/:id)
2. Grab the data-crossword-data attribute of the div with class js-crossword. 
3. Parse the JSON string to an object. Save in an array or database for further processing later.
4. From the raw output, parse individual clues into a new dataset.
5. Again from the raw output, parse crossword layouts into a new dataset.
