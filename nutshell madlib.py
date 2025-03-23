def custom_song(noun1, adjective1, noun2, verb, place, emotion, noun3, adjective2):
    print("\n\n")
    print(f"And if I can't be my own {noun1},")
    print(f"I feel {adjective1} and {emotion}.")
    print(f"To {verb} in a {place} of {noun2},")
    print(f"With a {noun3} that's {adjective2} and torn.")
    print()
    print(f"Yet I find myself in this {place},")
    print(f"Where the {noun2} is {adjective1} and worn.")
    print(f"And the {noun3} that once was {adjective2},")
    print(f"Now feels {emotion} and forlorn.")
input_noun1 = input("Enter a noun:")
input_adjective1 = input("Enter an adjective:")
input_noun2 = input("Enter another noun:")
input_verb = input("Enter a verb:")
input_place = input("Enter a place:")
input_emotion = input("Enter an emotion:")
input_noun3 = input("Enter a third noun:")
input_adjective2 = input("Enter another adjective:")
custom_song(
    noun1=input_noun1,
    adjective1=input_adjective1,
    noun2=input_noun2,
    verb=input_verb,
    place=input_place,
    emotion=input_emotion,
    noun3=input_noun3,
    adjective2=input_adjective2
)