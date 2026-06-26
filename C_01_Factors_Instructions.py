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


 #Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")