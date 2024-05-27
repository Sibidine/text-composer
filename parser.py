from pprint import pprint 
import inquirer
import sys

def generate_users(filename):
    
    users_list = []
    with open(filename) as file:
        for line in file:
            name = line[line.find('-'):line.find(:)]
            if name not in users_list:
                users_list.append[name]
            continue

    return users_list

def create_dropdown(users_list):
    questions = [
            inquirer.List(
                message="Choose user to generate file for:",
                choices=users_list
                )
            ]
    answers = inquirer.prompt(questions)
    return answers

def main():
    filename = sys.argv[-1]
    users_list = generate_users(filename)
    selected_user = create_dropdown(users_list).values()[0]
    pprint(selected_user)

main()

