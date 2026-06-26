#generates headings  (eg: -----heading-----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


#displays instructions
def instructions():
    statement_generator("instructions", "-")

    print("""
Type a integer between 1 and 200
I will show you if it is unity
if it is a prime number
and its factors

    """)


# Asks user for an integer between 1 and 200 (inclusive)
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here

statement_generator("The Ultimate Factor Finder", "-")

 #Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break