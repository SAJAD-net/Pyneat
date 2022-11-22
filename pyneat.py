import os
import sys
from pathlib import Path
import time

# A dictionary of most popular file types
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
  
}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def organize_junk(dest_path):
    # Attempts to change the current directory to the "dest_path" directory
    try:
        os.chdir(dest_path) 
    except Exception as e:
        print(e)
        sys.exit()

    # Checks the files in the 'dest_path' directory and organizes them into different directories   
    for entry in os.scandir():
        if entry.is_dir(): # Ignores the directories
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
  
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass
        
if __name__ == "__main__":
    # Checks the user arguments for dest_path
    if dest_path:=sys.argv[1]:
        # Calculates the total process time
        start_time = time.time()
        organize_junk(dest_path)
        total_time = (time.time() - start_time)
        print(f"- status : successfully done, total time : {total_time:.0}s")