askname = input("What is your first name and last name?")
    input("Welcome to LondonBookStores",askname)
askbalance = input("What is your current balance: ")
askbalance = int(askbalance)
if askbalance < 10:
    print(askname,"Your balance is low, you may want to top it up")

elif askbalance < 50:
    print(askname,"You will want to put more credit into your account before you run out!")

elif askbalance < 100:
    print(askname,", You have enough credit to last you the month!")

elif askbalance < 250:
    print(askname, "You have enough credit to last you the following month!")

else:
    print(askname, "You have enough to last you 3 months and more!")
