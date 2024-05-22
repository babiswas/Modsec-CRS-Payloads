from owasp_rule_map import owasp_rule_map
from connector_log import process_streams,ssh_zpa_connector,get_current_utc_time
import os
import time
import subprocess

if __name__=="__main__":
    myrule=set()
    username=""
    hostname=""
    password=""
    for file,rule_string in owasp_rule_map.items():
        rule_list=rule_string.split(',')
        utc1=str(get_current_utc_time()).split('.')[0]
        subprocess.call(['sh','./'+file])
        time.sleep(2)
        utc2=str(get_current_utc_time()).split('.')[0]
        stdout=ssh_zpa_connector(username,password,hostname,utc1,utc2)
        test=process_streams(stdout,rule_list)
        print(test,file,rule_string)
        for rl in rule_list:
            myrule.add(rl)
        fl=open("allrule.txt",'a')
    for r in list(myrule):
            fl.write(r+"\n")





