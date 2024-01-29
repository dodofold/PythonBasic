from sys import argv #import argv from sys

script, filename = argv #unpack argv from script and filename

txt = open(filename) #Open the file

print(f"Here's your file {filename}:") #print a string with formated argv filename
print(txt.read()) #read the file
txt.close() #close the file

print("Type the file name again:") #print a string to ask user for filename
file_again = input("> ") #ask user for filename

txt_again = open(file_again) #open the file again

print(txt_again.read()) #read the file again from variable txt_again

txt_again.close() #close the file