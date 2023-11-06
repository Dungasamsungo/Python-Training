print("\nPlease enter the following information\n")

first_name = input("First name: ").capitalize()
last_name = input("Last name: ").capitalize()
email = input("Email address: ").lower()
phone_number = input("Phone number: ")
job_title = input("Job Title: ").capitalize()
id = input("Id: ")
hair = input("Hair color: ").capitalize()
eyes = input("Eyes color: ").capitalize()
month = input("Month: ").capitalize()
status = input("Traning (Yes/No): ").capitalize()



print("\nThe ID Card is:")
print("-------------------------")
print(f"{last_name}, {first_name}\n{job_title}\n{id}\n\n{email}\n{phone_number}")
print(f"Hair: {hair:15} Eyes: {eyes}\nMonht: {month:14} Training: {status} ")
print("-------------------------\n")
