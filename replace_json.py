import json

# Load the JSON file
with open(r"C:\Users\Pratham.Malhotra\Downloads\arm_template1\ARMTemplateForFactory.json", 'r') as file:
    data = json.load(file)

# Replace the value
data['parameters']['factoryName']['defaultValue']= 'newValue'

# Save the modified JSON file
with open(r"C:\Users\Pratham.Malhotra\Downloads\arm_template1\ARMTemplateForFactory.json", 'w') as file:
    json.dump(data, file, indent=4)


# import json

# # Load the JSON file
# with open(r"C:\Users\Pratham.Malhotra\Downloads\arm_template1\ARMTemplateForFactory.json", 'r') as file:
#     data = json.load(file)

# # Print the structure of the 'parameters' key
# print(json.dumps(data["parameters"], indent=4))

# # Replace the value (assuming the structure is correct)
# data["parameters"]['defaultValue']['factoryName'] = 'newValue'

# # Save the modified JSON file
# with open(r"C:\Users\Pratham.Malhotra\Downloads\arm_template1\ARMTemplateForFactory.json", 'r') as file:
#     json.dump(data, file, indent=4)

