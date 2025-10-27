sub1=int (input("enter marks for subject 1:"))
sub2=int(input("enter marks for sub 2:"))
sub3=int (input("enter marks for sub 3:"))
sub4=int(input("enter marks for subject 4:"))
sub5=int(input("enter marks for subject 5:"))
sum=sub1+sub2+sub3+sub4+sub5
print("total=",sum)
average=sum/5
if(average>80):
 print("Avearge grade=","mastery")

elif (average<=70):
 print("Average grade=""proficient")
elif (average<=60):
 print("Average grade=""credit")
elif (average>=50):
 print("Average grade=""competent")
else:
 print("Average grade=""not yet competent")