# country=open('country.txt',"r")
# print(country.readlines())

# for lines in country.readlines():
#     print(lines)

# country.close()

country=open('country.txt','w')
country.write("hello this is my new file")
country.close()