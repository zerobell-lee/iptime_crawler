import requests
from bs4 import BeautifulSoup
import re
import sys

IPlist = []
MAClist = []

def getIP():
    global IPlist, MAClist
    session = requests.session()
    session.auth = ("id", "passwd")
    r = session.get("http://192.168.0.1/cgi-bin/timepro.cgi?tmenu=iframe&smenu=lan_pcinfo")
    soup = BeautifulSoup(r.text, "html.parser")
    tag = str(soup.find_all(class_="lansetup_main_span"))
    IPlist = re.findall(r'[0-9]+(?:\.[0-9]+){3}', tag)
    MAClist = re.findall(r'([\dA-F]{2}(?:[-:][\dA-F]{2}){5})', tag)

if __name__== "__main__":
    getIP()
    print(str(IPlist))
    print(str(MAClist))