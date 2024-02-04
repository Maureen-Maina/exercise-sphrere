# voting program
age = int(input("Enter your age: "))
country = input("Enter your country: ")
eligible_countries = ["Tanzania", "Uganda", "Kenya"]
if age >= 18 and country in ["Tanzania", "Uganda", "Kenya"]:
    print("Eligible")
else:
    age<18 and country not in ("Tanzania", "Uganda", "Kenya")
    print("Not eligible")
