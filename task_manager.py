#=====importing libraries===========
# Import datetime for use of todays date when adding tasks
import datetime

#=====FUNCTION MENU OPTIONS===========

def menu_choice():
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    # If user is admin give them menu that includes Display Statistics
    if username == "admin":
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
ds - Display Statistics
gr - Generate reports
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
        if menu == "r":
            return register()
        elif menu == "a":
            return add_task()
        elif menu == "ds":
            return display_statisics()
        elif menu == "gr":
            return generate_statisics()
        elif menu == "va":
            return view_all()
        elif menu == "vm":
            return view_my()
        elif menu == "e":
            return exit_programne()
        else:
            print("Invalid input")
            return menu_choice()

    # Else give user generic menu
    else:
        menu = input('''\nSelect one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    ds - Display Statistics
    e - Exit
    : ''').lower()
        if menu == "a":
            return add_task()
        elif menu == "va":
            return view_all()
        elif menu == "ds":
            return display_statisics()
        elif menu == "vm":
            return view_my()
        elif menu == "gr":
            return generate_statisics()
        elif menu == "e":
            return exit_programne()
        else:
            print("Invalid input")
            return menu_choice()


#=====FUNCTION REGISTER USER===========

def register():
    print("\nREGISTER USER\n")
    # Enter user name, password, and reneter password
    new_user = str.lower(input("Enter new username: "))

    # CHECK IF USERNAME EXISTS IN FILE
    # Open user file
    with open("user.txt", "r") as f:
        # For each line in file
        for line in f:
            # Line split into items
            username_check = line.split(", ")
            # Check new user input aganist user name in text file. Will run until user does not match user already registered
            while new_user == username_check[0]:
                print("Username already registered, please try a differrent username.")
                new_user = str.lower(input("Enter new username: "))

    new_password = input("Enter new user password: ")
    new_passwordcheck = input("Re-enter password: ")
    # If passwords do not match print error
    if new_password != new_passwordcheck:
        print("Passwords do not match. Please try again.")
    # Else write user and password to user txt file, starting on new line with break and print confirmation
    else:
        with open("user.txt", "a") as f:
            f.write("\n" + new_user + ", " + new_password)
            print("User and password successfully registered.\n")
            return menu_choice()


#=====FUNCTION ADDING TASK===========

def add_task():
    print("\nAdd Task\n")
    # Ask for user inputs for each task
    # Added comma at end so each can be easily distinguished
    task_username = input("Username of task assigned to: ") + ", "
    task_title = input("Task title: ") + ", "
    task_description = input("Task Description: ") + ", "
    task_due_date = input("Enter due date: ") + ", "
    today = str(datetime.datetime.today()) + ", " #TODO Fix date function
    task_complete = "No"
    # Open tasks file
    with open("tasks.txt", "a") as f:
        # Starting on new line write task to txt document
        f.write("\n" + task_username + task_title + task_description + task_due_date + today + task_complete)
        # Confirm task added
        print("Task successfully added.")
        return menu_choice()

#=====FUNCTION Display Statistics===========

def display_statisics():
    print("\nDISPLAY STATISICS\n")

    # Generates statistic reports
    generate_statisics()

    # Open user overview report
    with open("user_overview.txt", "r") as dispaly_user_statistics:
        print("\n-----------User Overview-----------\n")
        # Prints each line from user overview report
        user_lines = dispaly_user_statistics.readlines()
        for line in user_lines:
            print(line)
    
    # Open task overview report
    with open("task_overview.txt", "r") as dispaly_task_statistics:
        print("\n-----------Task Overview-----------\n")
        # Prints each line from report
        task_lines = dispaly_task_statistics.readlines()
        for line in task_lines:
            print(line)

    return menu_choice()        


#=====FUNCTION VIEW ALL TASKS===========

def view_all():
    # Open tast text file as read only
    with open("tasks.txt", "r") as f:
        # Enumerate used to print task number
        # For each line in text file
        for count, line in enumerate(f, start=1):
            # Strip line breaks and split data into item list seperated by , space
            task_data = line.strip("\n").split(", ")
            # Displays Task number
            viewtasks = f"\n------ Task {count} --------\n"
            viewtasks += "\n"
            # Prints on each line as per index from each line's item list
            viewtasks += f"Assigned to: {task_data[0]}\n"
            viewtasks += f"Task: {task_data[1]}\n"
            viewtasks += f"Description: {task_data[2]}\n"
            viewtasks += f"Assigned Date: {task_data[3]}\n"
            viewtasks += f"Due Date: {task_data[4]}\n"
            viewtasks += f"Task Complete: {task_data[5]}\n"
            viewtasks += "\n"
            viewtasks += "-----------------------"
            # Prints task
            print(viewtasks)

    return menu_choice()

#=====EDIT TASK===========

