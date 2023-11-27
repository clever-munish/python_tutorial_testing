# two list or two set any two thing which can be itrated

l1 = ["Munish", "Rohit", "Mohit"]
l2 = ["JS", "Pyhton", "Java"]
l3 = ["India", "AUS", "USA"]

for a in l1:
    # uneasted loop
    for b in l2:
        for c in l3:
            print(a + " " + b + " " + c)
