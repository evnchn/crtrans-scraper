import json
with open("all_crtrans.json") as f:
    all_crtrans = json.load(f)
from pprint import pprint

import os

os.system("cls")
print("---ALL ISD---")
for k, crtran in all_crtrans.items():
    hkust_code = crtran["HKUST"]["CODE"]
    if hkust_code.startswith("ISDN"):
        print(k)
        pprint(crtran)
input()
os.system("cls")
print("---Design Electives---")      
for k, crtran in all_crtrans.items():
    hkust_code = crtran["HKUST"]["CODE"]
    if hkust_code in "ENGG1300#IEDA2150#IEDA4650#ISDN2000#ISDN2500#ISDN3100#ISDN3200#ISDN3300#ISDN4300#ISDN4320".split("#"):
        print(k)
        pprint(crtran)
input()
os.system("cls")
print("---Product Management Electives ---")      
for k, crtran in all_crtrans.items():
    hkust_code = crtran["HKUST"]["CODE"]
    if hkust_code in "ENTR3100#FINA2203#ISDN3350#ISDN3360#ISDN4200#ISOM1380#ISOM2030#ISOM2700#ISOM4020#MARK2120".split("#"):
        print(k)
        pprint(crtran)