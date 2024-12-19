class SubfieldsinAI():
    def Subfields():
        print("Sub-fields in AI are:")
        List=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for i in List:
            print(i)
    def OddEven():
        N=int(input("Enter a Number:"))
        if(N%2==0):
            print(N,"is Even Number")
            message=N,"is Even Numner"
        else:
            print(N,"is Odd Number")
            message=N,"is Odd Number"
        return message
        
    def Marriageeligible():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<21):
            print("NOT ELIGIBLE")
            message="Not Eligible"
        else:
            print("ELIGIBLE")
        return message
    def percentage():
        s1=int(input("Subject1="))
        s2=int(input("Subject2="))
        s3=int(input("Subject3="))
        s4=int(input("Subject4="))
        s5=int(input("Subject5="))
        Total = s1+s2+s3+s4+s5
        print("Total=",Total)
        percentage = (Total/500)*100
        print("Percentage=",percentage)
        message=percentage
        return message
    def Triange():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        Area =(h*b)/2
        print(Area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter=h1+h2+b1
        print("Perimeter of Triangle:",Perimeter)
        message=Perimeter
        return message