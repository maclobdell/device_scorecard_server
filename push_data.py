#!/usr/bin/env python
import requests 
import pprint
import json

def main():
   
    debug_print = 0
    
    if debug_print == 1:
        pp = pprint.PrettyPrinter(indent=4)

    r = requests.get('http://localhost:5000/target_data/api/v1.0/targets')
    if debug_print == 1:
        pp.pprint(r.json())

    f = open("target_data_new_target.json", "r")
    t = json.loads(f.read())
    if debug_print == 1:
        pp.pprint(t)

    r = requests.post('http://localhost:5000/target_data/api/v1.0/targets', json = t)
    if debug_print == 1:
        pp.pprint(r.json())

    f = open("target_data_test_record.json", "r")
    t = json.loads(f.read())
    if debug_print == 1:
        pp.pprint(t)

    r = requests.put('http://localhost:5000/target_data/api/v1.0/targets/1', json = t)
    if debug_print == 1:
        pp.pprint(r.json())

    r = requests.get('http://localhost:5000/target_data/api/v1.0/targets')
    if debug_print == 1:
        pp.pprint(r.json())

if __name__ == '__main__':
    main()


          
          
