import urllib.request as request
import json
from json2html import *
import random
# ip="24.48.0.100"

# ips=["24.48.0.100","51.159.196.139","8.8.8.8","1.1.1.1"]
ips=[]
def generateIP():
    ip=""
    for i in range(0,4):
        ip+=str(random.randint(0,256))+"."
    ip=ip[:-1]
    return ip

for j in range(0,5):
    ips.append(generateIP())
print(ips)
result=[]
for ip in ips:
    data=json.load(request.urlopen("http://ip-api.com/json/"+ip))
    if data["status"]=="success":
        result.append((ip,data["country"],data["regionName"],data["city"]))

col=["IP","Pays","Region","Ville"]

    
def htmlExport(result,col):
    output="<table><tr>"
    for co in col:
        output+="<th>%s</th>"%co
    output+="</tr>"
    for line in result:
        output+='<tr>'
        for cell in line:
            output+="<td>%s</td>"%cell
        output+="</tr>"
    output+="</table>"
    with open("res_geo.html","w") as f:
        f.write(output)
        
htmlExport(result,col)


result={"GeoIP":[]}
for ip in ips:
    data=json.loads(request.urlopen("http://ip-api.com/json/"+ip).read())
    if data["status"]=="success":
        result["GeoIP"].append({"IP":ip,"Pays":data["country"],
                                "Region":data["regionName"],"Ville":data["city"]})
htmlCode=json2html.convert(result)
with open("res_geo_auto.html","w") as f:
        f.write(htmlCode)
        
