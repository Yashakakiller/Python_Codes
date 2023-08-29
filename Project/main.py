import pyfiglet
import time
import pandas as pd

#Formatted Text
def display_banner(message):
    banner = pyfiglet.Figlet()
    return banner.renderText(message)


#Display Main Menu
def show_main_menu():
    print(display_banner("Main Menu"))
    print("""
    1 READ CSV FILE
        1a dataframe 1
        1b dataframe 2
    2 MANIPULATION
        2a add new row
        2b add new column
        2c delete a column
        2d delete a row
        2e modify values of a row
        2f modify values of a column
        2g modify single value
    3 ANALYSIS
        3a display first n rows
        3b display last n rows
        3c display nonadjacent columns
        3d display nonadjacent rows
        3e display shape, size, information
        3f display asked value
    4 VISUALIZATION
        4a bar chart
        4b line chart
        4c histogram
        4d pie chart
    5 Exit
    """)

def get_user_choice():
    try:
        choice = int(input("Enter the number to perform the operation: "))
        if choice < 1 or choice > 5:
            print("\nYou have entered an invalid number.\n")
            return get_user_choice()
        return choice
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_choice()
    

def userChoiceOperation(user_choice):
    if(user_choice == 1):
        print("""
                For this program , we have 2 CSV FILES , please select any 1 of the below files
              
                        a) CSV 1
                        b) CSV 2 """)
        csv_selection = int(input("Enter the number : "))
        if(csv_selection == 1 ):
            csv_read = pd.read_csv("data1.csv", encoding="utf-8")
        

            
       
        

def main():
    time.sleep(2)
    show_main_menu()
    user_choice = get_user_choice()
    userChoiceOperation(user_choice)

main()