def edit_task():
    # Open task file as read only
    with open("tasks.txt", "r") as f:
        # Assign data from file to data variable
        data = f.readlines()
        # Ask user what task number they want to edit. 
        # Minus 1 to match enumerate count
        task_num = int(input("What task nunber do you want to update?")) - 1
        # Strip task line into items
        task_line_data = data[task_num].strip("\n").split(", ")
        
        # If the task is marked as complete
        if task_line_data[-1] == "Yes":
            # Can not update task
            print("This task is marked as complete. You are cannot update this task.")
            return menu_choice()

        # Display task user has selected for editiing
        viewtasks = f"------ You are updating task number {(task_num + 1)} --------\n"
        viewtasks += "\n"
        viewtasks += f"Assigned to: {task_line_data[0]}\n"
        viewtasks += f"Task: {task_line_data[1]}\n"
        viewtasks += f"Description: {task_line_data[2]}\n"
        viewtasks += f"Assigned Date: {task_line_data[3]}\n"
        viewtasks += f"Due Date: {task_line_data[4]}\n"
        viewtasks += f"Task Complete: {task_line_data[5]}\n"
        viewtasks += "\n"
        viewtasks += "-----------------------"
        print(viewtasks)

        #TODO Check with user if task selected is correct. If no return to beginning. If yes continue    

        # Ask user how they would like to update task - Mark as complete / Edit Due Date / Edit Assigned User
        edit_field = str.lower(input("How would you like to update the task?\nM - Mark as complete\nD - Edit Due Date\nU - Edit Assigned User"))
        
        # If user selects mark as complete
        if edit_field == "m":
            # Assign complete as Yes
            task_line_data[-1] = "Yes\n"
            # Rejoin items to make new data string ready to add to text file
            new_data = ", ".join(task_line_data)
            # Task line user selected now equals new data string - Data 
            data[task_num] = new_data
            # Open task file as write
            with open("tasks.txt", "w") as complete_task:
                # Write each line of the updated data variable to the task file
                for line in data:
                 complete_task.write(line)
            print("\nTask marked as complete\n")
            return menu_choice()

        # If user selects Edit Due Date
        elif edit_field == "d":
            new_due_date = input("What is the new due date for this task? Format should be day month and year e.g. 10 Oct 2019")
            #TODO Add date format check
            # Task line due date equals new due date
            task_line_data[-2] = new_due_date
            # Join task line items into string variable new data
            new_data = ", ".join(task_line_data)
            # Assign updated task line to corresponding data line
            data[task_num] = new_data
            # Open task file as write
            with open("tasks.txt", "w") as complete_task:
                # Add each line of updated data to tesk file
                for line in data:
                 complete_task.write(line + "\n")
            print("\nDue date has successfully updated\n")
            return menu_choice()
        
        # If user selects Update User
        elif edit_field == "u":
            # Ask for new user name
            new_user_task = input("Who do you want to assign this task to?")
            # Assign new user to task item
            task_line_data[0] = new_user_task
            # Join task line items into string variable new data
            new_data = ", ".join(task_line_data)
            # Assign updated task line to corresponding data line
            data[task_num] = new_data
            # Add each line of updated data to tesk file
            with open("tasks.txt", "w") as complete_task:
                for line in data:
                 complete_task.write(line + "\n")
            print("\nUser has successfully updated\n")
            return menu_choice()
        
        # If user selects invalid option
        else:
            print("Wrong input enterted. Please try again")
            return edit_task()

        #TODO Add option if user would like to exit edit task
        #TODO Break edit options into their own functions


#=====FUNCTION VIEW MY TASKS===========


def view_my():
    print("VIEW MY TASKS")
    # Open task text file as read only
    with open("tasks.txt", "r") as f:
        # Uses enumerate to confirm task number to user
        # For each line in task file
        for count, line in enumerate(f, start=1):
            # Split each line into a list
            task_data = line.strip("\n").split(", ")
            # If each line index 0 matches username
            if task_data[0] == username:
                # Print the task line
                viewtasks = f"------ Task {count} --------\n"
                viewtasks += "\n"
                viewtasks += f"Assigned to: {task_data[0]}\n"
                viewtasks += f"Task: {task_data[1]}\n"
                viewtasks += f"Description: {task_data[2]}\n"
                viewtasks += f"Assigned Date: {task_data[3]}\n"
                viewtasks += f"Due Date: {task_data[4]}\n"
                viewtasks += f"Task Complete: {task_data[5]}\n"
                viewtasks += "\n"
                viewtasks += "-----------------------"
                print(viewtasks)
            else:
                print("You do not have any tasks assigned to you")
        # Ask if user would like to update their task
        edit_choice = str.lower(input("Would you like to update your task? Y or N"))
        if edit_choice == "y":
            return edit_task()
        else:
            return menu_choice()

#=====FUNCTION GENERATE STATISTICS===========

