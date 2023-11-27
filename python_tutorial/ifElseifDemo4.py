#Boolean variable for status
status=False

#for loop for list

names=["Pyhton","JAVA,""JS"]
for name in names:

    if name=="JAVA":
        status=True
        break
    else:
        print("please wait we are sill sarching")

if status:
    print("we are glad that we found the record")
else:
    print("sorry we could not found the record")
