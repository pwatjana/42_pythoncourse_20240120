""" Print ticket base on age"""

def age_to_price(age: int) ->int:
    """return the ticket price by age"""
    ADULT_AGE = 18
    SENIOR_AGE = 65

    if age <=0:
        raise ValueError("invalid age")

    if age >= SENIOR_AGE:
        return 200
    elif age >= ADULT_AGE:
        return 250
    elif age < ADULT_AGE:
        return 150
    
def main():
    age = input("How are you?")
    age = int(age)
    price = age_to_price(age)
    print("Price:", price)
    
if __name__ == "__main__":
    main()
# what ever call name.py in terminal , vs will always call __main__
    # call others first file ?

