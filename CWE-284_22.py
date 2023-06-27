#3.# Example 3: CWE-284 - Improper Access Control

import shutil

src_file = "/path/to/file"
dst_dir = "/path/to/destination"
shutil.copy(src_file, dst_dir)

# The vulnerable line is line 3 where the code copies a file without checking if the user has permission to access it.