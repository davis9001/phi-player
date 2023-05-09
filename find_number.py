import os
from more_itertools import pairwise

# def find_in_files(search_number, files):
#     for (a, b) in pairwise(files):
#         with open(a, "r") as f1:
#             with open(b, "r") as f2:
#                 contents = f1.read()
#                 beg = f2.read(len(search_number) - 1)

#                 index = contents.find(contents + beg)
#                 if index != -1:
#                     if index - len(contents) > len(search_number):
#                         print("input is straddling files")

#                     return (a, index)
#     return None


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
      search_between_file = search_between_file + file
      with open(file, "r") as f:
        file_start = file[0:search_len]
        file_end = file[-search_len:0]
        search_between_buffer += file_start + file_end
        index = index + 1

def find_in_files(search_number, files):
    even = False
    between_buffer = ''
    for file in files:
        with open(file, "r") as f:
            contents = f.read()
            index = contents.find(search_number)
            
            search_size = len(search_number) + 1
            if even:
                between_buffer = between_buffer + contents[:search_size]
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
        print(f"Found '{number_to_search}' in file '{result}' at index {result[1]}.")
    else:
        print(f"Could not find '{number_to_search}' in any of the files.")

if __name__ == "__main__":
    main()

