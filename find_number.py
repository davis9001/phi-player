import os
from more_itertools import pairwise

def find_in_files(search_number, files):
    even = False
    between_buffer = ''
    for file in files:
        with open(file, "r") as f:
            contents = f.read()
            index = contents.find(search_number)
            
            search_size = len(search_number) + 1
            if even:
                between_buffer.extend(contents[:search_size])
            else:
                between_buffer = contents[-search_size:]

            print('between buffer: ' + between_buffer)
            if index != -1:
                return (file, index)
            else:
                if even:
                    if between_buffer.find(search_number) != -1:
                        return(file, 'middle')
                else:
                    even = False
                    between_buffer = ''
            if even:
                even = True
            else:
                even = False
    
    return None

def main():
    number_to_search = input("Enter the number to search for: ")
    directory = './phi'
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    result = find_in_files(number_to_search, files)
    if result is not None:
        print(f"Found '{number_to_search}' in or starting in file '{result}' at index {result[1]}.")
    else:
        print(f"Could not find '{number_to_search}' in any of the files.")

if __name__ == "__main__":
    main()

