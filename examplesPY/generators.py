#!/usr/bin/python3

"""THIS THE CODE TO CREATE A GENERATO"""
def generarpares(limit):
    num = 1

    while num<limit:
        yield num * 2
        num += 1

def main():
    emmus = generarpares(9)
    print(next(emmus))

if __name__ == '__main__':
    main()
