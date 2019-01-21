#ΕΡΓΑΣΙΑ 1: AΘΡΟΙΣΜΑ ΔΙΑΣΤΗΜΑΤΩΝ
while True:
    arxh = int(input("Dwste thn arxh tou diasthmatos: "))
    telos = int(input("Dwste to telos tou diasthmatos: "))
    list=[[arxh,telos]]
    while True:
	
        print("An oloklhrwsete thn eisagwgh diasthmatwn eisagete duo fores to '0'")
	
        arxh = int(input("Dwste thn arxh tou diasthmatos: "))
        telos = int(input("Dwste to telos tou diasthmatos: "))
	
        if arxh<telos:
            list.append([arxh,telos])
        elif arxh>telos:
            print("Error: Try again!")
        elif arxh==0 and telos==0:        
            break	

    list.sort()

    sum = int(list[0][1]-list[0][0])


    for i in range(1,len(list)):
    
        if list[i][0]>list[i-1][1]:
            sum+= (list[i][1]-list[i][0])
        else:
            if list[i][1]>list[i-1][1]:
                sum= sum + (list[i][1]-list[i-1][1])
		
    print( 'To athroisma tou mhkous twn diasthmatwn einai: ' , sum)
    print("Pieste 'ENTER' gia na ksanadwsete lista.")
    answer=str(input())
    if answer!="": 
        break
    
