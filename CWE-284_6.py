#7.# CWE-284: Improper Access Control
# Vulnerable line: if user_id in request.form['user_ids']:
# Description: This code does not properly check if the user is authorized to access the requested user's data.
if user_id in request.form['user_ids']:
    display_user_data()