# create a new file if it doesn't exist
#f= open("newfile.txt", "w")

#use write()  to write smth to the file and content will be overriden
# IF WE WANT TO write a few lines we need  write  write() - few times with new context
#f.write("Anna")


# or to do the same with writelines() -to write all lines at once
#lines =["Hello", "dear", "Anna"]
#f.writelines(lines)
# when we finish with file  - close()
#f.close()


# or best way to writw some lines - to use join()
#f= open("newfile.txt", "w")
#lines =["Hello", "dear", "Anna"]
#text = "\n".join(lines)
#f.writelines(text)
# when we finish with file  - close()
#f.close()




# challenge 1 Experiment with the "w+" access mode. Write some example code to understand how it works. 
# f =open ("challenge.txt", "w")
# f.write("ssssssssAA")
# f.write("fffffffffffBB")
# f.write("ArrrrrrAA")
# f.write("222222222222")
# f.seek(0)
# data= f.read()
# f.close()





# this is answer for a challenge
# with open('myfile.txt', 'w+') as f:

#     f.write('Hello, World\n')
#     f.write('Hello, World\n')
#     f.write('Hello, World\n')
#     f.tell()
#     f.seek(5)

#     data = f.read()
    
#     f.close()
f =open("data.txt", "r+")
f.write("xxxxx\n")
curentpost= f.tell()
print(curentpost)

f.seek(curentpost,1)
f.write('Line 6')
f.seek(0, 2)

f.write('\nLine 5')
f.close()