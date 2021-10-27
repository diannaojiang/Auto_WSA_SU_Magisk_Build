import requests
from bs4 import BeautifulSoup
import re
import zipfile
import os
import urllib.request
res = requests.post("https://store.rg-adguard.net/api/GetFiles", "type=CategoryId&url=858014f3-3934-4abe-8078-4aa193e74ca8&ring=WIS&lang=en-US", headers={
    "content-type": "application/x-www-form-urlencoded"
})
html = BeautifulSoup(res.content, "lxml")
a = html.find("a", string=re.compile("MicrosoftCorporationII\.WindowsSubsystemForAndroid_.*\.msixbundle"))
link = a["href"]
out_file = "wsa.zip"
arch = "${{ matrix.arch }}"
if not os.path.isfile(out_file):
    urllib.request.urlretrieve(link, out_file)
zip_name = ""
with zipfile.ZipFile(out_file) as zip:
    for f in zip.filelist:
        if arch in f.filename.lower():
            zip_name = f.filename
            if not os.path.isfile(zip_name):
                zip.extract(f)
            break
with zipfile.ZipFile(zip_name) as zip:
    if not os.path.isdir(arch):
        zip.extractall(arch)