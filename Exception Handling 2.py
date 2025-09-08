def vote(age):
    if age <18:
        raise ValueError("Invalid age")
    return "You are eligible to vote"
try:
    print(vote(18))
    print(vote(17))
except ValueError as e:
    print(e)