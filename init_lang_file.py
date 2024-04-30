### MKTranslate by rgzz666 ###
# MKTranslate can quickly initialize a json translation file. What you have to do is to write every single sentence into the sentences list below.

sentences=[\
"Here will be the sentences which you wished to be translated.",
"These sentences are stored in a list. Each item is a single sentence.",
"If you want to have a multi-line string translated, just break it with line separator.\nLike this!",
"It is recommended to write one single list item in each line to keep the code readable. Just like I did.",\
]


### Code Below ###

import json
import os

path=input("Enter file path to init: ")
path=path.replace('"',"")
print("")

if path=="":
    print("Seems you didn't enter anything... The script will generate the template translation file under its current working directory.")
    print("You might have to rename and move the file.by yourself.")
    path="./template.json"
elif not os.path.exists(path):
    print("The path you entered does not exist. The script will create the file at the path you entered.")
    print("You can also choose to create a template file under current working directory")
    if input("Create a new file at the path you entered? (Y/n) ").lower=="n":
        path="./template.json"

f=open(str(path),"r",encoding="utf-8")
curr_content=f.read()
f.close()
try:
    fcontent=json.loads(curr_content)
    print("The file already contains some translations. The script will append the rest.")
except:
    if curr_content.replace("\n","")!="":
        if input("The file contains some invalid contents. These contents must be removed from a translation file. Override them? (y/N) ").lower!="y":
            print("User canceled the remaining operations.")
            input("Press [ENTER] to exit... ")
            os._exit(1)
    fcontent={}

#fcontent={}
for s in sentences:
    if str(s) not in list(fcontent.keys()):
        print(list(fcontent.keys()))
        #print(s+" not in file")
        fcontent[str(s)]=""

content_str=json.dumps(fcontent,indent=0)

f=open(str(path),"w",encoding="utf-8")
f.write(content_str)
f.close()

print("")
print("All Set! Thank you for translating the software! ^_^")
input("Press [ENTER] to exit... ")
