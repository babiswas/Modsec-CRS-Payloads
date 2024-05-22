import paramiko
import logging
import datetime

logger=logging.getLogger()

def get_current_utc_time():
    return datetime.datetime.now(datetime.timezone.utc)

def ssh_zpa_connector(username:str,password:str,hostname:str,start_time_utc:str,end_time_utc:str):
    """Routine to get the zpa-connector logs"""
    try:
            ssh_client=paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=hostname,username=username,password=password)
            _,_,_=ssh_client.exec_command('sudo su')
            journalctl_command='journalctl -u zpa-connector --since '+f'"{start_time_utc}" '+"--until "+f'"{end_time_utc}"'
            _,stdout,_=ssh_client.exec_command(journalctl_command)
            return stdout
    except Exception as e:
        logger.error(e)

def process_streams(stdout,rule_list)->bool:
    test=True
    line=stdout.readline()
    temp_list=list()
    while len(line)!=0:
        for rule in rule_list:
            if rule in line:
                temp_list.append(rule)
        line=stdout.readline()
    print(temp_list)
    for rl in rule_list:
        if rl not in temp_list:
            test=False
            break
    return test

def process_streams_lines(stdout)->bool:
    test=True
    line=stdout.readline()
    temp_list=list()
    while len(line)!=0:
        print(line)
        line=stdout.readline()
    return
    






