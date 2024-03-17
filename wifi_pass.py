import subprocess
import re
import time

#-------------------------------------_CAPTURE_OUTPUT_--------------------------------------#

find_key = ''

o1 = subprocess.run(['netsh','wlan','show','profile'],capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", o1))

#-------------------------------------_FIND_WIFI_NAMES_--------------------------------------#

for name in profile_names:
    o2 = subprocess.run(['netsh','wlan','show','profile',name],capture_output=True).stdout.decode()

    find_key = re.findall("Security key           : Present",o2)

#-------------------------------------_FIND_WIFI_KEYS_--------------------------------------#

if find_key != '':
    for name in profile_names:
        o3 = subprocess.run(['netsh','wlan','show','profile',name,'key=clear'],capture_output=True).stdout.decode()

        password = (re.findall("Key Content            : (.*)\r",o3))

# ---------------------------------_PRINT_WIFI_SSID+PASSWORD_--------------------------------------#

        if password == '':
            pass
        else:
            print(name,password)

time.sleep(10)
print("Closing...")





