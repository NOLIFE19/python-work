name = input("enter your name?")
lastname = input("enter yout lastname?")
platform = input("choose email? gmail.com?, itstep.ge?, yahoo.com?")



name_x=name.strip()
lastname_y = lastname.strip()

#ამოღება  ორი  პირველი ასოსიur team:saba.ananidze@itstep.com,dima123@gmail.com,test_user@yahoo.com
firstandsecond = name[:2]

print(firstandsecond)

# მესამე ნაწილი

fullemail=f"{firstandsecond}{lastname}@{platform}"

print(fullemail)
print()
print()
print("Your email has been successfully created!")
# მეოთხე ნაწილი

import re

text="Our team members are: saba.ananidze@itstep.com, our friend Dima dima123@gmail.com, and one more test email address test_user@yahoo.com."
y =re.findall(r"@\w+", text)

result = "+".join(y)

print(result)