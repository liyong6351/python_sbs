friuts=["apple","orange","pear","bananer"]
print(friuts)
print(friuts[1])
print(len(friuts))
friuts[0]="watermelon"
print(friuts)
friuts.append("grape")
print(friuts)

print("永久性排序")
friuts.sort()
print(friuts)
friuts.sort(reverse=True)
print(friuts)
print("临时性排序")
friuts=["apple","orange","pear","bananer"]
print(friuts)
print(sorted(friuts))
print(friuts)

locations=["c重庆","c成都","w乌鲁木齐","q齐齐哈尔","k昆明"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations,reverse=True))
print(locations)