#mutable vs. immutable
'''
Mutable objects: list,dict,byte,array,etc.
'''
a = [1,1]
print("a:{}".format(a))
print("id(a) is:{}".format(id(a)))
print("")
#e.g. 53148688

b = [1,1]
print("b:{}".format(b))
print("id(b) is:{}".format(id(b)))
print("")
#e.g. 53148608

print("a is b?:{}".format(a is b))
print("------")
#False


'''
Immutable objects: int,float,string,tuple,etc.
'''
a = 1
print("a:{}".format(a))
print("id(a) is:{}".format(id(a)))
print("")
#e.g. 2042444032

b = 1
print("b:{}".format(b))
print("id(b) is:{}".format(id(b)))
print("")
#e.g. 2042444032

print("a is b?:{}".format(a is b))	     
#True

