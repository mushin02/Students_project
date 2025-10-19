def add_students(all_students):
    
    while True:
        try:
            number_of_students= int(input("How many students do you want to add? "))
            if number_of_students > 0:
                break
            else:
                print("Please enter a valid number")
        except ValueError:                        
            print("Invalid input. Please enter a number")

    for student in range(number_of_students):    
        while True:
            name= input("student name? ").strip()
            if not name:
                print("Name cannot be empty")
            elif any(character.isdigit() for character in name):
                print("Name cannot contain numbers")
            else:
                break    
                
        while True:
            group= input("student group? (e.g 10A)").strip().upper()
            if len(group) >=2 and group[:-1].isdigit() and group[-1].isalpha():
                break
            else:
                print("invalid group format")

        duplicate = any(
            s["name"].lower()== name.lower() and s["group"].upper() == group 
            for s in all_students
            )
    
        if duplicate:
            print(f"student '{name} in group '{group}' already exists")
            continue

    
        students = {"name": name, "group": group}    
        for subject in["spanish","english","social","science"]:
            while True:
                try:
                    grade= int(input(f"{subject} grade: "))
                    if grade >= 0 and grade <=100:
                        students[subject] = grade
                        break
                    else:
                        print("Grade must be between 0 and 100")
                except ValueError:
                    print("Please enter a valid number")        


        all_students.append(students)

    return all_students    

###

def show_all_students(all_students):
    
    
    if not all_students:
        print("No students to show.")
        return

    for s in all_students:
        print(f"Name: {s['name']}")
        print(f"Group: {s['group']}")
        print(f"Spanish: {s['spanish']}")
        print(f"English: {s['english']}")
        print(f"Social: {s['social']}")
        print(f"Science: {s['science']}")
        print("-" * 20) 

##

def print_top3_avgs(all_students):

    
    students_with_avg = []
    
    for student in all_students:
            grades = [
                int(student["spanish"]),
                int(student["english"]),
                int(student["social"]),
                int(student["science"])
            
            ]
            avg= sum(grades) / len(grades)
            
            students_with_avg.append((student["name"], avg))
            
    students_with_avg.sort(key=lambda student: student[1], reverse=True)
            
    for name, avg in students_with_avg[:3]:
        print(f"{name}: {avg:.2f}")

###

def print_avg_of_avg_grades(all_students):
   

    if not all_students:
        print("No students available.")
        return
    
    avg_grades = []

    for student in all_students:
        grades = [
            int(student["spanish"]),
            int(student["english"]),
            int(student["social"]),
            int(student["science"])
        ]
        avg = sum(grades) / len(grades)
        avg_grades.append(avg)

    class_avg = sum(avg_grades) / len(avg_grades)
    print(f"Class average grade: {class_avg}")
    return class_avg

##
def delete_student(all_students):
    

    if not all_students:
        print("No students to delete.")
        return
    
    search_name = input("Enter the name of the student to search: ").strip().lower() 

    matches = [(indx, s) for indx, s in enumerate(all_students, start=1) if s["name"].lower() == search_name]

    if not matches:
        print("f'Student {search_name} not found")
        return

    for indx, s in matches:
        print(f"{indx}, {s['name']} (group: {s['group']})")

    try:
        choice = int(input("Enter the number of the student to delete"))
        if any(indx == choice for indx, _ in matches):
            removed = all_students.pop(choice - 1)
            print(f"Student '{removed['name']}' deleted successfully")

        else:
            print("Invalid choice. That student number does not match your search.")
    except ValueError:
        print("please enter a valid number")        

##

def show_failed_students(all_students):
    

    if not all_students:
        print("Nostudents to show")
        return
    
    failed_students= []

    for s in all_students:
        if any(s[subject]<60 for subject in ["spanish", "english", "social", "science"]):
            failed_students.append(s)

    if not failed_students:
        print("No students have failed")
        return

    for s in failed_students:
        print(f"Name: {s['name']}") 
        print(f"Group: {s['group']}")
        print(f"Spanish: {s['spanish']}")
        print(f"English: {s['english']}")
        print(f"Social: {s['social']}")
        print(f"Science: {s['science']}")
        print("-" * 20)

               



