
def file_action(filename):

    try:
        file = open(filename, "r")

    except FileNotFoundError:
        print("Wrong name of file/path")

    else:
        user_last_login = {}
        user_total_time = {}

        for line in file:
            user, action, time = line.split(';')
            if action == "LOGIN":
                user_last_login[user] = int(time)
            if action == "LOGOUT":
                user_total_time[user] = user_total_time.get(user, 0) + (int(time) - int(user_last_login[user]))

        for user in user_total_time:
            print(f"{user}: {user_total_time[user]}s")

def calculate_time(lines):

    for part in lines():
        pass


dictionary = file_action("Dane\logs.txt")
