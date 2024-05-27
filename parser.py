from pprint import pprint 
import inquirer
import sys
import re


def starts_with_date(line):
    pattern = r'^\d{2}/\d{2}/\d{4}'
    return bool(re.match(pattern, line))

# Test examples

def generate_users(filename):
    
    users_list = []
    with open(filename) as file:
        for line in file:
            if starts_with_date(line) and ': ' in line:
                name = line[line.find(' - ')+3:line.find(': ')]
                if name not in users_list:
                    users_list.append(name)
                continue

    return users_list

def create_dropdown(users_list):
    questions = [
            inquirer.List(
                "User",
                message="Choose user to generate file for",
                choices=users_list,
                ),
            ]
    answers = inquirer.prompt(questions)
    return answers

def main():
    filename = sys.argv[-1]
    users_list = generate_users(filename)
    selected_user = [x for x in create_dropdown(users_list).values()]
    pprint(selected_user[0])

main()

