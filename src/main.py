import random
import string 

class Password:
    def __init__(self, length, include_upp = False, include_num = False, include_especial = False):
      self.length = length
      self.include_upp = include_upp
      self.include_num = include_num
      self.include_especial = include_especial


    def generate_char(self):
        if  random.choice([1,0]) == 1:
            return random.choice(string.ascii_letters)
        elif self.include_upp:
            return  random.choice(string.ascii_letters).upper()
    
    def generate_number(self):
        return random.randint(0, 9)
    
    def generate_special(self):
        SpecialChar = "£$&()*+[]@#^-_!?"
        return random.choice(SpecialChar)

    def set_password(self):
        password = ''
        while True:

            password.join(generate_char())

            if len(password) == self.length:
                return password

def set_options(include_upp, include_num, include_especial, length): 
    return

def main():
    password = Password(7, include_upp= True)

if __name__ == "__main__":
    main()