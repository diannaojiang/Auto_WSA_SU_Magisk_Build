import urllib.request
import zipfile
import os
magisk_apk = """${{ github.event.inputs.magisk_apk }}"""
if not magisk_apk:
    magisk_apk = """https://raw.githubusercontent.com/LSPosed/MagiskOnWSA/main/magisk.apk"""
out_file = "magisk.zip"
arch = "${{ matrix.arch }}"
abi_map={"x64" : ["x86_64", "x86"], "arm64" : ["arm64-v8a", "armeabi-v7a"]}
if not os.path.isfile(out_file):
    urllib.request.urlretrieve(magisk_apk, out_file)
def extract_as(zip, name, as_name, dir):
    info = zip.getinfo(name)
    info.filename = as_name
    zip.extract(info, dir)
with zipfile.ZipFile(out_file) as zip:
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagisk64.so", "magisk64", "magisk")
    extract_as(zip, f"lib/{ abi_map[arch][1] }/libmagisk32.so", "magisk32", "magisk")
    extract_as(zip, f"lib/{ abi_map[arch][0] }/libmagiskinit.so", "magiskinit", "magisk")
    extract_as(zip, f"lib/{ abi_map['x64'][0] }/libmagiskinit.so", "magiskpolicy", "magisk")