bad_url =  input()
clean_url = ""

for element in bad_url:
    if element != "/":
        clean_url += element
    else:
        if clean_url[-1] != "/":
            clean_url += element 

print(clean_url)

