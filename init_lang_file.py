### MKTranslate by rgzz666 ###
# MKTranslate can quickly initialize a json translation file. What you have to do is to write every single sentence into the sentences list below.

sentences=[\
"Error",
"Config file not found!\nPick a config file after closing this dialog.\nIf you don't have a config file, please download a config file template from the internet, then move it to the working directory.",
"Choose a Config File",
"You didn't choose any file. The program will end after closing this dialog.",
"Enter API Key",
"Depending on the configuration settings, you have to obtain and specify the API key yourself",
"No Value Entered",
"You have not entered any value, Demo mode will be enabled as there is no API key available.",
"City List",
"Add City",
"Add",
"Warning",
"Invalid translation file! Will use English."]


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
