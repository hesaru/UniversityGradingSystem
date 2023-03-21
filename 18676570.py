# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210726 / 18676570
# Date: 8/12/2021

#Necessary global lists
histo_list          =   []  #To append outputs for the user inputs
progress            =   []  #To append stars to print histogram
trailing            =   []  #To append stars to print histogram
retriever           =   []  #To append stars to print histogram
excluded            =   []  #To append stars to print histogram
inputs              =   []  #To append user input values
histo_list_save     =   []  #To append outputs for the user inputs for the purpose of text file creation
inputs_save         =   []  #To append user input values for the purpose of text file creation
continuity          =   ""  #Initial value for the continu function

#Code for the main menu
def main_menu():
    print("\nMain Menu\nContinue with,\n \n1   -Staff Version \n2   -Student Version\nq   -Quit")
    print("-----------------------------------------------------------------------------------------------------------")
    main_men_inp = str(input("Choose option: "))
    if main_men_inp == "1":
        menue()
    elif main_men_inp =="2":
        print("Student Version\n")
        inp_func_std()
        main_menu()
    elif main_men_inp == "q":
        exit()
    else:
        print("Wrong Input!")
        main_menu()

#Code for the staff version menue
def menue():
    print("-----------------------------------------------------------------------------------------------------------")
    print("Staff Version Menu")
    print("")
    print("1-   Add Inputs \n2-   Horizontal Histogram \n3-   Vertical Histogram \n4-   List of Last Inputs \n5-   View History \n6-   Clear History \
    \n7-   Main Menu \nq-   Exit")
    print("-----------------------------------------------------------------------------------------------------------")
    men_inp = input("Choose option: ")
    men_inp = men_inp.lower()
    print("")
    print("-----------------------------------------------------------------------------------------------------------")
    print("")
    if men_inp == "1":
        inp_func()
        menue()
    if men_inp == "2":
        if histo_list == []:
            print("Staff version with histogram\n")
            inp_func()
            histogram(histo_list)
            staff_version(progress, trailing, retriever, excluded)
            list_print(histo_list, inputs)
            menue()
        else:
            need_new = continu("Do you want to add new data before the histogram representation?(y/n) :","y","n")
            if need_new == "y":
                inp_func()
                histogram(histo_list)
                staff_version(progress, trailing, retriever, excluded)
                list_print(histo_list, inputs)
                menue()
            elif need_new == "n":
                histogram(histo_list)
                staff_version(progress, trailing, retriever, excluded)
                list_print(histo_list, inputs)
                menue()
    if men_inp == "3":
        if histo_list == []:
            inp_func()
            histogram(histo_list)
            vertical_histogram(progress, trailing, retriever, excluded)
            list_print(histo_list, inputs)
            menue()
        else:
            need_new = continu("Do you want to add new data before the histogram representation?(y/n) :","y","n")
            if need_new == "y":
                inp_func()
                histogram(histo_list)
                vertical_histogram(progress, trailing, retriever, excluded)
                list_print(histo_list, inputs)
                menue()
            elif need_new == "n":
                histogram(histo_list)
                vertical_histogram(progress, trailing, retriever, excluded)
                list_print(histo_list, inputs)
                menue()
    if men_inp == "4":
        if histo_list == []:
            inp_func()
            list_print(histo_list,inputs)
        else:
            need_new = continu("Do you want to add new data before the list of inputs representation?(y/n) :","y","n")
            if need_new == "y":
                inp_func()
                list_print(histo_list, inputs)
            elif need_new == "n":
                list_print(histo_list,inputs)
    if men_inp == "5":
        history()
        menue()
    if men_inp == "6":
        sure = continu("Do you really want to clear the History and Delete the \"data_file.txt\"?(y/n) :","y","n")
        if sure == "y":
            memory = open('data_file.txt', 'w')
            memory.close()
            print("History and \"data_file.txt\" Deleted!")
            menue()
        else:
            menue()
    if men_inp == "7":
        main_menu()

    if men_inp == "q":
        exit()
    else:
        print("Wrong input!")
        menue()


