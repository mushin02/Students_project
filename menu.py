import actions
import data

def show_menu():

    all_students=[]


    while True:
        try:
            options = int(input(
                '''
Choose an option:
1 - Add student(s)
2 - show all students
3 - show top 3 students
4 - show class average
5 - Export to CSV
6 - Import from CSV
7 - Delete Student
8 - show failed students
0 - Exit
--> '''
            ))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
        if options==1:
            actions.add_students(all_students)
        elif options==2:
            actions.show_all_students(all_students)
        elif options==3:
            actions.print_top3_avgs(all_students)
        elif options==4:
            actions.print_avg_of_avg_grades(all_students)
        elif options==5:
            data.export_to_csv(all_students)
        elif options==6:
            all_students = data.import_students_from_csv()
        elif options==7:
            actions.delete_student(all_students)   
        elif options==8:
            actions.show_failed_students(all_students)
        elif options==0:
            print("Goodbye!")
            break    
        else:
            print("Invalid option, try again")    


