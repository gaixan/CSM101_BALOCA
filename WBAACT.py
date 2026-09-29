balocaname = input("What is your name: ")
balocamonth = int(input("Enter Month: "))
balocaday = int(input("Enter Birth Day: "))

if (balocamonth == 1 and balocaday <= 20) or (balocamonth == 2 and balocaday <= 18):
    print(f"Your Birth day is: January, {balocaday}\nYou are Aquarius.")
elif (balocamonth == 2 and balocaday <= 19) or (balocamonth == 3 and balocaday <= 20):
    print(f"Your Birth day is: February, {balocaday}\nYou are Pisces.")
elif (balocamonth == 3 and balocaday <= 21) or (balocamonth == 4 and balocaday <= 19):
    print(f"Your Birth day is: March, {balocaday}\nYou are Aries.")
elif (balocamonth == 4 and balocaday <= 20) or (balocamonth == 5 and balocaday <= 20):
    print(f"Your Birth day is: April, {balocaday}\nYou are Taurus.")
elif (balocamonth == 5 and balocaday <= 21) or (balocamonth == 6 and balocaday <= 20):
    print(f"Your Birth day is: May, {balocaday}\nYou are Gemini.")
elif (balocamonth == 6 and balocaday <= 21) or (balocamonth == 7 and balocaday <= 22):
    print(f"Your Birth day is: June, {balocaday}\nYou are Cancer.")
elif (balocamonth == 7 and balocaday <= 23) or (balocamonth == 8 and balocaday <= 22):
    print(f"Your Birth day is: July, {balocaday}\nYou are Leo.")
elif (balocamonth == 8 and balocaday <= 23) or (balocamonth == 9 and balocaday <= 22):
    print(f"Your Birth day is: August, {balocaday}\nYou are Virgo.")
elif (balocamonth == 9 and balocaday <= 23) or (balocamonth == 10 and balocaday <= 22):
    print(f"Your Birth day is: September, {balocaday}\nYou are Libra.")
elif (balocamonth == 10 and balocaday <= 23) or (balocamonth == 11 and balocaday <= 21):
    print(f"Your Birth day is: October, {balocaday}\nYou are Scorpio.")
elif (balocamonth == 11 and balocaday <= 22) or (balocamonth == 12 and balocaday <= 21):
    print(f"Your Birth day is: November, {balocaday}\nYou are Sagittarius.")
elif (balocamonth == 12 and balocaday <= 22) or (balocamonth == 1 and balocaday <= 19):
    print(f"Your Birth day is: December, {balocaday}\nYou are Capricorn.")
else:
    print(f"Birth day is invalid.")