alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
alnum = alpha + num

ctext = 'hereispasswordCTF'

def rotate(s, num):
    new1 = ''
    for c in s:
        if c in alnum:
            new1 += alnum[(alnum.index(c) + num) % 36]
        else:
            new1 += c
    return new1
dtext=rotate(ctext,3)
print dtext
print ("{}".format(rotate(dtext,-3)))

git remote add origin https://github.com/orangeistoxic/the-paradise-of-pyhton.git
 git push -u origin master