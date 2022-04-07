#See README.md for details and assumptions
import csv
import regex as re

def main():
    OGFileData = []
    scan_source_file(OGFileData)
    process_words(OGFileData)
    write_to_file(OGFileData)

def scan_source_file(list):
    try:         
        sourcefile = input("csv file: ")
        with open(sourcefile, encoding="utf8") as f:
            csv_f = csv.reader(f)

            for row in csv_f:
                if len(row) > 2: #if line isn't empty and has at least up to 'reading' field                 
                    if "[" not in row[1]: #assumes readings with brackets are already configured correctly
                        wordType = get_word_type(row[0])
                        if wordType == "Just Kanji" or wordType == "Kanji and Kana" or wordType == "Just Kana":
                            list.append(row)
                
    except Exception as e:
        print("An exception has occurred while scanning the source file:")
        print(e)

def get_word_type(word):
    try:
        wordType = ""
        hasKanji = re.search(r'\p{Han}', word)
        hasKana = re.search(r'\p{Hiragana}|\p{Katakana}', word)

        #word is just kanji
        if hasKanji and not hasKana: 
            wordType = "Just Kanji"
        
        #word is a mix of kanji and kana, any configuration
        elif hasKanji and hasKana: 
            wordType = "Kanji and Kana"

        #Just kana    
        elif not hasKanji and hasKana: 
            wordType = "Just Kana"
        
        #No Jp characters; in theory, shouldn't ever get here
        else:
            wordType = "No Japanese characters"

        return wordType

    except Exception as e:
        print("An Exception has occurred while trying to assess the word type:")
        print(e)

def process_words(list):        
    try:
        for row in list:            
            scraped = False
            exprs = row[0]
            reading = row[1]
            wordType = get_word_type(exprs)
            print("word: " + exprs)

            #check for scraped tag (see assumptions in README.md)
            if len(row) >= 6: 
                if "scraped" in row[5]:
                    scraped = True                      

            if wordType == "Just Kanji":
                print("just kanji\nreading: " + reading)
                reading = exprs + "[" + reading + "]"
                print("new reading: " + reading + "\n")
                row[1] = reading
                
            elif wordType == "Kanji and Kana": 
                print("has kanji and kana\nreading: " + reading)

                #check for okurigana, which need to be removed from reading
                if not scraped: 
                    reading = remove_okurigana(exprs, reading)

                format_reading(exprs, reading)
                print("new reading: " + reading + "\n")
                row[1] = reading
    
            elif wordType == "Just Kana": 
                #if no reading, reading should be expression
                if len(reading) == 0: 
                        print("reading empty: "+ reading)
                        reading = exprs
                        print("new reading: " + reading + "\n")
                        row[1] = reading
                #should never get here but
                else:
                    if reading != exprs:
                        print("this word is just kana, but the expression and reading are different?? check README.md")
                    else:
                        print("reading matches expression\n")

    except Exception as e:
        print("An Exception has occurred while processing words:")
        print(e)                    
   
def remove_okurigana(expression, reading):    
    try:   
        r = reading
        hitKanji = False
        removeBack = []

        for char in expression:
            if not hitKanji:
                if not re.match(r'\p{Han}', char):
                    r = r.removeprefix(char)
                else:
                    hitKanji = True
            elif hitKanji:
                if not re.match(r'\p{Han}', char):
                    removeBack.append(char)

        i = len(removeBack) - 1
        while i >= 0:
            r = r.removesuffix(removeBack[i])
            i -= 1
        print("okurigana removed!")
        return r

    except Exception as e:
        print("An Exception has occurred while trying to remove okurigana:")
        print(e)

def format_reading(expression, reading):
    try:
        pass

    except Exception as e:
        print("An Exception has occurred while trying to format the correct furigana reading:")
        print(e)

def write_to_file(note):
    try:
        pass
    
    except Exception as e:
        print("An Exception has occurred while trying to write to the new file:")
        print(e)
                 
if __name__ == "__main__":
    main()
