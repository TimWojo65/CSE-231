################################################################################
#
# Computer Project 05
#
#
#
#
#
#
#
#
#
################################################################################


import csv
from operator import itemgetter

# --- Menu and injury_lst (read-only) ---
menu = '''
    Menu : 
        1: The maximum exercise time a pet received
        2: Individual pet information
        3: The pets with abnormal diet conditions
        4: Top 5 pets in exercise time
        5: The pets with injury records
        6: The number of pets who took vaccines no more than X
        7: Top 10 pets in overall score ranking
        X: Exit
'''

injury_lst = ["Burn", "Bite", "Cut", "Scratch"]

#diet list is frequency, protein, and fat

# use these strings in your input and print statements.
"\n:~Enter a pet names file ~:"
"\n:~Enter a Diet record file ~:"
"\n:~Enter a Exercise record file ~:"
"\n:~Enter a Health record file ~:"
"Error. File does not exist"
"\nThank you and Good Bye"

"\n:~Input a choice ~:"
"Error: Invalid choice. Please enter a valid choice."

#------------------option 1
"\n--------------"
"Maximum exercise time: {} minutes"
"Pet name(s): {}"

#----------------option 2
"\n:~Enter a pet name ~:"
"Invalid name or does not exist"

"\n--------------"
"Diet:\n\tMeal frequency: {}\n\tNutritional Balance:\n\t\tProtein: {}\n\t\tFat: {}"

"\n--------------"
"Exercise:\n\tWalk(s): {}\n\tPlay time: {}"

"\n--------------"
"Health:\n\tVaccines taken: {}\n\tInjury reports: {}"

#------------option 3
"\n--------------"
"The number of pets with abnormal diet conditions: {}"
"\t{}:\n\t Meal: {}, Protein: {}, Fat: {}"

#------------option 4
"\n--------------"
"{}: {}"

#------------option 5
"\n--------------"
"{}: {}"

#------------option 6
"\n:~Enter the vaccine number ~:"
"Invalid input"
"Number of pet(s): {}"

#------------option 7
"\n--------------"
"{}: {}"



# All your functions definition starts here


#this should look at fp_exercise, and [0]*30 + [1] for each line
#take the largest of these values, and return the index for that line
#take that index num, and use it to grab the same id from fp_names and return that

#no actually this should re-sort the list of names in order of most to least
#exercise, that way it can be re-used for multiple options
def top_exercise(exercise, names):
    name_and_time = []
    for i in range(len(exercise)):
        first = int(exercise[i][0])
        second = int(exercise[i][1])
        total = first * 30 + second
        name_and_time.append([names[i][0].strip(), total])

    #name_and_time.sort(key=lambda x: x[1], reverse=True)

    return name_and_time

#this function should create a new list, where each line consists of 3 values
#name, vaccine num, and injury type
#this can then be sorted by vaccines or injuries, depending on the option chosen
def health_info(names, health):
    health_list=[]
    for i in range(len(names)):
        health_list.append([names[i][0], health[i][0], health[i][1]])
    return health_list

#this counts the vaccine total and returns that number, and is its own function
#so it can be used multiple times to return different vaccine totals without
#the counter getting all fucked up. It resets every time the function is called
def vaccine_count(health_list, vaccine_num):
    pet_num = 0
    vaccine_num=int(vaccine_num)
    for i in health_list:
        vaccines = int(i[1])
        if vaccines <= vaccine_num:
            pet_num += 1
    return pet_num

#this should create a master list. It should contain multiple lists within it
# holding every value throughout all the separate csv files. The lists should follow
#this format: [name, diet[0]and[1]and[2], exercise[0]and[1], and health[0]and[1]
def big_list(names, diet, exercise, health):
    master_list = []
    for i in range(len(names)):
        master_list.append([names[i][0], diet[i][0], diet[i][1], diet[i][2], exercise[i][0], exercise[i][1], health[i][0], health[i][1]])
    return master_list

def open_file(message):
    while True:
        filename=input(message)
        try:
            fp=open(filename,"r")
            return fp
        except FileNotFoundError:
            print("Error. File does not exist")






def read_files(fp_names, fp_diet, fp_exercise, fp_health):
    reader_names = csv.reader(fp_names)
    reader_diet = csv.reader(fp_diet)
    reader_exercise = csv.reader(fp_exercise)
    reader_health = csv.reader(fp_health)

    names_data = [line for line in reader_names]
    diet_data = [line for line in reader_diet]
    exercise_data = [line for line in reader_exercise]
    health_data = [line for line in reader_health]

    return names_data, diet_data, exercise_data, health_data



valid_menu=["1","2","3","4","5","6","7"]




