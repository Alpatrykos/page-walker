import json
import re


def remove_whitespace(text):
    return re.sub('[\s]+', ' ', text)


def print_json(json_object):
    print(json.dumps(json_object, indent=2, sort_keys=True))


def save_json_to_file(json_object, file_name):
    with open("%s.json" % file_name, "w") as f:
        f.write(json.dumps(json_object, indent=2, sort_keys=True))


def camelcase_to_underscore(text):
    text = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    text = re.sub('([a-z0-9])([A-Z])', r'\1_\2', text)
    return text.lower()
