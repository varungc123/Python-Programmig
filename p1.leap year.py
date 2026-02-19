year=(int(input("Enter year:")))
if (year%100!=0 and year%4==0) or (year%400==0):
    print(f"YES {year} is a leap year")
else:
    print(f"NO {year} is not a leap year")

    #or...........................................................................................

def leapYear(year):
    return (year%100!=0 and year%4==0) or (year%400==0)

year=(int(input("Enter year:")))
flag=leapYear(year)
if flag:
    print(f"wYES {year} is a leap year")
else:
    print(f"wNO {year} is not a leap year")

    #or.........................................................

start=int(input("Enter start year:"))
end=int(input("Enter end year:"))
if (start>end):
    print("inalid")
else:
    for year in range(start, end):
        flag = leapYear(year)
        if flag:
            print(year,end=" ")
        else:
            print(year,end="")