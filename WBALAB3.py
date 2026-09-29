balocaname = input("Enter your name: ")
balocamonth = float(input("Enter Month(1-12): "))

if balocamonth >=1 and balocamonth <=3:
    balocaseason = "Rainy"
    balocadetail = "The rainy season is a time to stay home, unwind, and enjoy the comfort and tranquility of cozy indoor moments."
elif balocamonth >=4 and balocamonth <=5:
    balocaseason = "Spring"
    balocadetail = "Many cultures celebrate this lively season with festivals focused on hope and renewal."
elif balocamonth >=6 and balocamonth <=8:
    balocaseason = "Summer"
    balocadetail = "A season of warmth, relaxation, and enjoyable moments spent outdoors, making the most of sunny days."
elif balocamonth >= 9 and balocamonth <=12:
    balocaseason = "Christmas Vibe"
    balocadetail = "Winter is a season of calm and comfort, offering cool days, cozy moments indoors, and time to relax and recharge."
else:
    balocaseason = "Invalid"
    balocadetail = "Invalid season"

print(f"Name: {balocaname.title()}")
print(f"Month: {balocamonth}")
print(f"Season: {balocaseason}")
print(f"Description: {balocadetail}")

