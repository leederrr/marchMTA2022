#McKenzie Kelley
#MTA SEARCH

#Function will open file with exception handling, split the file data information, and redirects input given from the opening menu function. 
def main():                                                                                                                                                                                         
    file_data = [] #empty list for data file
    stationnames = ['8 ST-NYU','14 ST-UNION SQ','14 ST','23 ST','28 ST','34 ST-HERALD SQ','34 ST-PENN STA','49 ST','57 ST-7 AV','59 ST','5 AV/59 ST','TIMES SQ-42 ST','PRINCE ST','CANAL ST','SPRING ST','42 ST-PORT AUTH','W 4 ST-WASH SQ']
    dateslist = ['03/01/2022','03/02/2022','03/03/2022','03/04/2022','03/05/2022','03/06/2022','03/07/2022','03/08/2022','03/09/2022','03/10/2022','03/11/2022','03/12/2022','03/13/2022','03/14/2022','03/15/2022','03/16/2022','03/17/2022','03/18/2022','03/19/2022','03/20/2022','03/21/2022','03/22/2022','03/23/2022','03/24/2022','03/25/2022','03/26/2022','03/27/2022','03/28/2022','03/29/2022','03/30/2022','03/31/2022']
    #Try, except IOError, else suite for file exception handling.
    try:
        myfile = open('MarchMTANYC.txt','r')
    except IOError: 
        print("Problem with opening the file.")
    else:
        file_data = []
        line = myfile.readline().rstrip() #Strips the file data by lines.
        
       #Will split the lines of myfiles by commas and strip values, respectively when line is not empty. 
        while line != '':
            file_data.append(line.split(','))
            line = myfile.readline().rstrip()

        #If statements determine what to do from input of opening_menu() function.
        result = opening_menu()
        if result == '1': #If 1 is entered for choice...
            entries_and_exits(file_data, stationnames, dateslist)
        if result == '2': #If 2 is entered for choice...
            print("\n\t~~~~~ Thanks for using the MTA Turnstile Search Program! ~~~~~")
        
#Function serves as an opening menu for the program and determines what to do based off of user input.
def opening_menu():
    print("\t~~~~~ Welcome to the MTA Turnstile Search Program! ~~~~~\n")
    print("1: Search for the entry & exit totals of a given station name and date") #entries_and_exits function
    print("2: End the program\n")

    #User input
    choice = input(f'What option do you choose?: ')
    
    #Validates user choice input. 
    while choice != '1' and choice != '2':
        print("\nThat is not an option!")
        choice = input(f'What option do you choose?: ')
    return choice #Return user input

#Function will look for matching input in the file, index elements from the lists, and output the total counts.
def entries_and_exits(file_data, stationnames, dateslist):
    INDEX = 0 #index for sorting through lines of data
    #Empty lists that will later be appended to:
    entriesdaystart = []
    entriesdayend = []
    exitsdaystart = []
    exitsdayend = []
    times1 = []
    times2 = []

    #User input for station name and date
    mystation = str(input(f'\nWhat is the name of the station? '))
    if mystation not in stationnames:
        print("That is not a valid station name.\nPlease review the station name key and try again.\n")
        return main()
    mydate = str(input(f'What is the date? (mm/dd/yy) '))
    if mydate not in dateslist:
        print("Please review the dates in March 2022 and/or ensure the date is in the mm/dd/yyyy format.\n")
        return main()
    

#While loop to find if index is in the proposed length, then appends elements to various empty lists.
    while INDEX < len(file_data):
        if file_data[INDEX][3] == mystation and file_data[INDEX][6] == mydate:
            entriesdaystart.append(file_data[INDEX][9])
            entriesdayend.append(file_data[INDEX + 1][9])
            exitsdaystart.append(file_data[INDEX][10])
            exitsdayend.append(file_data[INDEX + 1][10])            

            #Converts elements of entry values into integers.
            for x in range(len(entriesdaystart)):
                int(entriesdaystart[x])
            for x in range(len(entriesdayend)):
                int(entriesdayend[x])

            #Converts elements of exit values into integers.
            for x in range(len(entriesdaystart)):
                int(exitsdaystart[x])
            for x in range(len(entriesdayend)):
                int(exitsdayend[x])

        if file_data[INDEX][3] == mystation and file_data[INDEX][6] == mydate:
            times1.append(file_data[INDEX][7])
            times2.append(file_data[INDEX + 1][7])

            for x in range(len(times1)):
                times1a = times1[x]  
            for x in range(len(times1)):
                times2a = times2[x]

            totalentries = int(entriesdayend[x]) - int(entriesdaystart[x]) #Calculation for the overall entry counts (night count minus morning count)
            totalexits = int(exitsdayend[x]) - int(exitsdaystart[x]) #Calculation for the overall exit counts (night count minus morning count)

            #Output to user:
            print(f'\nDescription of {mystation} Station on {mydate} from {times1a} to {times2a}\n')
            print(f'Total Turnstile Entries: {totalentries}')
            print(f'Total Turnstile Exits: {totalexits}')
        INDEX += 2 #Index for sorting through to the next lines.
            
                   
main() #Calls the main function.
