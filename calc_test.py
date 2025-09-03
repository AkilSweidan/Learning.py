from calculator import sqaure


def main():
    test_sqaure()
    


def test_sqaure():
    if sqaure(2) != 4 :
        print("Test 2 Failed")
    if sqaure(3) != 9 :
        print("Test 3 Failed")
    if sqaure(4) != 16 :
        print("Test 4 Failed")
    if sqaure(5) != 25 :
        print("Test 5 Failed")
    if sqaure(6) != 36 :
        print("Test 6 Failed")

    else : 
        print("All Tests Passed")

if __name__ == "__main__":
    main()