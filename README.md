## Introduction
This program takes a csv as input and exports a csv with the readings configured in a way that shows furigana when in Anki (spaced repetition flashcard app). The fields I use for my Japanese cards are: 

* Expression
* Reading
* Meaning
* Part of Speech
* Notes

Anki also puts tags at the end of csv rows

## Assumptions
* no mixed japanese + western characters
* 6th csv field is tags; this is so the program can look in row[5] for the 'scraped' tag
* a note w/ the 'scraped' tag doesn't have okurigana in the reading field, just the reading for kanji; this is how cards are set up in the jisho_to_csv program
* otherwise, assume the readings field includes okurigana that need to be removed
* if a reading has brackets, assume it is already configured correctly

## Limitations:
* I don't know what I'm doing lol
* this program is primarily intended for personal use, i don't expect it to be convenient for others to use in its current form