import os
import re


listOfFile = os.listdir(".")


for i in listOfFile:
    if (re.match("\w+[.]css", i)):
        newFilarray = re.split("[.]", i)
        os.rename(i, newFilarray[0] + ".module.css")
