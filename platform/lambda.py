# def lambda_handler(event, context):
import json

def get_keypair_from_json(json_file, item):
    with open(json_file) as file:
        data = json.load(file)
        return get_keypair_recursive(data, item)

def get_keypair_recursive(data, item):
    results = []  # Store matching key-value pairs

    if isinstance(data, dict):
        for key, value in data.items():
            if key == item:
                results.append((key, value))
            if isinstance(value, (dict, list)):
                results.extend(get_keypair_recursive(value, item))
    elif isinstance(data, list):
        for item_value in data:
            results.extend(get_keypair_recursive(item_value, item))
    return results

def create_keypair_dictionary(results):
    keypair_dict = {}
    for key, value in results:
        if key in keypair_dict:
            keypair_dict[key].append(value)
        else:
            keypair_dict[key] = [value]
    return keypair_dict

# Example usage
json_file_path = "C:/Users/maham/OneDrive/Desktop/cfn (1)/cfn/ct_event.json"
item_to_find = "tags"

# Find key-value pairs in JSON
results = get_keypair_from_json(json_file_path, item_to_find)

# Create dictionary from results
keypair_dict = create_keypair_dictionary(results)

# Print the dictionary
if keypair_dict:
    print("Key-Value Dictionary:")
    print(json.dumps(keypair_dict, indent=4))
else:
    print("Item not found in the JSON.")


# # Example usage
# json_file_path = "C:/Users/maham/OneDrive/Desktop/cfn (1)/cfn/ct_event.json"
# item_to_find = "tags"

# # Find key-value pairs in JSON
# results = get_keypair_from_json(json_file_path, item_to_find)

# # Print the results
# if results:
#     print(f"Found {len(results)} occurrences of '{item_to_find}' in the JSON:")
#     for i, (key, value) in enumerate(results, start=1):
#         print(f"\nMatch {i}:")
#         print("Key:", key)
#         print("Value:")
#         print(json.dumps(value, indent=4))
# else:
#     print("Item not found in the JSON.")
