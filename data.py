import csv

def export_to_csv(students):
     
     if not students:
         print("No students to export")
         return

     with open ("students.csv", "a", newline="") as file:
        fieldnames= ["name","group", "spanish","english", "social", "science"]
        writer= csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell()==0:
            writer.writeheader()
     
        for student in students:

            writer.writerow(student)     
    
     print(f"Exported {len(students)} student(s) to students.csv")

###

def import_students_from_csv(filename=None):

    if filename is None:
        filename = input("Enter the file name: ")

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            students = []  

            for row in reader:
                student = {
                    "name": row["name"],
                    "group": row["group"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "social": int(row["social"]),
                    "science": int(row["science"])
                }
                students.append(student)

        print(f"{len(students)} students imported from {filename}")
        return students
    except FileNotFoundError:
        print("No previously exported file found. Please export students first.")
        return []