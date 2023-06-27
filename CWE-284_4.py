#5.# CWE-284: Improper Access Control
# Vulnerable line: if user_role == 'admin' and user_id == request.args.get('user_id'):
# Description: This code does not properly check if the user is authorized to access the requested user's data and perform admin actions.
if user_role == 'admin' and user_id == request.args.get('user_id'):
    perform_admin_actions()