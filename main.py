import chardet
import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
encoding = chardet.detect(results)['encoding']
results = results.decode(encoding)

with open("list_wifi.txt", "w") as f:
    f.write(results)