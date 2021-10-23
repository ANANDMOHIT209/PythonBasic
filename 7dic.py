data={1:'Shailee',4:'Mohit',3:'Sneha'}
print(data[4])
x=data.get(1,'Not found')
y=data.get(2,'Not found')
print(x)
print(y)

#merging list in dictionary

keys=['Mohit','Sneha','Shailee']
value=['20','18','23']
data=dict(zip(keys,value))
print(data)

#add
data['abc']='67'
print(data)
del data['abc']
print(data)
 