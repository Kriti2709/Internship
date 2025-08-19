import datetime

class Employee:
    def __init__(self, emp_id, name, email, dept, joining_date):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.department = dept
        self.joining_date = datetime.datetime.strptime(joining_date, "%Y-%m-%d").date()
        self.leave_balance = 20  # default yearly leave balance
        self.leave_requests = []  # (start_date, end_date, status)

class LeaveManagementSystem:
    def __init__(self):
        self.employees = {}
        self.emp_counter = 1

    def add_employee(self, name, email, dept, joining_date):
        emp = Employee(self.emp_counter, name, email, dept, joining_date)
        self.employees[self.emp_counter] = emp
        print(f"✅ Employee {name} added with ID {self.emp_counter}")
        self.emp_counter += 1

    def apply_leave(self, emp_id, start_date, end_date):
        if emp_id not in self.employees:
            print("❌ Employee not found")
            return

        emp = self.employees[emp_id]
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

        # Edge cases
        if start < emp.joining_date:
            print("❌ Cannot apply leave before joining date")
            return
        if end < start:
            print("❌ Invalid leave dates (end before start)")
            return
        days = (end - start).days + 1
        if days > emp.leave_balance:
            print("❌ Not enough leave balance")
            return
        for (s, e, status) in emp.leave_requests:
            if status == "Approved" and not (end < s or start > e):
                print("❌ Overlapping leave request")
                return

        emp.leave_requests.append((start, end, "Pending"))
        print(f"✅ Leave request submitted for {days} days")

    def approve_leave(self, emp_id, index, approve=True):
        if emp_id not in self.employees:
            print("❌ Employee not found")
            return
        emp = self.employees[emp_id]
        if index < 0 or index >= len(emp.leave_requests):
            print("❌ Invalid request index")
            return
        start, end, status = emp.leave_requests[index]
        if status != "Pending":
            print("❌ Already processed")
            return

        if approve:
            days = (end - start).days + 1
            emp.leave_balance -= days
            emp.leave_requests[index] = (start, end, "Approved")
            print("✅ Leave Approved")
        else:
            emp.leave_requests[index] = (start, end, "Rejected")
            print("❌ Leave Rejected")

    def show_leave_balance(self, emp_id):
        if emp_id not in self.employees:
            print("❌ Employee not found")
            return
        emp = self.employees[emp_id]
        print(f"👤 {emp.name} | Balance: {emp.leave_balance} days")

    def list_employees(self):
        for emp_id, emp in self.employees.items():
            print(f"{emp_id}. {emp.name} ({emp.department}) - {emp.email}")


# --- Console Menu ---
def main():
    system = LeaveManagementSystem()
    while True:
        print("\n=== Leave Management Menu ===")
        print("1. Add Employee")
        print("2. Apply Leave")
        print("3. Approve/Reject Leave")
        print("4. Show Leave Balance")
        print("5. List Employees")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            dept = input("Department: ")
            joining = input("Joining Date (YYYY-MM-DD): ")
            system.add_employee(name, email, dept, joining)

        elif choice == "2":
            emp_id = int(input("Employee ID: "))
            s = input("Start Date (YYYY-MM-DD): ")
            e = input("End Date (YYYY-MM-DD): ")
            system.apply_leave(emp_id, s, e)

        elif choice == "3":
            emp_id = int(input("Employee ID: "))
            system.show_leave_balance(emp_id)
            idx = int(input("Request index (0..n): "))
            decision = input("Approve? (y/n): ")
            system.approve_leave(emp_id, idx, approve=(decision.lower() == "y"))

        elif choice == "4":
            emp_id = int(input("Employee ID: "))
            system.show_leave_balance(emp_id)

        elif choice == "5":
            system.list_employees()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
