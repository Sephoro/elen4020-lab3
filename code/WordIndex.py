import mrs
import string

class WordIndex(mrs.MapReduce):

    def map(self,line_num,line_text):
        
        stopWords = open('stopWords.txt','r').read().split()
        
        #Extra punctuation
        morePunct = ['--', '...', '\'']

        for word in line_text.split():
            
            # Check for the extra English Punctuation
            if any(punct in word for punct in morePunct):
                
		#Remove the extra English Punctuation
                for punct in morePunct:
                    word = word.replace(punct,' ')

                word = word.split()

                for w in word:
                    w = w.strip(string.punctuation).lower()
                    if w and w not in stopWords and not w[0].isdigit():
                            yield (w,line_num + 1) #Start counting at 1

            else:
                word = word.strip(string.punctuation).lower()
                if word and word not in stopWords and not word[0].isdigit():
                    yield (word,line_num + 1) #Start counting at 1

    def reduce(self,word,line_num):
        
        lineNumbers = []
        for i in line_num:
            
            #At most 50 lines
            if len(lineNumbers) >= 50:
                break
            #If a word repeats on a line, write the line only once
            if i not in lineNumbers:
                lineNumbers.append(i)
                
        yield lineNumbers
        


if __name__ == '__main__':
    mrs.main(WordIndex)
