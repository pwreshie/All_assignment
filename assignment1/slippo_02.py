from datetime import datetime as dt
import csv
import xlwt
from tempfile import TemporaryFile


read_file = open("C:\Users\User\Desktop\Rawfile.txt", mode = 'r', encoding = 'utf-8')

whole_data = read_file.readlines()
print(whole_data[:5])
# print(len(whole_data))

#To clean the data
for num in range(len(whole_data)):
    whole_data[num] = whole_data[num].rstrip("\n")

# print(whole_data[:5])

# To get unique dates
unique_dates = []
for entry in whole_data:
    date = entry.split(" on ")[1]
    if date in unique_dates:
        pass
    else:
        unique_dates.append(date)

# print(unique_dates[:5])

#Sorting the unique dates
sorted_unique_dates = sorted(unique_dates, key = lambda a: dt.strptime(a, "%d-%m-%Y"))
# print(sorted_unique_dates[:20])


#To sort the whole data
sorted_whole_data = []
for date in sorted_unique_dates:
    for entry in whole_data:
        if date == entry.split(" on ")[1]:
            sorted_whole_data.append(entry)
        else:
            pass

# print(sorted_whole_data[:10])


# To unpack the entries
list_of_names = []
list_of_sales = []
list_of_dates = []

for entry in sorted_whole_data:
    extracted_name = entry.split(" : ")[0]
    list_of_names.append(extracted_name)

    extracted_amount = entry.split(" on ")[0].split(" : ")[1]
    refined_amount = int(extracted_amount.lstrip("₦"))
    list_of_sales.append(refined_amount)

    extracted_date = entry.split(" on ")[1]
    list_of_dates.append(extracted_date)


# Writing the sorted whole data to a csv file
new_file = open("C:\Users\User\Desktop\slippo.csv", mode = "w", encoding = "utf_8", newline = "")

pen = csv.writer(new_file)
pen.writerow(["Name", "Sales", "Date"])

for num in range(len(sorted_whole_data)):
    pen.writerow([list_of_names[num], list_of_sales[num], list_of_dates[num]])

new_file.close()




# Preparing data for second sheet
unique_agents = sorted(list(set(list_of_names)))

all_agents_sales = []

for agent in unique_agents:
    agent_sum = 0
    for index, entry in enumerate(list_of_names):
        if agent == entry:
            desired_amount = list_of_sales[index]
            agent_sum += desired_amount
        else:
            pass

    all_agents_sales.append(agent_sum) 


total_revenue = sum(all_agents_sales)

impact_list = [(entry/ total_revenue) * 100 for entry in all_agents_sales]

commission_list = [0.045 * entry for entry in all_agents_sales]


#preparing third sheet
total_revenue = sum(all_agents_sales)

total_commission = sum(commission_list)

profit = total_revenue - total_commission




#writing to an excel book
book = xlwt.Workbook()

first_sheet = book.add_sheet("All Transactions")
second_sheet = book.add_sheet("Agent's Transactions")
third_sheet = book.add_sheet("Financial Statement")


#writing into first sheet
first_sheet.write(0,0, "Name")
first_sheet.write(0,1, "Sales")
first_sheet.write(0,2, "Date")


for index, entry in enumerate(list_of_names):
    first_sheet.write(index + 1, 0, entry)

for index, entry in enumerate(list_of_sales):
    first_sheet.write(index +1, 1, entry)

for index, entry in enumerate(list_of_dates):
    first_sheet.write(index +1, 2, entry)


#Writing into second sheet
second_sheet.write(0,0, "Agent name")
second_sheet.write(0,1, "Agent sales")
second_sheet.write(0,2, "Impact")
second_sheet.write(0,3, "Commission")

for index, entry in enumerate(unique_agents):
    second_sheet.write(index +1, 0, entry)

for index, entry in enumerate(all_agents_sales):
    second_sheet.write(index +1, 1, entry)

for index, entry in enumerate(impact_list):
    second_sheet.write(index +1, 2, "{0:.2f}%".format(entry))

for index, entry in enumerate(commission_list):
    second_sheet.write(index +1, 3, entry)


#Writing into the third sheet
third_sheet.write(0,0, "Total Revenue")
third_sheet.write(0,1, "Total Commission")
third_sheet.write(0,2, "Profit")

third_sheet.write(1,0, total_revenue)
third_sheet.write(1,1, total_commission)
third_sheet.write(1,2, profit)

#saving the book in excel
book.save("C:\Users\User\Desktop\slippo_excel.xls")
book.save(TemporaryFile())