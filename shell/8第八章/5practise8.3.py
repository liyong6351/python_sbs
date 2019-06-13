def city_country(city="重庆",country="中国"):
    return str(city) + "." + str(country)

def make_ablum(singer="李志",book="300万"):
    result={}
    result["singer"]=singer
    result["book"]=book
    return result

print(city_country("成都"))
print(city_country())
print(city_country("芝加哥","美国"))


print(make_ablum("许巍","那一年"))
print(make_ablum("beyond","真的见证"))
print(make_ablum())

active=True
books=[]
while active:
    singer=input("please input singer:")
    book=input("please input book:")
    if singer == 'q':
        active=False
        continue
    books.append(make_ablum(singer,book))
print(books)