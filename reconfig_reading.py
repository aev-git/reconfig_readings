import csv
import regex as re

try: 
    scraped = False
    sourcefile = input("csv file: ")
    with open(sourcefile, encoding="utf8") as f:
        csv_f = csv.reader(f)

        for row in csv_f:
            if len(row) > 0: #line isn't empty

                if len(row) >= 6: #makes sure the following doesn't result in an error
                    if row[5] == "scraped":
                        scraped = True  
                
                exprs = row[0]
                reading = row[1]
                
                if "[" not in reading:
                    if len(reading) == 0:
                        print("reading: "+ reading)
                        reading = exprs
                        print("new reading: " + reading)
                    hasKanji = re.search(r'\p{Han}', exprs)
                    hasKana = re.search(r'\p{Hiragana}|\p{Katakana}', exprs)

                    if hasKanji and not hasKana:
                        print(exprs + ": just kanji")
                    elif hasKanji and hasKana:
                        print(exprs + ": has kanji and kana")
                    elif not hasKanji and hasKana:
                        print(exprs + ": just kana")
                    else:
                        print("no Japanese characters?")
                    
                else: print(exprs + "bracket detected")

except Exception as e:
    print("An exception has occurred;")
    print(e)
