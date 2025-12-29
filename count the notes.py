Amount=int(input("Please enter Amount for withdrawl"))

note1=Amount//500
note2=(Amount%500)//200
note3=((Amount%500)%200)//100

print("Number of 500 ruppee notes", note1)
print("Number of 200 ruppee notes", note2)
print("Number of 100 ruppee notes", note3)
