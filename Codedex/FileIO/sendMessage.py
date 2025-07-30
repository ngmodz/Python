send_msg = "Hello Nishu,How are you?"

with open ('send_msg.txt','w') as file:
    file.write(send_msg)
    
    
file.close()

# Modify the message to simulate unsending
unsent_message = 'This message has been unsent.'

# Truncating a file
with open('unsent_message.txt', 'r+') as file:
  file.write(unsent_message)
  file.truncate(20)  # Limit the file size to 20 bytes
  file.seek(0)    # moving the cursor to beginning 
  
  file.close()
  
  
with open ('unsent_message.txt','r+') as file:    # r+ in the open() function is used to indicate both reading and writing are allowed in the file.
    content = file.read()
    print(content)
    
    
file.close()