#Code for the user inputs and inputs validation
def inp_func():
    try:
        pas_t = int(input("\nPlease enter your credits at pass:"))
        if (pas_t <= 120) & (pas_t % 20 == 0) & (pas_t >= 0):

            defer_t = int(input("Please enter your credit at defer:"))
            if (defer_t <= 120) & (defer_t % 20 == 0) & (defer_t >= 0):

                    fail_t = int(input("Please enter your credit at fail:"))
                    if (fail_t <= 120) & (fail_t % 20 == 0) & (fail_t >= 0):
                            if (pas_t + defer_t + fail_t) != 120:
                                print("Total incorrect")
                                con = continu("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ","y", "q")
                                if con == "y":
                                    inp_func()
                                else:
                                    pass
                            else:
                                print(prog_out(pas_t, defer_t, fail_t))
                                inputs.append((pas_t,defer_t,fail_t))
                                inputs_save.append((pas_t, defer_t, fail_t))
                                histo_list.append(prog_out(pas_t, defer_t, fail_t))
                                histo_list_save.append(prog_out(pas_t, defer_t, fail_t))
                                savefile(histo_list_save,inputs_save)
                                del histo_list_save[:]
                                del inputs_save[:]
                                con = continu("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ","y","q")
                                if con == "y":
                                    inp_func()
                                else:
                                    pass
                    else:
                        print("Out of range")
                        con = continu("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ","y", "q")
                        if con == "y":
                            inp_func()
                        else:
                            pass
            else:
                print("Out of range")
                con = continu("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ","y", "q")
                if con == "y":
                    inp_func()
                else:
                    pass
        else:
            print("Out of range")
            con = continu("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ","y", "q")
            if con == "y":
                inp_func()
            else:
                pass

    except ValueError:
        print("Integer required")
        con = continu("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ","y", "q")
        if con == "y":
            inp_func()
        else:
            pass

#function for the student version inputs
def inp_func_std():
    try:
        pas_t = int(input("\nPlease enter your credits at pass:"))
        if (pas_t <= 120) & (pas_t % 20 == 0) & (pas_t >= 0):

            defer_t = int(input("Please enter your credit at defer:"))
            if (defer_t <= 120) & (defer_t % 20 == 0) & (defer_t >= 0):

                    fail_t = int(input("Please enter your credit at fail:"))
                    if (fail_t <= 120) & (fail_t % 20 == 0) & (fail_t >= 0):
                            if (pas_t + defer_t + fail_t) != 120:
                                print("Total incorrect")
                                main_menu()
                            else:
                                print(prog_out(pas_t, defer_t, fail_t))

                    else:
                        print("Out of range")
                        main_menu()
            else:
                print("Out of range")
                main_menu()
        else:
            print("Out of range")
            main_menu()
    except ValueError:
        print("Integer required")
        main_menu()

#function to determine the criteria which is relevant for an input

def prog_out(pas, defer, fail):
    if (pas == 120) & (defer == 0) & (fail == 0):
        return "Progress"

    elif pas == 100:
        if ((defer == 20) & (fail == 0)) | ((defer == 0) & (fail == 20)):
            return "Progress (module trailer)"

    elif pas == 80:
        if ((defer == 40) & (fail == 0)) | ((defer == 20) & (fail == 20)) | ((defer == 0) & (fail == 40)):
            return "Module retriever"

    elif pas == 60:
        if ((defer == 60) & (fail == 0)) | ((defer == 40) & (fail == 20)) | ((defer == 20) & (fail == 40)) | \
                ((defer == 0) & (fail == 60)):
            return "Module retriever"

    elif pas == 40:
        if ((defer == 80) & (fail == 0)) | ((defer == 60) & (fail == 20)) | ((defer == 40) & (fail == 40)) | \
                ((defer == 20) & (fail == 60)):
            return "Module retriever"
        elif (defer == 0) & (fail == 80):
            return "Exclude"

    elif pas == 20:
        if ((defer == 100) & (fail == 0)) | ((defer == 80) & (defer == 20)) | ((defer == 60) & (fail == 40)) | \
                ((defer == 40) & (fail == 60)):
            return "Module retriever"
        elif ((defer == 20) & (fail == 80)) | ((defer == 0) & (fail == 100)):
            return "Exclude"

    elif pas == 0:
        if ((defer == 120) & (fail == 0)) | ((defer == 100) & (fail == 20)) | ((defer == 80) & (fail == 40)) | \
                ((defer == 60) & (fail == 60)):
            return "Module retriever"
        elif ((defer == 40) & (fail == 80)) | ((defer == 20) & (fail == 100)) | ((defer == 0) & (fail == 120)):
            return "Exclude"


