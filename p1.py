import re
def password_strength_checker(password):
    if(len(password)<8):
        return "Weak:password should contain atleast 8 length"
    if not any(ch.isdigit() for ch in password):
        return "Weak:password should contain atleast 1 digit"
    if not any(ch.islower() for ch in password):
        return "Weak:password should contain atleast 1 lower"
    if not any(ch.isupper() for ch in password):
        return "Weak:password should contain atleast 1 upper"
    if not re.search(r'[!@#$%^&*(){}<>,.|]',password):
        return "Medium:Not special character"
    return "String password"
def run():
    while True:
        input1=input("Enter your password or exit to exit");
        if(input1.lower()=="exit"):
            return "exited"
            break
        print(password_strength_checker(input1));
run();

    
