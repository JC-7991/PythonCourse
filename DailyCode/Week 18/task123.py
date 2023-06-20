'''
Given a string, return whether it represents a number. Here are the different kinds of
numbers:
"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:
"a"
"x 1"
"a -2"
"-"
'''

def checkValid(string: str) -> bool:

    is_valid = True
    has_number = False
    num_negatives, num_points, num_e = 0, 0, 0

    for char in string:

        if not (char.isdigit()):
            if char == "-":
                if num_negatives >= 1:
                    
                    if num_negatives == 1 and num_e == 1:
                        num_negatives += 1
                        continue
                    is_valid = False
                    break
                num_negatives += 1
            elif char == ".":
                if num_points >= 1:
                    if num_points == 1 and num_e == 1:
                        num_points += 1
                        continue
                    is_valid = False
                    break
                num_points += 1
            elif char == "e":
                if num_e >= 1:
                    is_valid = False
                    break
                num_e += 1
            elif char == " ":
                pass
            else:
                is_valid = False
                break
        else:
            has_number = True
    return is_valid and has_number


if __name__ == "__main__":

    print(checkValid("10"))
    print(checkValid("-10"))
    print(checkValid("10.1"))
    print(checkValid("-10.1"))
    print(checkValid("1e5"))
    print(checkValid("1e-5"))
    print(checkValid("-1.6 e -5.2"))
    print(checkValid("a"))
    print(checkValid("x 1"))
    print(checkValid("a -2"))
    print(checkValid("-"))