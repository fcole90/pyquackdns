#!/usr/bin/env python3

import json
import requests
import sys
import time

DUCK_DNS_URL = 'https://www.duckdns.org/update'

#APIs at https://www.duckdns.org/spec.jsp
'''
HTTP Parameters
---------------

domains - REQUIRED - comma separated list of the subnames you want to update
token - REQUIRED - your account token
ip - OPTIONAL - if left blank we detect IPv4 addresses, if you want you can supply a valid IPv4 or IPv6 address
ipv6 - OPTIONAL - a valid IPv6 address, if you specify this then the autodetection for ip is not used
verbose - OPTIONAL - if set to true, you get information back about how the request went
clear - OPTIONAL - if set to true, the update will ignore all ip's and clear both your records
'''

def main():
    
    default_config_file_name = "config_parameters.json"
    if len(sys.argv) < 2 or len(sys.argv) > 3 :
        print_usage_error()
    else:
        # Check configuration parameter
        if len(sys.argv) > 2:
            config_file_name = sys.argv[2]
        else:
            config_file_name = default_config_file_name
            print("Using default parameter file: " + default_config_file_name)
        
        # Options
        if sys.argv[1] == 'configure':            
            configure(config_file_name)
        elif sys.argv[1] == 'start':
            start(config_file_name)
        else:
            print_usage_error()
       
       

def print_usage_error():
    print("Quack: Keeps your DuckDNS IP information updated.\n"
          "Usage:\n"
          "\tstart [CONF_FILE]\t- start the service\n"
          "\tstop\t\t\t- stop the service\n"
          "\trestart\t\t\t- restart the service\n"
          "\tconfigure [CONF_FILE]\t- set up your account details\n"
          "\t-h --help\t\t- print this help message")


def configure(config_file_name):
    params = {}
    
    domain = input("Please, insert your domain name:\n>>> ")
    token = input("Please, insert your token:\n>>> ")
    
    params = {
        'domains': domain,
        'token': token,
        'verbose': 'true'
    }
    
    with open(config_file_name, 'w') as config_file:
        json.dump(params, config_file)
    
    print("Saved, now you can start the service.")


def start(config_file_name):    
    with open(config_file_name, 'r') as config_file:
        params = json.load(config_file)
    
    while True:
        try:
            r = requests.get(DUCK_DNS_URL,
                             params=params, 
                             verify=False)
            print(r.text)
            time.sleep(10)
        except:
            e = sys.exc_info()[0]
            print('Error: ' + str(e) + str())
            time.sleep(10)


if __name__ == '__main__':
    main()
