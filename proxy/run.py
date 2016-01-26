import subprocess
import os

os.chdir('/var/www/sqlmap/')
subprocess.Popen('python sqlmapapi.py -s',shell=True)
subprocess.Popen('python /var/www/html/proxy/proxy_io.py 8888 &',shell=True)
subprocess.Popen('python /var/www/html/proxy/task.py &',shell=True)


https://github.com/mitmproxy/mitmproxy/tree/master/examples