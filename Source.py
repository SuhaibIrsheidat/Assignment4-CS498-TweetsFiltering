# ------------------------------ #
i = open("EI-oc-En-joy-train.txt", 'r', encoding="utf-8")
a = list() #Initialize a 2D-List
# ------------------------------ #
def filteringRowTweet(tweet):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    words = word_tokenize(tweet); new_r = [] #Tokenizing and new list
    stopWords = set(stopwords.words('english')) #Get english stopwords
    words=[word.lower() for word in words if word.isalpha()] #Remove punctuations
    for w in words: #Removing stopwords
        if (w not in stopWords) :
            new_r.append(w)
    # Stemming
    from nltk.stem import PorterStemmer
    ps = PorterStemmer().stem
    for y in new_r:
        y = ps(y)
    return ' '.join(new_r) #Returning final tweet
# ------------------------------ #
def main():
    for x in i: #This loop is to split the txt file into cells in 2D-List
        a.append(x.split('\t'))
    for row in a[1::]: 
        row[0] = list(row[0].split('-'))[-1] #Remove '2017-Eng-'
        row[1] = filteringRowTweet(row[1].lower()) #Remove stopwords and do other stuff
        del row[2] #Remove the column 'After dimension'
        row[2] = row[2][0] #Intensity class: keep only the numbers and remove the rest
    # -------------------------- #
    # Creating CSV file 
    import csv
    with open('tweets.csv', mode='w', encoding="utf-8") as newCSV:
        csv_writer = csv.writer(newCSV, delimiter=",")
        for row in a[1::]:
            csv_writer.writerow(row)
        newCSV.close()
    
    # -------------------------- #
    import pandas
    print(pandas.read_csv('tweets.csv', delimiter=',', names=['ID', 'Tweet', 'Intensity']))
# ------------------------------ #
if __name__ == '__main__':
    main()
# ------------------------------ #