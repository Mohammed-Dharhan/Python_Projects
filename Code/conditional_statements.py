hours = int(input("Please input the hours worked: \n"))
rate  = int(input("Please input the rate: \n"))

if(hours > 40):
    extra_hours = hours - 40
    pay =(40 * rate) + (rate * 1.5 * extra_hours)
    print('Your pay is: ', pay)

else:
    print(pay)
