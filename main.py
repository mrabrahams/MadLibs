# # learning string concatenation by creating a madlib
# print("some string " + variable)
# print("some string {}".format(variable))
# print(f"some string {variable}") <-- preferred method


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because " \
         f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

