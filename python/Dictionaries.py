#Dictionary is key-value pairs

d = {'dogs': "cute", 'cat': "furry"}

#value access with key
cat_adj = d['cat']

#check if key in dict
print('cat' in d)

#update key-value
d['dog'] = 'Howie'

#add key-value
d['fish'] = 12

#remove key
del d['fish']

#iterate over key and values
for key, value in d.items():
    print(f"{key} : {value}")
