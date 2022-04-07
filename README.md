## Introduction
This program takes a csv as input and exports a csv with the readings configured in a way that shows furigana when in Anki (spaced repetition flashcard app). The fields I use for my Japanese cards are: 

* Expression
* Reading
* Meaning
* Part of Speech
* Notes

Anki also puts tags at the end of csv rows

## Assumptions
Boy we got a lotta these, huh
* reading is just kana, no kanji
* no mixed japanese + western characters
* 6th csv field is tags; this is so the program can look in row[5] for the 'scraped' tag
* a note w/ the 'scraped' tag doesn't have okurigana in the reading field, just the reading for kanji; this is how cards are set up in the jisho_to_csv program
* otherwise, assume the readings field includes okurigana that need to be removed
* if a reading has brackets, assume it is already configured correctly
* if a note has no reading, it is assumed that the reading should be the expression. A note should only have no reading if the expression is just kana, and only words without kanji will be processed this way. 

!!! Words with kanji, but no reading, will not be configured properly for furigana !!!

* BIG ASSUMPTION: the reading is assumed to be correct!

## Limitations:
* I don't know what I'm doing lol
* this program is primarily intended for personal use, i don't expect it to be convenient for others to use in its current form
* I was never taught the proper way to code in python, so my use of functions and main and such may not be conventional. They might also BE conventional, I can't tell the difference!