def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        modified_content = [line.upper() for line in content]
        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File '{input_filename}' read successfully.")
        print(f"Modified content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: An I/O error occurred while accessing '{input_filename}' or '{output_filename}'.")

input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the file to write the modified content: ")

read_and_modify_file(input_file, output_file)
