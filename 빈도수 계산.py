file = open('Txt_example.txt', "r")
 
text = file.read() 
 
wordList = text.split()
 
wordCount = {} 
 
for word in wordList:
 
    # Get 명령어를 통해, Dictionary에 Key가 없으면 0리턴
 
    wordCount[word] = wordCount.get(word, 0) + 1 
    
    keys = sorted(wordCount.keys())
 
for word in keys:
 
    print(word + ':' + str(wordCount[word])) 
