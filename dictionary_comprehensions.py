def main():
    # One way to do things
    # dictionary = {}
    # for i in range(1, 101):
    #     if(i % 3 != 0):
    #         dictionary[i] = i**3

    # A new way! Dictionary comprehensions
    # Must be read from 2 -> 3 -> 1
    # { (key: value) (for value in iterable) (if condition) }
    # dictionary = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(dictionary)

    # Challenge
    dictionary = { i: round(i**0.5, 2) for i in range(1, 1001) }
    print(dictionary)

if __name__ == '__main__':
    main()