def main():
    fp_names = open_file("\n:~Enter a pet names file ~:")
    fp_diet = open_file("\n:~Enter a Diet record file ~:")
    fp_exercise = open_file("\n:~Enter a Exercise record file ~:")
    fp_health = open_file("\n:~Enter a Health record file ~:")
    names, diet, exercise, health = read_files(fp_names, fp_diet, fp_exercise, fp_health)
    #names, diet, exercise, health = read_files(open("Names.csv"), open("diet_0.csv"), open("exercise_0.csv"), open("health_0.csv"))
    master_list = big_list(names, diet, exercise, health)
    finish=False
    while True:
        print(menu)
        while True:
            menu_choice=input("\n:~Input a choice ~:")
            if menu_choice in valid_menu:
                break
            elif menu_choice == "X":
                print("\nThank you and Good Bye")
                finish=True
                break
            else:
                print("Error: Invalid choice. Please enter a valid choice.")
        if finish==True:
            break
        if menu_choice == "1":
            name_and_time = top_exercise(exercise, names)
            total = name_and_time[0][1]
            name = name_and_time[0][0]
            print("\n--------------")
            print("Maximum exercise time: {} minutes".format(total))
            print("Pet name(s): {}".format(name))
        elif menu_choice == "2":
            while True:
                dummy_value = False
                pet_name = input("\n:~Enter a pet name ~:")
                for i, j in enumerate(names):
                    if pet_name == j[0].strip():
                        dummy_value=True
                        index_value = i
                        break
                if dummy_value==False:
                    print("Invalid name or does not exist")
                    continue
                else:
                    print("\n--------------")
                    print("Diet:\n\tMeal frequency: {}\n\tNutritional Balance:\n\t\tProtein: {}\n\t\tFat: {}".format(master_list[index_value][1], master_list[index_value][2], master_list[index_value][3]))

                    print("\n--------------")
                    print("Exercise:\n\tWalk(s): {}\n\tPlay time: {}".format(master_list[index_value][4], master_list[index_value][5]))

                    print("\n--------------")
                    print("Health:\n\tVaccines taken: {}\n\tInjury reports: {}".format(master_list[index_value][6], master_list[index_value][7]))
                    break
        elif menu_choice == "3":
        #The pet a) takes no more than 1 meal; AND b) has high fat AND low protein
            #master list 0-3
            pet_counter=0
            weird_diet=[]
        #MEALS - PROTEIN - FAT
            for i in master_list:
                if int(i[1])<2 and i[2]=="Low" and i[3]=="High":
                    pet_counter+=1
                    i[0]=i[0].strip()
                    weird_diet.append(i[0:4])

            print("\n--------------")
            print("The number of pets with abnormal diet conditions: {}".format(pet_counter))
            for i in weird_diet:
                print("\t{}:\n\t Meal: {}, Protein: {}, Fat: {}".format(i[0], i[1], i[2], i[3]))
        elif menu_choice == "4":
            name_and_time = top_exercise(exercise, names)
            name_and_time.sort(key=lambda x: x[1], reverse=True)
            print("\n--------------")
            for i in range(5):
                name = name_and_time[i][0]
                total = name_and_time[i][1]
                print("{}: {}".format(name, total))
        elif menu_choice == "5":
            health_list = health_info(names, health)
            Burns=[]
            Bites=[]
            Cuts=[]
            Scratches=[]
            for i in health_list:
                if i[2].strip() in injury_lst:
                    if i[2]=="Burn":
                        Burns.append(i[0].strip())
                    elif i[2]=="Bite":
                        Bites.append(i[0].strip())
                    elif i[2]=="Cut":
                        Cuts.append(i[0].strip())
                    elif i[2]=="Scratch":
                        Scratches.append(i[0].strip())
            Burns.sort()
            Bites.sort()
            Cuts.sort()
            Scratches.sort()
            burns_list=", ".join(Burns)
            bites_list=", ".join(Bites)
            cuts_list=", ".join(Cuts)
            scratches_list=", ".join(Scratches)
            print("\n--------------")
            print("{}: {}".format("Burn", burns_list))
            print("{}: {}".format("Bite", bites_list))
            print("{}: {}".format("Cut", cuts_list))
            print("{}: {}".format("Scratch", scratches_list))
        elif menu_choice == "6":
            health_list = health_info(names, health)
            valid_char = "01234"
            while True:
                vaccine_num=input("\n:~Enter the vaccine number ~:")
                if vaccine_num in valid_char:
                    break
                else:
                    print("Invalid input")
                    continue
            pet_num=vaccine_count(health_list, vaccine_num)
            print("Number of pet(s): {}".format(pet_num))
        elif menu_choice == "7":
            score_list = top_exercise(exercise, names)

            for i, line in enumerate(master_list):
                if int(line[6]) > 0:
                    score_list[i][1]=score_list[i][1]+int(line[6])*10
                else:
                    score_list[i][1]+=-10

            for i, line in enumerate(master_list):
                if int(line[1]) > 0:
                    score_list[i][1]=score_list[i][1]+int(line[1])*10
                else:
                    score_list[i][1]+=-10

            for i, line in enumerate(master_list):
                if line[7]=="None":
                    score_list[i][1]+=10
                else:
                    score_list[i][1]-=10

            for i, line in enumerate(master_list):
                if line[2]=="Low":
                    score_list[i][1]-=10
                elif line[2]=="Mid":
                    score_list[i][1]+=10
                else:
                    score_list[i][1]+=20

            for i, line in enumerate(master_list):
                if line[3]=="Low":
                    score_list[i][1]+=20
                elif line[3]=="Mid":
                    score_list[i][1]+=10
                else:
                    score_list[i][1]-=10
        # this format: [name, diet[0]and[1]and[2], exercise[0]and[1], and health[0]and[1]
            score_list.sort(key=lambda x: x[1], reverse=True)
            print("\n--------------")
            for i in score_list:
                print("\t{}: {}".format(i[0], i[1]))








# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()