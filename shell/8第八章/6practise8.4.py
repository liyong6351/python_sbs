def show_magics(magics):    
    while magics:
        magic = "the Greate " + magics.pop()
        print(magic)

def make_pizza(*material):
    print(material)

magics=["lilei","hmm","lily","lucy","jim"]

show_magics(magics[:])
print(magics)
show_magics(magics)
print(magics)

make_pizza("nihao","shijie","","黄昏")

