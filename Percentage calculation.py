print("Enter the average of the marks obtained in 4 subjects")

maths=int(input("maths:"))
english=int(input("english:"))
ss=int(input("social studies:"))
science=int(input("science:"))

sum=maths+english+ss+science
print("sum of maths, english, ss, and science:", sum)

perc=(sum/400)*100
print(end="Percentage Mark=")
print(perc)