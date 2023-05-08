import os

def find_number_spanning_files(search_number, files):
    search_len = len(search_number)
    search_between_file = []
    search_between_buffer = ''
    index = 0
    for file in files:
        if index > 1:
            index = 0
            search_between_buffer = ''
        if index > 0:
            found = search_between_buffer.find(search_number)
            if found != -1:
                return (file, found)
        search_between_file += file
        with open(file, "r") as f:
            file_start = file[0:search_len]
            file_end = file[-search_len:0]
            search_between_buffer += file_start + file_end
            index = index + 1

def find_in_files(search_number, files)
    for file in files:
        with open(file, "r") as f:
            contents = f.read()
            index = contents.find(search_number)
            if index != -1:
                return (file, index)
    return None

def main():
    number_to_search = input("Enter the number to search for: ")
    directory = './phi'
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    result = find_number_spanning_files(number_to_search, files)
    if result is not None:
        print(f"Found '{number_to_search}' in file '{result}' at index {result[1]}.")
    else:
        print(f"Could not find '{number_to_search}' in any of the files.")

if __name__ == "__main__":
    main()

