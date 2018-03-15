import subprocess
max_file = 2000
url = "https://ictf.cs.ucsb.edu/archive/2011/traffic/ictf2011-1322841389-"
for i in range(0, max_file):
	f = str(i) 
	file_name = url + "0"*(4-len(f)) + f + ".gz"
	p = subprocess.run("wget " + file_name + " -O traffic_file.gz", shell=True)
	p = subprocess.run("gunzip traffic_file.gz", shell=True)
	p = subprocess.run("tcpdump -r traffic_file -w file_edited port http", shell=True)
	p = subprocess.run("sudo src/snort -r file_edited -c etc/snort/snort.conf", shell=True)
	p = subprocess.run("wc -l /var/log/snort/alert >> found.txt", shell=True)
	p = subprocess.run("rm traffic_file", shell=True)







# alert tcp any any -> any $HTTP_PORTS (msg:"Example"; sid:1234; rev:1;)
