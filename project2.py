import csv

#(A)
def tempBelow17C():
    # This function returns the number of times the temperature fell below 17 degrees Celcius
    
    with open('Data.csv', 'r') as csv_file:     #reads in the data file and stores it under the variable name "csv".
        csv_reader = csv.reader(csv_file)       #stores tabular data in to plain text to make it easier for viewing 
        next(csv_reader)
        
        num_of_times = 0                        #creating a variable with initial value of zero, it represents th number of times the temp fell below 17
        for line in csv_reader:                 #Iterating through each row of the data table
            line = line[1]                      #Here, I i create a variable "line" and in it, I store the the first index of the table (meaning the temperatures column)
            temp = int((line[0:2]))             #Here, I use slicing to remove the "C" after each temp to ensure I'm only working with integers
            if temp < 17:                       #If the temperature falls below 17
                num_of_times =  num_of_times + 1#Then the variable is added by 1, so whenever the temp is below 17 it adds 1 to the variable and in the end prints out the total
        print ("The temperature was recorded below 17C: ", num_of_times, "times!") #Here, I'm printing out the variable along with some string formatting to make it more readible
        return                                  #Exiting the function

#(B)
def tempAbove24C():
    #This function returns the number of times the temperature rose above 24 degrees Celcius
    with open('Data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        num_of_times = 0
        for line in csv_reader:
            line = line[1]
            temp = int((line[0:2]))             
            if temp  > 24:                      #If the temperature rises above 24
                num_of_times =  num_of_times + 1 #same as above but this time it adds 1 whenever the temp rises above 24
        print ("The temperature was recorded above 24C: ", num_of_times, "times!") #same as above
        return                                  #Exiting the function

#(C)
def averageTemperature():
    #This function returns the average temperature
    with open('Data.csv', 'r') as csv_file:     #same as above
        csv_reader = csv.reader(csv_file)       #same as above
        next(csv_reader)

        total = 0                               #I create a variable called "total" with initial value of zero. It will represent the sum of all the temperatures 
        num_of_temps = 0                        #I create a variable called "num_of_temps" with initial val of 0. It will represent the numebr of times a temp was recorded
        for line in csv_reader:                 #Same as above
            num_of_temps += 1                   #Every time i go through each temp in the temperatures column, I add 1 to my variable so it will result in the totla number of temperatures recorded
            line = line[1]                      #same as above
            temp = int((line[0:2]))             #Ssame as above
            total += temp                       #I add the temperature to my "total" variable
            average = total // num_of_temps     # I create a new variable "average" and in it i store the answer of total divided by num_of_temps which is the average!
        print("The total temperature is:",total)#printing out the the sum of all the temps added together
        print("The total number of times a temperature was recorded is:",num_of_temps) # printing out the the number of times the temp was recorded
        print("--------")                       #Just formatting to make the result look nicer
        print("Therefore, the average remperature recorded is: ", average,"Degrees Celcius!") # Finally printing out the average value
        return                                  #Exiting the fucntion




#(D)  
def outsideRange():
    #Calculates the time it takes for the tempeature to fall back into the 24-27 degrees range
    with open('Data.csv', 'r') as csv_file:    #same as part 1 
        csv_reader = csv.reader(csv_file)      #same as part 1
        next(csv_reader)


        for column in csv_reader:              #same as part 1
            time = column[0]                   #Here i index by 0 so that i can take out just the Time colume and focus on it (ignore all other columns)
            temp = column[1]                   #Here i index by 1 so that i can take out just the Temperature colume and focus on it (ignore all....)
            temp1 = int(temp[0:2])             #same as part 1 
            if temp1 < 17 or temp1 > 24:       #If the temperature is outside the operational range
                print("Temp is:",temp1,"therefore", "It will take 30 secs for it to fall back into operational range") #Then i calculate that the it will take 30 secs to fall back into the opeational range
                print("-------------------------------------------------------------------------------------")         #Formatting

            if temp1 >= 17 and temp1 <= 24:    #If the temp is in the range;
                print(temp1,"Is already in range!") #Then just print out the tempeature 
                print("-------------------------------------------------------------------------------------")

            
            


