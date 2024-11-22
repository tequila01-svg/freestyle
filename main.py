file=open('diamond.txt','r')
print(file.read())
file.close()


file_append=open('diamond.txt','a')
file_append.write("\n it is my first append class")
file_append.close()

file=open('diamond.txt','r')
print(file.readlines())
file.close()