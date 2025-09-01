import json 
import requests
import sys 


if len(sys.argv) != 2  :
    sys.exist()
    
response = requests.get("http://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"])


