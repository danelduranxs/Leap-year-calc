print()
año = int(input("Ingresa un año de la historia:"))


if año%4 == 0 and año%100 > 0 and año>0:
    print()
    print("El año", año ,"D.C es un año bisiesto.")
    
elif año%100 ==0 and año%400==0 and año>0: 
    print()
    print("El año", año ,"D.C es un año bisiesto.")
    

elif año%4 == 0 and año%100 > 0 and año<0:
    print()
    print("El año", año *-1 ,"A.C es un año bisiesto.")    
    

elif año%100 ==0 and año%400==0 and año<0: 
    print()
    print("El año", año*-1 ,"A.C es un año bisiesto.")
    
else:
    if año<0:
        print()
        print("El año", año*-1 ,"A.C no es un año bisiesto.")
        
    elif año >0 :
        print()
        print("El año", año ,"D.C no es un año bisiesto.")


