from pprint import pprint 
import inquirer
import sys
import re


def starts_with_date(line):
    pattern = r'^\d{2}/\d{2}/\d{4}'
    return bool(re.match(pattern, line))

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

def get_user(filename):
    users_list = generate_users(filename)
    selected_user = [x for x in create_dropdown(users_list).values()]
    return selected_user[0]

def generate_user_file(filename, user):

    user_file = user+'.txt'
    current_speaker = ''

    with open(filename) as file:
        fw = open(user_file, mode="w")
        for line in file:
            if starts_with_date(line) and ': ' in line:
                current_speaker = line[line.find(' - ')+3:line.find(': ')]
                if current_speaker == user:
                    fw.write(line[line.find(': ')+1:])
            elif not starts_with_date(line) and current_speaker == user:
                fw.write(line)
        fw.close()

def parse(filename):
    username = get_user(filename)
    generate_user_file(filename,username)
    return username+'.txt'


