#4.# CWE-284: Improper Access Control
# Vulnerable line: if user_id == request.args.get('user_id'):
# Description: This code does not properly check if the user is authorized to access the requested user's data.
if user_id == request.args.get('user_id'):
    display_user_data()