import os
import re
# os.popen("netstat > res_net.txt")

establishedRegex=re.compile(r"\s+(?P<proto>\w+)\s+(?P<iploc>([\w\-]+)?((\d{1,3}.){3}\d{1,3})?):(?P<portloc>\w+)\s+(?P<ipdst>([\w\-]+)?((\d{1,3}.){3}\d{1,3})?):(?P<portdst>\w+)\s+(ESTABLISHED)")

with open("res_net.txt") as f:
    lignes = f.readlines()

tabEstablished=[]

for ligne in lignes:
    if match:=establishedRegex.match(ligne):
        iploc=match.group("iploc")
        portloc=match.group("portloc")
        ipdst=match.group("ipdst")
        portdst=match.group("portdst")
        print("Adresse locale: "+iploc+":"+portloc+
              "\tAdresse distante: "+ipdst+":"+portdst)
        dictionnaire={"iploc":iploc,"portloc":portloc,"ipdst":ipdst,"portdst":portdst}
        tabEstablished.append(dictionnaire)
        
def jsonExport(tabEstablished):
    output="{"
    i=0
    for line in tabEstablished:
        output+='"%s":{"iploc":"%s","portloc":"%s","ipdst":"%s","portdst":"%s"},'%(i,line["iploc"],line["portloc"],line["ipdst"],line["portdst"])
        i+=1
    output=output[:-1]+"}"
    with open("res_net.json","w") as f:
        f.write(output)

jsonExport(tabEstablished)
    
    
def htmlExport(tabEstablished):
    output="<table><tr><th>Adresse ocale</th><th>Port local</th><th>Adresse distante</th><th>Port distant</th></tr>"
    for line in tabEstablished:
        output+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'%(line["iploc"],line["portloc"],line["ipdst"],line["portdst"])
    output+="</table>"
    with open("res_net.html","w") as f:
        f.write(output)
htmlExport(tabEstablished)