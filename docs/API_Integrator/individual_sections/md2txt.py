import os

def convert_md_to_txt():
    # Get all files in the current directory
    for filename in os.listdir():
        # Check if the file is a markdown file
        if filename.endswith(('.md', '.markdown')):
            # Create the new filename with .txt extension
            new_filename = os.path.splitext(filename)[0] + '.txt'
            
            try:
                # Read the content of the markdown file
                with open(filename, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                
                # Write the content to a new txt file
                with open(new_filename, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(content)
                    
                print(f"Converted: '{filename}' → '{new_filename}'")
            except Exception as e:
                print(f"Error converting '{filename}': {e}")

if __name__ == "__main__":
    convert_md_to_txt()