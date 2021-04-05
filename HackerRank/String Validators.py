if __name__ == '__main__':
    s = input()
    i = s.split()
    
    print(any(i.isalnum() for i in s)) # string are alphanumeric (a-z, A-Z and 0-9).
    print(any(i.isalpha() for i in s)) # string are alphabetical (a-z and A-Z)
    print(any(i.isdigit() for i in s)) # string are digits (0-9).
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
