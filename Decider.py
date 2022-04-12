import random
print("Do you really need a decider?")
choiceList=[]
def decider():
    global choiceList
    input_First=input("\nEnter the first option\n")
    input_Second=input("\nEnter the second option\n") #Since there should be at least 2 options to decide
    input_More=input("\nWant to add more option? (y/n)") #Only takes y into account, anything else goes false

    i=3 #starts from 3 because first 2 inputs are above
    input_Extra={} #dictionary to take variable input names
    choiceList=[input_First,input_Second]

    while(input_More.lower()=="y"):
        input_Extra[i]=input("\nEnter the %s. option.\n" % i)
        choiceList.append(input_Extra[i])
        i+=1
        input_More=input("\nWant to add more option? (y/n)")
    i-=1 #to make i value equal to input count

    #check inputs in between
    #print("\n1. input is",input_First,"\n2. input is",input_Second)
    #for k in range(3,i+1):
    #    print("\n%s. input is"%k,input_Extra[k])
    #check inputs in between
    print("\n",random.choice(choiceList))
decider()
inputRollAgain=input("\nPress * to run again, anything to exit. ")
while inputRollAgain=="*":
    print("\n",random.choice(choiceList))
    inputRollAgain=input("\nPress * to run again, anything to exit. ")
