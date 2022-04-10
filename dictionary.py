dictionary={'Name':'Varsha','Age':18,'state':'Tamil nadu','graduate':'1st year BCA'}
x=('name','age','state','graduate')
y=0
dict1=dict.fromkeys(x,y)
print(dict1)
print(dictionary)
print("Getting Name",dictionary.get("Name"))
print("printing items of dictionary\n",dictionary.items())
print("printing the keys of the dictonary\n",dictionary.keys())
print("removing state for the dictionary\n",dictionary.pop("state"),"\n",dictionary)
print("printing the values in the dictionary\n",dictionary.values())
print("clearing the dictionary\n",dictionary.clear())
