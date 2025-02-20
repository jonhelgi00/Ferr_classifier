import os

def add_prefix_to_files(folder_path, prefix="google"):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Create the full file path
        file_path = os.path.join(folder_path, filename)

        # Skip directories, only process files
        if os.path.isfile(file_path):
            # Split the filename and extension
            name, ext = os.path.splitext(filename)

            # Create the new filename with the prefix
            new_filename = f"{prefix}_{name}{ext}"
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Example usage
folder_path = "/Users/jonhelgi/Projects/Ferr_classifier/data/dataset/raw_img/combined/google/lewis_structure_diagram"  # Replace with your folder path
add_prefix_to_files(folder_path)
