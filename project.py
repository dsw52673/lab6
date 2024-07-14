import json
import xmltodict
import yaml
import sys
import os

def json_to_xml(json_obj):
    return xmltodict.unparse(json_obj, pretty=True)

def xml_to_json(xml_str):
    return json.loads(json.dumps(xmltodict.parse(xml_str)))

def yaml_to_json(yaml_str):
    return yaml.safe_load(yaml_str)

def json_to_yaml(json_obj):
    return yaml.dump(json_obj, default_flow_style=False)

def convert_file(input_file, output_file):
    input_type = os.path.splitext(input_file)[1].lower()
    output_type = os.path.splitext(output_file)[1].lower()

    with open(input_file, 'r') as f:
        input_data = f.read()

    if input_type == '.json':
        data = json.loads(input_data)
    elif input_type in ['.xml']:
        data = xml_to_json(input_data)
    elif input_type in ['.yml', '.yaml']:
        data = yaml_to_json(input_data)
    else:
        raise ValueError(f"Unsupported input file type: {input_type}")

    if output_type == '.json':
        output_data = json.dumps(data, indent=4)
    elif output_type in ['.xml']:
        output_data = json_to_xml(data)
    elif output_type in ['.yml', '.yaml']:
        output_data = json_to_yaml(data)
    else:
        raise ValueError(f"Unsupported output file type: {output_type}")

    with open(output_file, 'w') as f:
        f.write(output_data)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_file(input_file, output_file)