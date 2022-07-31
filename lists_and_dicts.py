def main():
    my_list = [1, "Hell", True, 4.5];
    my_dict = { "firstName": "Facundo", "lastName": "Gordillo" }

    super_list = [
        my_dict,
        { "newThing": "toAdd" }
    ]

    super_dict = {
        "my_dict": my_dict,
        "my_list": my_list
    }

    print("SUPER LIST", super_list)

    print("SUPER DICT")
    for key, value in super_dict.items():
        print("key:", key, "| value:", value)


if __name__ == '__main__':
    main()