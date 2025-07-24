
ItemsInCart = 0

if ItemsInCart != 2:    #raise Exception("product count not match")

    pass

#assert (ItemsInCart == 2)   # will throw an assertion error


try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("somehow i reached this block as there is failure in try block")

