#See README.md for details and assumptions
import csv
import regex as re

def main():
    OGFileData = []
    scan_source_file(OGFileData)
    process_words(OGFileData)
    write_to_file

def scan_source_file(list):
    try:         
        sourcefile = input("csv file: ")
        with open(sourcefile, encoding="utf8") as f:
            csv_f = csv.reader(f)

            for row in csv_f:
                if len(row) > 2: #if line isn't empty and has at least up to 'reading' field                 
                    if "[" not in row[1]: #assumes readings with brackets are already configured correctly
                        list.append(row)
                
    except Exception as e:
        print("An exception has occurred while scanning the source file:")
        print(e)

def remove_okurigana(word):    
    pass

def write_to_file(note):
    pass

def process_words(list):        
    try:
        for row in list:            
            scraped = bool
            exprs = row[0]
            reading = row[1]
            print("word: " + exprs)

            #check for scraped tag (see assumptions in README.md)
            if len(row) >= 6: 
                if "scraped" in row[5]:
                    scraped = True  

            #if no reading, reading should be expression
            if len(reading) == 0: 
                    print("reading empty: "+ reading)
                    reading = exprs
                    print("new reading: " + reading + "\n")
                    row[1] = reading
            else:               
                    hasKanji = re.search(r'\p{Han}', exprs)
                    hasKana = re.search(r'\p{Hiragana}|\p{Katakana}', exprs)

                    #word is just kanji
                    if hasKanji and not hasKana: 
                        print("just kanji\nreading: " + reading)
                        reading = exprs + "[" + reading + "]"
                        print("new reading: " + reading + "\n")
                    
                    #word is a mix of kanji and kana, any configuration
                    elif hasKanji and hasKana: 
                        print("has kanji and kana\nreading: " + reading + "\n")

                        #check for okurigana, which need to be removed from reading
                        if not scraped: 
                            remove_okurigana()

                        #put reading in     

                    #Just kana; in theory shouldn't ever get to this point?    
                    elif not hasKanji and hasKana: 
                        print("just kana; something isn't configured as expected.\nreading: " + reading + "\n")
                    
                    #No Jp characters; shouldn't get here either
                    else:
                        print("no Japanese characters?")

    except Exception as e:
        print("An Exception has occured while processing words:")
        print(e)                    
                    
if __name__ == "__main__":
    main()
#write to new csv file           


