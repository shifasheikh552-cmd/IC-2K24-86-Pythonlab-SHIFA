#STUDENT GRADE CALCULATOR
last_student = None

def get_grade(average):
    # Scheme from Section B, Q3 (standard scheme)
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def enter_marks():
    global last_student
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return

        marks = []
        print("Enter marks for 5 subjects (out of 100):")
        for i in range(1, 6):
            while True:
                try:
                    m = float(input(f"  Subject {i}: "))
                    if 0 <= m <= 100:
                        marks.append(m)
                        break
                    else:
                        print("  Error: Marks must be between 0 and 100.")
                except ValueError:
                    print("  Error: Please enter a valid number.")

        total = sum(marks)
        average = total / 5
        grade = get_grade(average)

        last_student = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }
        print(f"\nData saved! {name}'s Average: {average:.2f}, Grade: {grade}")

    except Exception as e:
        print(f"Error: {e}")

def view_last_student():
    if last_student is None:
        print("\nNo student data found. Please enter marks first (Option 1).")
        return

    print("\n--- Last Entered Student ---")
    print(f"Name    : {last_student['name']}")
    print(f"Marks   : {last_student['marks']}")
    print(f"Total   : {last_student['total']}/500")
    print(f"Average : {last_student['average']:.2f}")
    print(f"Grade   : {last_student['grade']}")

def main():
    while True:
        print("\n------ STUDENT GRADE CALCULATOR ------")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            enter_marks()
        elif choice == '2':
            view_last_student()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()