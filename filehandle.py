f=open("C:\\AI-projects\\new.txt","r+")
fnew=open("C:\\AI-projects\\new1.txt","w+")

#read() method is used to read the content of the file
#if i want to append text to the file then use "a" instead of "w"
#f=open("C:\\AI-projects\\new.txt","a")

#write() method is used to write the content to the file
# f.write("Hello world my name is Dulhara\n and currently im learning ML and AI\nso you can collaborate with me to learn more about AI and ML\n")    

#f.flush() 

#Why Use flush()?

#By default, Python buffers file operations for performance reasons. This means data is not immediately written to the file but is temporarily stored in memory before being written in chunks.



for line in f:
    #tokens = line.split('o') #split the line by letter 'o'
    tokens = line.split(' ') #split the line by space
    #print(tokens)
    #print(len(tokens)) #print the length of the tokens
    #print(tokens[0]) #print the first token

    fnew.write(line + " word count :" + str(len(tokens)) + "\n") #write the line to the file

#close the file
f.close() 
fnew.close()