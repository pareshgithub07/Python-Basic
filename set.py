S=set()
print(set)
"""s_form_list = set([1,2,3,4])
print(s_form_list)
print(type(s_form_list))"""

S.add(1)# the set will gives the unic values it will not shows the dublecate values
S.add(1)
S.add(3)
S.add("paresh")
print(S)
S.remove("paresh")#it will removing the element of set which is "paresh"
print(S)

S.add(1)
S.add(3)
S1=S.intersection({1,2,3})# it will gives the same values in available in both sets
print(S,S1)
S1=S.union({1,2,3})
print(S,S1)
