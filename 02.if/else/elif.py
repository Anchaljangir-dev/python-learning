sub1 = int(input("enter your marks:"))
sub2 = int(input("enter your marks:"))
sub3 = int(input("enter your marks:"))
total_percentage = ((sub1+sub2+sub3)/300)*100
if total_percentage>90:
    grade = "A"
elif total_percentage>70:
    grade = "B"
elif total_percentage>60:
    grade = "C"
else:
    grade = "D"

print(grade , total_percentage)