import mrs
import string


class WordCount(mrs.MapReduce):

    #MAP
    def map(self, line_num, line_text):
        StopWords = ["for", "as", "the" ,"is", "at", "which", "to","or","it","had", ""]
        b = open('stopWords.txt','r').read().split()

        open('SortedWords.txt', 'w').close()
        open('top10_.txt', 'w').close()
        open('top20_.txt', 'w').close()
        
        for word in line_text.split():
            word = word.strip(string.punctuation).lower()
            #dont forget to remove numbers

            if word not in StopWords and not word.isdigit():
                yield (word, 1)

    #REDUCE
    def reduce(self,word, counts):  
        self.SortInDesc(word, sum(counts))
        yield sum(counts)

    #SORT IN ORDER
    def SortInDesc(self,word, counts):

        words = open("SortedWords.txt", "a+")
        words.write(word + " " + str(counts) + "\n")
        words.close()

        with open("SortedWords.txt") as textFile:
            lines = [line.split() for line in textFile]
            lines.sort(key = lambda x: x[1], reverse=True)
           
        self.TopKQuery(lines)
   
        words.close()


    #WRITES TO FILE
    def TopKQuery(self, lines):

        top10 = open("top10_.txt", "w")
        top20 = open("top20_.txt", "w")
        num = 0

        for i in lines:

            if num <20:   
                if num <10:
                    top10.write(i[0] +" "+ i[1] + "\n")

                    
                top20.write(i[0] +" "+ i[1] + "\n")
                num = num+1

        
        top10.close() 
        top20.close()

    
if __name__ == '__main__':
    mrs.main(WordCount)
   


    
