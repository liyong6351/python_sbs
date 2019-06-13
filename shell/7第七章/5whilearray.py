unconfirmed_users=["lily","lucy","jim"]
confirmed_users=[]
while unconfirmed_users:
    user=unconfirmed_users.pop()
    print("Verify the user:" + user)
    confirmed_users.append(user)

print(confirmed_users)

pets=["dog","cat","dog","rabbit","cat"]
for value in pets:
    print(value)
print("------set-------")
for value in set(pets):
    print(value)

while 'dog' in pets:
    pets.remove('dog')

print(pets)

responses={}
active=True
while active:
    name=input("input the name:")
    response=input("input the response:")
    responses[name]=response
    repeat=input("do you need repeat?")
    if repeat == 'n':
        active = False

print(responses)