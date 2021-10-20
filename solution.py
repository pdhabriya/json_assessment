import json
import glob
import os
import sys

sys.dont_write_bytecode = True

young = []
old = []
json_str = "/people*json"

def age_filter(files):
    for file in glob.glob(files):
        with open(file, 'r') as json_file:
            json_text = json.load(json_file)
            for item in json_text:
                my_dict={}
                if not isinstance(item.get('age'), int): continue
                my_dict['name'] = item.get('name')
                my_dict['bestfriend'] = [( i['name']) for i in item['friends'] if i['id'] == 0 ]
                my_dict['age'] = item.get('age')
                my_dict['gender'] = item.get('gender')
                young.append(my_dict) if my_dict['age'] < 30 else old.append(my_dict)

    with open('old.json', 'w') as f:
        json.dump(old, f, indent=4, sort_keys=True)
    with open('young.json', 'w') as f:
        json.dump(young, f, indent=4, sort_keys=True)

def main():
    age_filter(os.getcwd() + json_str)

if __name__ == "__main__":
    main()
