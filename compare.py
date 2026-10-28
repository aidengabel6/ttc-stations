def minimum(value_a, value_b):
    """Returns the lesser of value_a and value_b"""
    if value_a < value_b:
        return value_a
    else:
        return value_b

def main():
    print ("minimum of 1 and 2 is",minimum(1,2))
    print(minimum(2,1) == 1)
    print(minimum(2,2) == 2)

if __name__ == "__main__":
    main()