#Function for the histogram "*" elements lists creation (for both normal and vertical histogram)

def histogram(entered_list):
    for val in histo_list:
        if val == "Progress":
            progress.append("*")
        elif val == "Progress (module trailer)":
            trailing.append("*")
        elif val == "Module retriever":
            retriever.append("*")
        else:
            excluded.append("*")


#function for the staff version histogram printing

def staff_version(progress, trailing, retriever, excluded):
    print("-----------------------------------------------------------------------------------------------------------")
    print("Horizontal Histogram")
    print("Progress ", len(progress), "    : ", *progress)
    print("Trailer ", len(trailing), "     : ", *trailing)
    print("Retriever ", len(retriever), "   : ", *retriever)
    print("Excluded ", len(excluded), "    : ", *excluded)
    tot_items = len(progress) + len(trailing) + len(retriever) + len(excluded)
    print(tot_items, " outcomes in total.")
    progress.clear()
    trailing.clear()
    retriever.clear()
    excluded.clear()
    print("-----------------------------------------------------------------------------------------------------------")

#function for the vertical histogram printing

def vertical_histogram(progress, trailing, retriever, excluded):
    print(
        "------------------------------------------------------------------------------------------------------------")
    print("Progress Trailing Retriever Excluded ")

    trial = [len(progress), len(trailing), len(retriever), len(excluded)]
    #To avoid the error of exceeding the elements of lists all lists get append blank spaces until it reachs the no of \
    # elements of the largest lists length
    tot_items = len(progress) + len(trailing) + len(retriever) + len(excluded)
    elements = (max(trial))
    progress_temp = progress
    trailing_temp = trailing
    retriever_temp = retriever
    excluded_temp = excluded

    while len(progress_temp) < elements:
        progress_temp.append(" ")

    while len(trailing_temp) < elements:
        trailing_temp.append(" ")

    while len(retriever_temp) < elements:
        retriever_temp.append(" ")

    while len(excluded_temp) < elements:
        excluded_temp.append(" ")

    for val in range(elements):
        print("  ", *progress_temp[val], "      ", *trailing_temp[val], "       ", *retriever_temp[val], "      ",
              *excluded_temp[val])

    print(tot_items, " outcomes in total.")
    progress.clear()
    trailing.clear()
    retriever.clear()
    excluded.clear()

#function for the list format
def list_print(histo_list,inputs):
    print("\n-----------------------------------------------------------------------------------------------------------")
    for val in range(len(histo_list)):
        print(histo_list[val],end = " - ")
        print(inputs[val])
    menue()

# function for continuity (y = option1 q= option2)
def continu(message,option1,option2):
    """Function for the continuity choice
    Call with
    continuity variable, prompt question as a string,choice1,choice2"""
    cont_inp = input(message)
    cont_inp = cont_inp.lower()
    while (cont_inp != option1) and (cont_inp != option2):
        print("wrong input")
        cont_inp = input(message)
        cont_inp= cont_inp.lower()
    if cont_inp == option1:
        return option1
    else:
        return option2

#Function to create or update the data files of inputs
def savefile (histo_list_save,inputs_save):
    import os
    memory = open('data_file.txt', 'a')
    for val in range(len(histo_list_save)):
        memory.write(str(histo_list_save[val]))
        memory.write(" - ")
        memory.write(str(inputs_save[val])+"\n")
    memory.close()


#function to read data files
def history():
    import os
    if os.path.exists('data_file.txt'):
        memory = open('data_file.txt','r')
        line = memory.readlines()
        memory.close()
        for lines in range(len(line)):
            print(str(line[lines])[ :-1])
    else:
        print("History files may be deleted or does not exist!")



#Calling main menu function for the startup of the program
main_menu()
