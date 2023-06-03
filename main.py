import argparse
import os.path
import sys

parser = argparse.ArgumentParser(description="CodeScribe - An Automate way to describe code")

parser.add_argument('-s', '--code_folder', type=str, help='Path to the code folder')

args = parser.parse_args()

# Check if the code folder path is provided
if not args.code_folder:
    parser.print_help()
    exit(1)

if len(sys.argv) < 2:
    print("Usage: python CodeScriber.py /code_folder")
    sys.exit(1)

code_folder = sys.argv[1]

# Check if the code folder path is valid
if not os.path.isdir(args.code_folder):
    print(f"Invalid code folder path: {args.code_folder}")
    exit(1)


file_list = os.listdir(args.code_folder)
code_files = {}


print("Files in the code folder:")

for i, file_name in enumerate(file_list, start=1):
    print(f"{i}. {file_name}")

    # Read the code from each file and store it in a variable
    # Check if the item in the code folder is a file
    file_path = os.path.join(args.code_folder, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            code = file.read()
            code_files[file_name] = code
    else:
        print(f"Skipping {file_name} as it is not a file.")

file_number = int(input("Enter the file number to display the code: "))
file_name = file_list[file_number - 1]
code = code_files[file_name]

print(f"\nCode for file {file_name}:\n")
print(code)