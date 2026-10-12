def outer():
    name="hi"
    def inner():
        print(name)

    return inner

res=outer()
res()

