"""
DOCSTRING
THIS IS MAIN APPLICATION ,IN WHICH MENU IS GIVEN FOR USER . USER SELECT ONE CHOICE, 
THEN MODULE CALL IS DONE ACCORDING TO  USER SELECTION

"""
from ass1submodule import * # IMPORT THE ASS2SUBMODULE PROGRAM WHICH CONTAINS CODE FOR OPERATIONS

   
def main(): # START OF MAIN MODULE

    choice=0
    s1=Student("0220180193","paddu","05/06/2000","paddu@mitaoe.ac.in","9552756170")
    
    while True: # START OF WHILE LOOP
        print("\n")
        print("Select the option: \n")
        print("1. Add") 
        print("2. Search")
        print("3. Delete")
        print("4. Update")
        print("5. Display")
        print("6. Number of students")
        print("7. Exit\n")
        choice = int(input())
        
        # CHOICE SELECTED BY USER WILL BE COMPARE AND CALL MODULE ACCORDINGLY
        if choice == 1:
            s1.addStudent()
        elif choice == 2:
            s1.search()
        elif choice == 3:
            s1.delStudent()
        elif choice == 4:
            s1.update()
        elif choice == 5:
            s1.display()
        elif choice == 6:
            s1.count()
            
        elif choice == 7:
            break
        else:
            print("\nWrong Choice choosed.........") # EXECUTE WHEN USER SELECT THE OTHER OPTION WHICH IS NOT GIVEN IN MENU
    # END OF WHILE LOOP
    


main() # CALL TO MAIN MODULE