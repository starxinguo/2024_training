users = ['admin', '1', '2', '3', '4']
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?\n")
        else:
            print(f"Hello {user}thank you for logging in again.")
else:
    print("We need to find some users!")