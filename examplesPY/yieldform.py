#!/usr/bin/python3

def yieldform(*listy):

    for elements in listy:
        yield from elements

def main():
    emmus = yieldform("Emmus", "Yeison")
    print(next(emmus))
    print(next(emmus))

if __name__ == '__main__':
    main()
