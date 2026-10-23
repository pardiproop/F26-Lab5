# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 19/10/2026
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.
with open("rhyme.txt","w") as dataFile:
    dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")")
# TO DO 2: Open rhyme.txt file.
f=open('rhyme.txt','d')
line=f.readline()
while line!="":
    clean_line=line.strip().strip('.')
    words_line=clean_line.split()
    count=len(words_line)
    print(clean_line,'------',count,'words')
    line=f.readline()
f.close()
# TO DO 3: Print the output as directed in readme.md file.
