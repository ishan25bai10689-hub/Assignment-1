import os

# This function calculates the grade based on the average marks
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "Fail"

# This function handles the main logic
def main():
    print("--- Simple Student Report Card ---")
    
    # 1. Input: Get student details
    # We use simple input() and convert numbers to integers
    name = input("Enter Student Name: ")
    reg_no = input("Enter Registration Number: ")
    
    print("Enter marks for 3 subjects (out of 100):")
    try:
        sub1 = int(input("Subject 1 Marks: "))
        sub2 = int(input("Subject 2 Marks: "))
        sub3 = int(input("Subject 3 Marks: "))
    except ValueError:
        print("Error: Please enter valid numbers only.")
        return # Stop the program if input is wrong

    # 2. Process: Calculate Total and Average
    total = sub1 + sub2 + sub3
    average = total / 3
    
    # Get the grade using our function
    grade = get_grade(average)

    # 3. Output: Show the result on screen
    print("\n----------------------------")
    print("REPORT CARD FOR: ", name)
    print("Total Marks: ", total, "/ 300")
    print("Average: ", round(average, 2))
    print("Final Grade: ", grade)
    print("----------------------------")

    # 4. Save: Write this to a text file (Real-world application)
    # 'a' means append (add to the end of the file)
    with open("class_records.txt", "a") as f:
        # We create a simple string to save
        record = name + "," + reg_no + "," + str(grade) + "\n"
        f.write(record)
        print("Data saved to class_records.txt successfully.")

# Run the program
if __name__ == "__main__":
    while True:
        main()
        # Ask user if they want to continue
        again = input("\nDo you want to add another student? (yes/no): ")
        if again.lower() != "yes":
            print("Exiting program.")
            break