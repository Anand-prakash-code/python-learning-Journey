a=b=c=100
print(a,b,c) #100 100 100

x,y,z,w=1,2,"python",'python' 
print(x,y,z,w)            # 1 2 python python

del x
print(x) # The del statement removes the variable reference, and the memory is freed only if no other references to the object exist.