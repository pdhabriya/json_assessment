import json
import jsonschema
from jsonschema import validate
import os
import sys
import solution

jsonSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "bestfriend": {"type": "string"},
        "gender": {"type": "string"}
    },
}

class TestAgefilter:

    def __init__(self):
        pass

    def get_test_data(self, filename):
        with open(os.getcwd() + filename, 'r') as data_file:
            json_data = json.load(data_file)
        return json_data

    def test_old_json_output(self):
        json_str = "/old.json"
        data = self.get_test_data(json_str)
        list1 = [item.get('age') for item in data]
        for ele in list1:
            try:
                assert ele >= 30, "Assertion failed, age is less than 30 in old.json"
            except AssertionError as msg:
                print(msg)
                sys.exit(1)
        print("Assertion passed")

    def validateJson(self, json_data):
        try:
            validate(instance=json_data, schema=jsonSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def test_json_isvalid(self):
        json_str = "/old.json"
        data = self.get_test_data(json_str)
        isValid = validateJson(data)
        if isValid:
            print("Given JSON data is Valid")
        else:
            print("Given JSON data is InValid")

##Run the solution
solution.main()

##Run the test cases
t1 = TestAgefilter()
t1.test_old_json_output()
t1.test_json_isvalid()