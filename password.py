def EMAILVERIFY(email, password):
    email = str(email)
    password = str(password)
    if not "@" in email:
        return "Please format this correctly stupid"
    if len(password) < 8:
        return "Please enter a longer password"
    if any(char.isupper() for char in password) == False:
        return("Please add an uppercase letter")
    
    return {
        "Email": email,
        "Password": password
    }

     


y = input('email: ')
x = input('password: ')

print(EMAILVERIFY(y, x))

