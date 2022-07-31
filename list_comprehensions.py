from operator import mod


def main():
    # One way to do things
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    # A new way! List comprehension
    # Must be read from 2 -> 3 -> 1
    # [(element) (for element in iterable) (if condition)]
    [i**2 for i in range(1, 101) if i % 3 != 0]

    # Challenge
    # challenge_result = [i for i in range(100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    [i for i in range(100000) if i % 36 == 0]


if __name__ == "__main__":
    main()