#This program was developed by Samip on 9/11/2017 and uses CLI.
from sys import argv
script,username,password=argv
input_file=open("PassCrypt Demo.txt",'a')
input_file.write("\n")
input_file.write("Username:")
input_file.write(username)
input_file.write("  ")
input_file.write("Password:")
input_file.write(password)

print "Password Writing Success"
print "These are your available username and passwords : \n"
input_file=open("PassCrypt Demo.txt",'r')
print input_file.read()
input_file.close()
