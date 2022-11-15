import api
import inquirer

api = api.ApiService('.user.db')


def mode():
    end = False
    while end is False:
        mode = [inquirer.List('mode', message="Select a mode: ", choices=["1. Insert Entry", "2. Delete Entry", "3. List Database", "4. Quit"],)]
        answers = inquirer.prompt(mode)
        if answers.get('mode') == '1. Insert Entry':
            insert_entry()
        if answers.get('mode') == "2. Delete Entry":
            delete_entry()
        if answers.get('mode') == "3. List Database":
            list_db()
        if answers.get('mode') == "4. Quit": 
            api.quit()
            print("session closed")
            end = True




def insert_entry():
    fname = input("Enter Users First Name: ")
    lname = input("Enter Users Last Name: ")
    age = int(input("Enter Users Age: "))
    dept = int(input("Enter Users Department Code\n1. Engineer\n2. HR\n3. Sales\n4. Development\nDepartment: "))

    if dept == 1:
        dept = 'Engineer'
    if dept == 2:
        dept = 'HR'
    if dept == 3:
        dept = 'Sales'
    if dept == 4:
        dept = 'Development'


    api.insert(fname,lname,age,dept)
    

def delete_entry():
    payload = api.fetch()
    mode = [
        inquirer.List
        (
            'mode', 
            message="Select a mode: ", 
            choices=[
                "1. Insert Entry", 
                "2. Delete Entry", 
                "3. List Database", 
                "4. Quit"],
        )
    ]
    answers = inquirer.prompt(mode)
    api.remove(id)

def list_db():
    api.fetch()