#!/usr/bin/env python3

import re
import operator


def main():
    pattern_info = r"ticky: INFO ([\w ']*) "
    pattern_error = r"ticky: ERROR ([\w ']*) "
    pattern_user = r"\((.+)\)"
    error_messages = {}
    users = {}

    with open("syslog.log", "r") as log:
        for line in log.readlines():
            match_error = re.search(pattern_error, line.strip())
            match_info = re.search(pattern_info, line.strip())

            if match_error:
                if match_error.group(1) not in error_messages:
                    error_messages[match_error.group(1)] = 1
                elif match_error.group(1) in error_messages:
                    error_messages[match_error.group(1)] += 1

            match_user = re.search(pattern_user, line.strip())
            user = match_user.group(0)[1:-1]
            if user not in users:
                users[user] = [0, 0]
                if match_error:
                    users[user][1] = 1
                elif match_info:
                    users[user][0] = 1
            elif user in users:
                if match_error:
                    users[user][1] += 1
                elif match_info:
                    users[user][0] += 1

    error_messages = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)
    users = sorted(users.items(), key=operator.itemgetter(0))

    with open("error_message.csv", "w") as file:
        file.write("Error,Count")
        file.write('\n')
        for items in error_messages:
            file.write("{},{}".format(items[0], items[1]))
            file.write('\n')
    
    with open("user_statistics.csv", "w") as file:
        file.write("Username,INFO,ERROR")
        file.write('\n')
        for items in users:
            file.write("{},{},{}".format(items[0], items[1][0], items[1][1]))
            file.write('\n')
        
if __name__ == "__main__":
    main()
