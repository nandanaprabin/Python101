#program to do some basic conversions
while True:
    print("\nCONVERSIONS\n\n1:Celcius to Farenheit\n2:Kilometers to miles\n3:Days to weeks\n4:Kilograms to pounds\n5:Hours to minutes\n6:Exit\n")
    i=int(input("Enter your choice: "))
    if i==1:
        c=float(input("Enter temperature in Celcius: "))
        f=(c*9/5)+32
        print(c,"degree Celcius is",f,"Farenheit")
    elif i==2:
        km=float(input("Enter the distance in Kilometers: "))
        miles=km*0.621371
        miles=round(miles,2)
        print(km,"Kilometers is",miles,"Miles")
    elif i==3:
        days=int(input("Enter the number of days: "))
        weeks=days/7
        weeks=round(weeks,2)
        print(days,"days is",weeks,"weeks")
    elif i==4:
        kg=float(input("Enter the weight in Kilograms: "))
        pound=kg* 2.20462
        pound= round(pound,2)
        print(kg,"Kilogram is",pound,"pounds")
    elif i==5:
        hours=int(input("Enter the time in hours: "))
        minutes=hours*60
        print(hours,"hours is",minutes,"minutes")
    elif i==6:
        exit(0)
    else:
        print("Invalid choice")