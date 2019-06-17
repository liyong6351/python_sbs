with open('data/pi_digits.txt') as file_object:
    lines=file_object.readlines()

pi=""
for content in lines:
    pi += content.strip()
    print(content.rstrip())

print(pi)
print(pi[:15])
print("nihao")

if '19851028' in pi:
    print("in")
else:
    print("not in")