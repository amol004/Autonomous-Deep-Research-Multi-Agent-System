
from tools import read_text_file,write_text_file

import os

# Build absolute path to notes.txt
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Day05(Document_reading)", "Data"))
notes_path = os.path.join(base_dir, "notes.txt")
print(read_text_file(notes_path))

#write_text_file(notes_path, "Hello, this is the new content! \n")
print(read_text_file(notes_path))
