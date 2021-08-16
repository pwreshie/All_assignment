read_file = open("C:\Users\User\Desktop\Rawfile.txt", mode = "r", encoding = "utf-8")

whole_data = read_file.readlines()
print(whole_data[:5])
print(len(whole_data))


##### TO CLEAN THE DATA #####
for num in range(len(whole_data)):
    whole_data[num] = whole_data[num].rstrip("\n")

print(whole_data[:5])



### Month with the highest sales ###
read_file = open("C:\Users\User\Desktop\Rawfile.txt", mode = "r", encoding = "utf-8")
refined_list_date = [dt.strptime(i, '%d-%m-%Y').strftime('%B') for i in list_of_date]
s2 = zip(refined_list_date, list_of_sales)
unsorted_month = {}
for k, v in s2:
    unsorted_month[k] = unsorted_month.get(k, 0) + v
result = sorted(unsorted_month.items(), key=lambda a: a[1])[-1]

###solution###
new_structure = zip(unique_agents, all_agents_sales)
sorted_structure = sorted(new_structure, key = lambda a : a[1], reverse = True)
for guy in sorted_structure[:10]:
    print(guy[0])


