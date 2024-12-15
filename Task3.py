import os
import shutil

def organize_files_by_type(folder_path):
    try:
        organize_files(folder_path)
    except Exception as e:
        print(f"An error occurred: {e}")

def organize_files(folder_path):
    if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return

    file_iteration(extensions())
    print("File organization complete!")

def check_If_file_moved(folder_path,file_path, file, moved):
    if not moved:
        unknown_folder = os.path.join(folder_path, 'Others')
        os.makedirs(unknown_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(unknown_folder, file))
        print(f"Moved: {file} -> Others")

def file_existence(file_ext, file,folder_path, folder):
    if file_ext in extensions:
        destination_folder = os.path.join(folder_path, folder)
        os.makedirs(destination_folder, exist_ok=True)  
        shutil.move(file_path, os.path.join(destination_folder, file))
        print(f"Moved: {file} -> {folder}")
        moved = True
        return


def file_iteration(extensions_map):
    for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isdir(file_path):
                continue
            
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extensions in extensions_map.items():
                file_existence(file_ext, file,folder_path, folder)
                check_If_file_moved(folder_path,file_path)


def extensions():
    extensions_map = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
            'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
            'Music': ['.mp3', '.wav', '.aac'],
            'Archives': ['.zip', '.rar', '.tar', '.gz'],
        }
    return extensions_map


if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to organize: ").strip()
    organize_files_by_type(folder_path)

# test case, provide a folder url which has files that you want to be organized