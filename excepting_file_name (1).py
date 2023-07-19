

def get_file_extension(filename):
    # Find the last occurrence of the dot symbol
    dot_index = filename.rfind(".")

    # Check if a dot is found and extract the extension
    if dot_index != -1:
        extension = filename[dot_index + 1:]
        return extension.lower()
    else:
        return None

filename = input("filename (with extension): ")


file_extension = get_file_extension(filename)

# Check if the file extension is found
if file_extension:
    print("The extension of the file is:", file_extension)
else:
    print("No file extension found.")