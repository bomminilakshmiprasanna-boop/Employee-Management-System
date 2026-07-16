"""Employee Management System (Basic)
Menu-driven demo project for internship.
"""
import json, os

FILE="employees.json"

def load():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=2)

def add(data):
    emp={
      "id":input("ID: "),
      "name":input("Name: "),
      "dept":input("Department: "),
      "designation":input("Designation: "),
      "salary":float(input("Salary: ")),
      "phone":input("Phone: ")
    }
    data.append(emp); save(data); print("Added.")

def view(data):
    if not data: print("No employees."); return
    for e in data:
        print(e)

def search(data):
    eid=input("Employee ID: ")
    for e in data:
        if e["id"]==eid:
            print(e); return
    print("Not found")

def update(data):
    eid=input("Employee ID: ")
    for e in data:
        if e["id"]==eid:
            e["name"]=input(f'Name ({e["name"]}): ') or e["name"]
            e["dept"]=input(f'Department ({e["dept"]}): ') or e["dept"]
            s=input(f'Salary ({e["salary"]}): ')
            if s: e["salary"]=float(s)
            save(data); print("Updated"); return
    print("Not found")

def delete(data):
    eid=input("Employee ID: ")
    for i,e in enumerate(data):
        if e["id"]==eid:
            data.pop(i); save(data); print("Deleted"); return
    print("Not found")

def report(data):
    print("Total Employees:",len(data))
    print("Total Salary:",sum(e["salary"] for e in data))

def main():
    data=load()
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Update\n5.Delete\n6.Report\n7.Exit")
        ch=input("Choice: ")
        if ch=="1": add(data)
        elif ch=="2": view(data)
        elif ch=="3": search(data)
        elif ch=="4": update(data)
        elif ch=="5": delete(data)
        elif ch=="6": report(data)
        elif ch=="7": break
        else: print("Invalid")
if __name__=="__main__":
    main()