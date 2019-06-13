alien_0={"color":"red","point":15}
print(alien_0)
print(alien_0["color"])
print(alien_0["point"])

alien_0["x_point"]=100
alien_0["y_point"]=50
print(alien_0)

del alien_0["point"]
print(alien_0)

print('------practice 6.1---------')
friend={"first_name":"黄","last_name":"华章","age":36,"city":"hz"}
print(friend)

fa_num={"lily":1,"lucy":3,"jim":5,"lilei":7,"hmm":9}
print(fa_num)

la={"C":"difficult","PHP":"most beautiful","java":"my fa","python":"intresting","vb":"past"}
print(la.keys())
for key in la.keys():
    print("language " + str(key) + ":" + la[key])
for key,value in la.items():
    print("key=" + str(key) + ": value=" + str(value))

for key in sorted(la.keys()):
    print("language " + str(key) + ":" + la[key])