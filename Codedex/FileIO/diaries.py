# import fileIO

file = open('diaries.txt','a')          # opening the file in adding lines to the end
file.write("Heyy Nishant!!\n")
file.write("How are you??\n")

# lines = ['This is first line\n','This is second line\n']
# file.writelines(lines)          # writelines is used to write multiple lines

# file = open('diaries.txt','r')          # opening the file in reading mode

# content = file.read()           # reading a file
# print(content)


# content2 = file.readlines()
# print(content2,end = '')


# file.close()            # close a file and free up resources

with open('diaries.txt', 'r') as file:      # use a with block to open a file, handle it, and close it automatically
    content = file.read()           
    print(content)
    