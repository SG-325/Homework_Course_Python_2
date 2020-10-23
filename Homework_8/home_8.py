import json
import yaml


#Task_1
with open("py_json.json", "r") as f:
    value_json = json.load(f)


with open("json_to_text.txt", "w") as f_text:
    f_text.write(str(value_json))



#Task_2
with open("json_to_yaml.yaml", "w") as f_yaml:
    yaml.dump(value_json, f_yaml)


#Task_3
with open("json_to_yaml.yaml", "r") as f_yaml_1:
    yaml_value = yaml.load(f_yaml_1, Loader = yaml.FullLoader)


with open("yaml_to_json.json", "w") as f_json:
    json.dump(yaml_value, f_json, sort_keys = True, indent = 2)


#Task_4
with open("yaml_to_text.txt", "w") as f_text_1:
    f_text_1.write(str(yaml_value))



print("\nThe program works.")