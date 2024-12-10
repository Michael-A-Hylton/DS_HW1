# ---------------------------------------
# CIS 492, Intro to Data Science
# Homework 1: GPA Calculator
# Michael Hylton
# Last Modified: September 07, 2024
# ---------------------------------------
# Takes any number of student classes less
# then 7 and gives their GPA based on inputed grades
# ---------------------------------------

def main():
    while True:
        numOfClasses=0
        try:
            numOfClasses=int(input("Enter the number of courses you are takeing: "))
        except:
            print("Please input a valid input")
        if numOfClasses>=1 and numOfClasses<=7:
            break
        else:
            print("Please choose a number between one and seven\n")
    #input number of classes
     
    avgGPA=float(1.0)
    prevTotalCreds=float(0)
    i=1
    while i<=(numOfClasses) and i<=7:
        #i is the number of current class
        while True:
            currentGrade=input("\nEnter grade for course %d: " %i)
            
            
            #next, we need to convert the letter grade to a gpa value
            if(currentGrade=="A" or currentGrade=="a"):
                currentGPA=float(4.0)
                break
            elif(currentGrade=="A-" or currentGrade=="a-"):
                currentGPA=float(3.7)
                break
            elif(currentGrade=="B+" or currentGrade=="b+"):
                currentGPA=float(3.3)
                break
            elif(currentGrade=="B" or currentGrade=="b"):
                currentGPA=float(3.0)
                break
            elif(currentGrade=="B-" or currentGrade=="b-"):
                currentGPA=float(2.7)
                break
            elif(currentGrade=="C+" or currentGrade=="c+"):
                currentGPA=float(2.3)
                break
            elif(currentGrade=="C" or currentGrade=="c"):
                currentGPA=float(2.00)
                break
            elif(currentGrade=="C-" or currentGrade=="c-"):
                currentGPA=float(1.7)
                break
            elif(currentGrade=="D+" or currentGrade=="d+"):
                currentGPA=float(1.3)
                break
            elif(currentGrade=="D" or currentGrade=="d"):
                currentGPA=float(1.0)
                break
            elif(currentGrade=="F" or currentGrade=="f"):
                currentGPA=float(0.0)
                break
            else:
                print("Please type a letter grade between A and F")
        
        while True:
            currentCredits=0
            try:
                currentCredits=int(input("\nEnter Credits for course %d: " %i))
            except:
                print("Invalid input")
            if currentCredits>0 and currentCredits<6:
                break
            else:
                print("Please insert a whole number between 1 and 5\n")
        
        
        avgGPA=((avgGPA*prevTotalCreds)+(currentGPA*float(currentCredits)))/(prevTotalCreds + float(currentCredits))
        #((1*0)+(3.7*4.0))/(0+4)
        prevTotalCreds=prevTotalCreds+float(currentCredits)
        #0+4
        i=i+1
        
        
    print("Your GPA is %.2f" % avgGPA)

 
if __name__=="__main__":
    main()
