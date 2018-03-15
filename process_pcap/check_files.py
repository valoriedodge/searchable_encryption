import subprocess
import urllib.request
import gzip

p = subprocess.Popen(["sudo src/snort -r pcaps/filtered_2 -c etc/snort/snort.conf "], stdout=subprocess.PIPE)

p = subprocess.Popen(["sudo src/snort -r pcaps/filtered_2 -c etc/snort/snort.conf "], stdout=subprocess.PIPE)
out = p.stdout.read()
print(out)

alert tcp any any -> any $HTTP_PORTS (msg:"Example"; sid:1234; rev:1;)
alert tcp any any -> any $HTTP_PORTS (msg:"Example"; sid:1234; rev:1;)
