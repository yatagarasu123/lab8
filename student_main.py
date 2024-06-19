import json
def task1(file_path, age):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above = [entry['name'] for entry in data if entry['age'] > age]
    return names_above

def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def task3(schema, file_path):
    inv_files = []
    for file_path in file_path:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                pass
            except json.JSONDecodeError:
                inv_files.append(file_path)
    return inv_files


def task4(file_path, key):
    def extract_values(obj, key):
        value = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    value.append(v)
                elif isinstance(v, (dict, list)):
                    value.extend(extract_values(v, key))
        elif isinstance(obj, list):
            for item in obj:
                value.extend(extract_values(item, key))
        return value

    with open(file_path, 'r') as file:
        data = json.load(file)
    value = extract_values(data, key)
    return value


def task5(file_path, category, update_function):
    with open(file_path, 'r+') as file:
        data = json.load(file)
        for item in data:
            if item.get('category') == category:
                update_function(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def increase_price(item):
    item['price'] += 10


