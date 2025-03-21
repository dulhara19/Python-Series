f=open("C:\\AI-projects\\new.txt","r+")

#if i want to append text to the file then use "a" instead of "w"
#f=open("C:\\AI-projects\\new.txt","a")

#write() method is used to write the content to the file
# f.write("Hello world my name is Dulhara\n and currently im learning ML and AI\nso you can collaborate with me to learn more about AI and ML\n")    

#f.flush() 

#Why Use flush()?

#By default, Python buffers file operations for performance reasons. This means data is not immediately written to the file but is temporarily stored in memory before being written in chunks.



for line in f:
    tokens = line.split()
    print(tokens)
    
#close the file
f.close() 