#3.# CWE-326: Insecure Storage of Sensitive Information
# Vulnerable line: conn = sqlite3.connect('database.db')
# Description: The SQLite database is created without any encryption or protection, making it vulnerable to theft or unauthorized access.

import sqlite3
conn = sqlite3.connect('database.db')