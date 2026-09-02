def gen():
    for i in range(5):
        yield i


g=gen()
print(g[0])