import datetime
# import mysql.connector
# import os


def task_menu():
    print('============================================')
    print('Please Choose your task')
    print('============================================')
    print('LG : Login')
    print('RG : Register')
    print('US : User')
    print('EMP : Employee')
    print('TS : Timesheets')
    print('============================================')


def task_input(index):
    task = input(f"Choose a task {index + 1}: ")
    return task


def calculate_hours(hour):
    midnight = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    time_delta = datetime.timedelta(hours=hour)
    time_obj = (midnight + time_delta).time()

    if hour > 24:
        return f"({hour // 24} day, {time_obj})"

    return f"({time_obj})"


def input_hours():
    while True:
        work_hours = float(input("Enter your working hour for login (in float, e.g 1.5 for 1 hour 30 minutes): "))
        if (work_hours < 0):
            print("Invalid input value")
        else:
            break
    return work_hours


def summary(username, task_dic):
    print(f"Summary of Task for {username}")
    task_name = {"LG": "Login", "RG": "Register", "US": "User", "EMP": "Employee", "TS": "Timesheet"}
    for i, v in task_dic.items():
        hours = calculate_hours(v)
        print(f"Task: {task_name[i]}, Working Hours: {v:.2f} {hours}")


# def save_to_db(username, task_dic):
#   mydb = mysql.connector.connect(
#       host="localhost",
#       user="root",
#       password="DeptIT2022;",
#       database="test_python"
#     )

#   mycursor = mydb.cursor()

#   # Insert user
#   sql = "INSERT INTO users (username) VALUES (%s)"
#   val = [(username)]
#   mycursor.execute(sql, val)

#   # Insert Task
#   task_sql = "INSERT INTO tasks (task, hours) values (%s, %s)"
#   task_val =

#   mydb.commit()

#   print(mydb)

def main():
    username = input("Enter your name: ")
    number_of_task = input("Enter the number of task you want to do: ")
    task_dic = dict()
    task_list = ["LG", "RG", "US", "EMP", "TS"]
    for i in range(int(number_of_task)):
        task_menu()
        while True:
            task = task_input(i)
            if task not in task_list:
                print("Input invalid, please try again !")
            else:
                work_hours = input_hours()
                task_dic[task] = work_hours
                break

    summary(username, task_dic)
    # save_to_db("test", "test")


if __name__ == "__main__":
    main()
