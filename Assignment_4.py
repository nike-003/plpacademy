# Read original file and write uppercase version to a new file
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (example: convert to uppercase)
modified_content = content.upper()

# Write to new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File processed and saved as 'output.txt'")


#2. Error Handling Lab 
filename = input("Enter filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' could not be read.")