def generate_statisics():

    # Variables needed for counts and date format
    task_complete = 0
    tasks_uncomplete = 0
    overdue = 0
    task_count = 0
    date_format = '%d %b %Y'
    user_count = 0
    user_task_count = 0
    user_task_complete = 0
    user_overdue = 0
    user_task_incomplete = 0

    # Open task file
    with open("tasks.txt", "r") as f:
        # For each line in file
        for line in f:
            # For Task count
            task_count += 1
            # Breaks line data into items
            task_data = line.strip("\n").split(", ")
            # Assigns due date to string variable
            due_date_str = task_data[-2]
            # Converts due date sting into datetime - uses date format variable 
            dt = datetime.datetime.strptime(due_date_str, date_format)

            # === If task marked as complete ===
            if task_data[-1] == "Yes":
                # Task complete count plus 1
                task_complete += 1
            
            # === If task not complete ===
            if task_data[-1] == "No":
                # Task incoplete plus 1
                tasks_uncomplete +=1
                # If task is not marked as complete check if overdue
                if dt < datetime.datetime.today():
                    # If overdue count plus one
                    overdue += 1

            # === If user assigned task line ===
            if task_data[0] == username:
                # User count plus 1
                user_task_count += 1
                # If marked as complete
                if task_data[-1] == "Yes":
                    # Users completed tasks count plus 1 
                    user_task_complete += 1
                # If marked as complete
                if task_data[-1] == "No":
                    # Users completed tasks count plus 1 
                    user_task_incomplete += 1
                # Checks if task is over due and adds 1 to count if true
                if dt < datetime.datetime.today():
                    user_overdue += 1
                
                
    # Percentage calculations and formated to 2 decimal places and % added
    # Except added to remove zerodivision error if a number equals 0 and assignes variable to 0
    try:
        percent_incomplete = '{0:.0f}'.format((tasks_uncomplete / task_count * 100))
    except ZeroDivisionError:
        percent_incomplete = 0

    try:
        percent_overdue = '{0:.0f}'.format((overdue / tasks_uncomplete * 100))
    except ZeroDivisionError:
        percent_overdue = 0

    try:
        percent_assigned = '{0:.0f}'.format((user_task_count / task_count * 100))
    except ZeroDivisionError:
        percent_assigned = 0
    
    try:
        percent_usertask_compplete = '{0:.0f}'.format((user_task_complete / user_task_count * 100))
    except ZeroDivisionError:
        percent_usertask_compplete = 0
    
    try:
        percent_usertask_incomplete = '{0:.0f}'.format((user_task_incomplete / user_task_count * 100))
    except ZeroDivisionError:
        percent_usertask_incomplete = 0

    try:
        pecent_user_overdue = '{0:.0f}'.format((user_overdue / user_task_count * 100))
    except ZeroDivisionError:
        pecent_user_overdue = 0

    # Dictionary of task overview
    task_overview = {
        "Total tasks": task_count,
        "Total completed": task_complete,
        "Tasks incomplete": tasks_uncomplete,
        "Overdue": overdue,
        "Percent incomplete": percent_incomplete,
        "Percent overdue": percent_overdue,
        }
    
    # Open task overview txt file as write
    with open("task_overview.txt", 'w') as f:
        # For each key and value in task task overview
        for key, value in task_overview.items():
            # Write to file
            f.write('%s: %s\n' % (key, value))

    with open("user.txt", "r") as f:
        for line in f:
            user_count += 1
            user_data = line.strip("\n").split(", ")

    user_overview = {
        "Total users": user_count,
        "Total tasks": task_count,
        "User tasks": user_task_count,
        "Percent assigned to user": percent_assigned,
        "Percent tasks complete": percent_usertask_compplete,
        "Percent tasks incomplete": percent_usertask_incomplete,
        "Percent of overdue tasks": pecent_user_overdue
    }

    with open("user_overview.txt", 'w') as f:
        for key, value in user_overview.items():
            f.write('%s: %s\n' % (key, value))


#=====FUNCTION EXIT===========

def exit_programne():
    print('Goodbye!!!')
    exit()



#====Login Section====

# Credential match set to false
credential_match = False

# While loop to run whilst credential match is set to false
while not credential_match:
    # Open user.txt as read only
    with open("user.txt", "r") as f:
        # Ask user for credentials
        print("Please sign in using your username and password:")
        username = str.lower(input("Username: "))
        password = input("Password: ")
        # For each line in text file
        for line in f:
            # Line is split into item list seperated by , and space and strip removes any spaces beginning or end
            stored_login = line.strip("\n").split(", ")
            # If username and password entered matches line in file
            if username == stored_login[0] and password == stored_login[1]:
             # Login succesfull. Change credemtial match to True to break from loop
             print("Log in successful\n")
             credential_match = True
             break
        # Else statement for log in failure
        else:
            print("Invalid username and/or password, please try again")

menu_choice()