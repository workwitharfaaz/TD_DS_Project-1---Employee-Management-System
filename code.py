import json


def load_employees():
    try:
        with open("employees.json", "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_employees(employees):
    with open("employees.json", "w") as f:
        json.dump(employees, f, indent=4)


def add_employee(employees):
    emp_id = input("Enter the emp_id: ")
    
    while emp_id in employees:
        print("Employee ID already exists. Try again.")
        emp_id = input("Enter the emp_id: ")

    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    department = input("Enter the department: ")
    salary = int(input("Enter the salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    save_employees(employees)
    print("Employee Successfully Added!\n")


def view_employees(employees):
    if not employees:
        print("No Employees Available.\n")
    else:
        print(f"\n{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<12} {'Salary':<10}")
        print("-" * 55)
        for emp_id, details in employees.items():
            print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} {details['department']:<12} {details['salary']:<10}")
        print()


def search_employee(employees):
    emp_id = input("Enter Employee ID to Search: ")

    if emp_id in employees:
        details = employees[emp_id]
        print(f"\n{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<12} {'Salary':<10}")
        print("-" * 55)
        print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} {details['department']:<12} {details['salary']:<10}")
    else:
        print("Employee not found.\n")


def remove_employee(employees):
    emp_id = input("Enter Employee ID to Remove: ")

    if emp_id in employees:
        confirm = input(f"Are you sure you want to remove {employees[emp_id]['name']}? (y/n): ")
        if confirm.lower() == 'y':
            del employees[emp_id]
            save_employees(employees)
            print("Employee removed successfully!\n")
        else:
            print("Operation cancelled.\n")
    else:
        print("Employee not found.\n")


def main_menu():
    employees = load_employees()

    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Remove Employee")
        print("5. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            view_employees(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            remove_employee(employees)
        elif choice == "5":
            print("Thank you! Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()
