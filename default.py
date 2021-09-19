import sys
import os
import json
o = os.getcwd()
o = o.replace("packages","")
a = json.loads("""

{							
	"app_style": "background-color: #333333",
	"navbar_style": "background-color: #35363a; color: white"
}
""")
#self.js_btn = QAction("js", self)
#self.js_btn.triggered.connect(lambda: self.browser.page().runJavaScript('document.body.style.color = "white"; document.body.style.color = "yellow"; document.body.style.backgroundColor = "red";'))
#self.navbar.addAction(self.js_btn)
with open(o+"/config.json","w") as f:
	json.dump(a, f)

