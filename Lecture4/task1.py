text = input("")
modified_string = ""
for char in text:
    if char == "'":
        modified_string += '"'
    elif char == '"':
        modified_string += "'"
    else:
        modified_string += char

print(modified_string)
