import sys
import os
import json
o = os.getcwd()
o = o.replace("packages","")

with open(o+"/config.json","r") as j:
	j = json.load(j)

						
j["app_style"] = "background-color: #333333"
j["navbar_style"] = "background-color: #35363a; color: white"
j["body_background-color"] = "#222222"
j["body_color"] = "white"


with open(o+"/config.json","w") as f:
	json.dump(j, f)

