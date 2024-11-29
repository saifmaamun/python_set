# add(), copy(), update(), pop(), discard(), remove(), clear()
s1= {5,6,3,8,7,1}
s1.add(78)
print(s1)
s1.add((89,65,10))
print(s1)
s1.update((89,65,10))
print(s1)
s2=s1.copy()
print(s2)
s1.pop()
print(s1)
s1.discard(8)  # if the element is not found it will ignore and not throw an error
print(s1)
s1.remove(78) # if the element is not found it will throw an error
print(s1)
s2.clear()
print(s2)
