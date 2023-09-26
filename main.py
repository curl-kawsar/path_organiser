import os
import shutil

def organize_files(source_dir):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Others': []  
    }
    # Create folders for each file type if they don't already exist
    
    for folder in file_types.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    # Iterate files in the source directory
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isdir(file_path):
            continue
        
    # Get the file extension
    
        file_extension = os.path.splitext(filename)[1]
        target_folder = 'Others' # Default if the extension is not recognized
        for folder, extensions in file_types.items():
            if file_extension.lower() in extensions:
                target_folder = folder
                break
    # Move the file to the appropriate folder
    
        new_file_path = os.path.join(source_dir, target_folder, filename)
        shutil.move(file_path, new_file_path)
        print(f"Moved '{filename}' to '{target_folder}'")

if __name__ == "__main__":
    source_directory = input("Enter The Path: ") #Enter the path for Organise 

    if os.path.exists(source_directory):
        organize_files(source_directory)
        print("File organization completed.")
    else:
        print("Directory not found.")
