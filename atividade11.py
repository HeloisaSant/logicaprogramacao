

lista= [2,4,8,16,32]

print( str.join('---', map (lambda x: x > 2 and x < 6 , filter(lambda x: x > 2 and x < 6 , lista))))
