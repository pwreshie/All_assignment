#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from datetime import datetime as dt
import random as rd
from collections import Counter


# In[2]:


hours = [9, 10, 11, 12, 13, 14, 15, 16, 17]
sales = [3459.00, 54290.99, 23444.00, 453299.99, 35099.00, 78442.50, 45113.00, 674000.00, 49834.00]


# In[3]:


##scatter plot


# In[4]:


plt.scatter(hours, sales)

plt.title("A scatter plot of sales during opening hours")
plt.xlabel("hours")
plt.ylabel("sales")

plt.show()


# In[5]:


plt.rcParams["figure.figsize"] = [10, 6]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


##line plot


# In[7]:


plt.plot(hours, sales, color = "red", linewidth = 4, alpha = 0.6)

plt.title("Flow of sales across the day")
plt.xlabel("hours")
plt.ylabel("sales")

plt.show()


# In[ ]:





# In[8]:


data = pd.read_csv("slippo.csv")
data.head()


# In[9]:


data.set_index(pd.Index([num for num in range(1, len(data) + 1)]), inplace = True)


# In[10]:


data.head()


# In[11]:


data["Date"] = data["Date"].apply(lambda a : dt.strptime(a, "%d-%m-%Y"))


# In[12]:


data["Month"] = data["Date"]


# In[13]:


data.head()


# In[14]:


data["Month"] = data["Month"].apply(lambda a : a.strftime("%b"))


# In[15]:


data.head()


# In[16]:


data.tail()


# In[17]:


needed_df = pd.DataFrame(data.groupby("Month")["Sales"].sum()).reset_index()
needed_df


# In[18]:


needed_df["Month"] = needed_df["Month"].apply(lambda a : dt.strptime(a, "%b"))


# In[19]:


needed_df.head()


# In[20]:


needed_df.sort_values(by = "Month", inplace = True)


# In[21]:


needed_df.head()


# In[22]:


needed_df["Month"] = needed_df["Month"].apply(lambda a : a.strftime("%b"))


# In[23]:


needed_df.head()


# In[24]:


slippo_x = needed_df["Month"].to_list()
slippo_y = needed_df["Sales"].to_list()


# In[25]:


####time to plot!!!

plt.plot(slippo_x, slippo_y, linewidth = 6, color = "k", alpha = 0.7)

plt.title("Flow sales across the months")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
# plt.plot


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


xyz_data = needed_df.copy()
xyz_data.head()


# In[27]:


extracted_sales = xyz_data["Sales"].to_list()
rd.seed(77)
rd.shuffle(extracted_sales)


# In[28]:


extracted_sales


# In[29]:


## temporay cell
# quick = [45, 4, 6, 7]
# rd.seed(0)
# pick = rd.choice(quick)

# pick


# In[30]:


xyz_data["Sales"] = extracted_sales


# In[31]:


xyz_data.head()


# In[32]:


needed_df.head()


# In[33]:


xyz_x = xyz_data["Month"]
xyz_y = xyz_data["Sales"]


# In[34]:


###multi-line plot

plt.plot(slippo_x, slippo_y, linewidth = 2, alpha = 0.82, color = "blue", label = "slippo")
plt.plot(xyz_x, xyz_y, linewidth = 2, alpha = 0.73, color = "black", label = "xyz")

plt.title("Comparism flow of sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend(loc = "best", shadow = True)
plt.show()


# In[35]:


needed_df.head()


# In[36]:


###bar chart


# In[ ]:





# In[ ]:





# In[37]:


all_colors = ["blue", "pink", "orange", "green", "cyan", "purple", "brown", "yellow", "brown", "indigo", "grey"]


# In[38]:


plt.bar(slippo_x, slippo_y, width = 0.6, color = all_colors)
plt.show()


# In[39]:


plt.bar(slippo_x, slippo_y, width = 0.6, color = all_colors[:  11])

plt.title("Sales volume by month")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:


new_data = pd.read_csv("Ecom Expense.csv")
new_data.head()


# In[41]:


b = pd.DataFrame(new_data["City Tier"].value_counts()).reset_index()


# In[42]:


extracted_tier = b["index"].to_list()
extracted_tier


# In[43]:


extracted_count = b["City Tier"].to_list()
extracted_count


# In[44]:


plt.bar(extracted_tier, extracted_count, width = 0.5, color = all_colors[2: 8: 2])

plt.title("Population spread of each City Tier")
plt.xlabel("City Tier")
plt.ylabel("Count")

for index, value in enumerate(extracted_count):
    plt.text(x = index, y = value + 13, s = f"{value}")

plt.show()


# In[45]:


smart_group = pd.DataFrame(new_data.groupby("Gender")["City Tier"].value_counts())
smart_group


# In[46]:


Counter(zip(new_data["City Tier"], new_data["Gender"]))


# In[47]:


left_position = smart_group["City Tier"].to_list()[:3]
right_position = smart_group["City Tier"].to_list()[:3]


# In[48]:


##side-by-side bar chart


# In[49]:


indices = np.arange(3)

plt.bar(indices - 0.3, left_position, width = 0.3, color = "blue", label = "Female")
plt.bar(indices, right_position, width = 0.3, color = "black", label = "Male")
plt.xticks(indices - 0.15, extracted_tier)


plt.title("Tier By Gender")
plt.xlabel("City Tier")
plt.ylabel("Count")

plt.legend(loc = "best", shadow = True)
plt.show()


# In[50]:


##Assignment 8


# In[51]:


b = pd.DataFrame(new_data["City Tier"].value_counts()).reset_index()


# In[52]:


Counter(zip(new_data["City Tier"], new_data["Gender"]))


# In[53]:


extracted_tier = b["index"].to_list()
extracted_tier


# In[54]:


indices = np.arange(3)

plt.bar(indices - 0.3, left_position, width = 0.3, color = "yellow", label = "Female")
plt.bar(indices, right_position, width = 0.3, color = "black", label = "Male")
plt.xticks(indices - 0.15, extracted_tier)


plt.title("Population Spread By Gender")
plt.xlabel("City Tier")
plt.ylabel("Count")

plt.legend(loc = "best", shadow = True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[55]:


###stacked bar chart


# In[56]:


plt.bar(extracted_tier, smart_group["City Tier"].to_list()[:3], color = "blue", width = 0.3, label = "Female")
plt.bar(extracted_tier, smart_group["City Tier"].to_list()[3:], color = "black", width = 0.3, label = "Male", bottom = smart_group["City Tier"].to_list()[:3])


plt.title("Stacked bar chart by Gender")
plt.xlabel("City Tier")
plt.ylabel("Count")

plt.legend(loc = "best", shadow = True)
plt.savefig("Stacked_guy.png")


# In[ ]:





# In[57]:


plt.rcParams["figure.figsize"]= [12, 8]


# In[ ]:





# In[58]:


###pie chart


# In[59]:


plt.pie(extracted_count, labels = extracted_tier, radius = 1.5, colors = all_colors[2:8], autopct = "%0.2f%%", explode = [0.2, 0, 0])

plt.show()


# In[ ]:





# In[60]:


plt.pie(needed_df["Sales"], labels = needed_df["Month"], radius = 1.5, autopct = "%0.2f%%", explode = [0,0,0,0,0,0,0,0,0.1,0,0])

plt.show()


# In[ ]:





# In[61]:


fig, axs = plt.subplots(1, 3, figsize = (20, 6))

plot1 = axs[0]
plot2 = axs[1]
plot3 = axs[2]


# In[62]:


###assignment 9


# In[63]:


fig, axs = plt.subplots(2, 2, figsize = (20, 6))


plot1 = axs[0, 0]
plot2 = axs[0, 1]
plot3 = axs[1, 0]
plot4 = axs[1, 1]

plot1.plot(xyz_x[:4], xyz_y[:4], linewidth = 1, color = "magenta", alpha = 0.7)
plot1.set_title("1st quarter sales report")

plot2.plot(xyz_x[4:7], xyz_y[4:7], linewidth = 1, color = "magenta", alpha = 0.7)
plot2.set_title("2nd quarter sales report")

plot3.plot(xyz_x[7:10], xyz_y[7:10], linewidth = 1, color = "magenta", alpha = 0.7)
plot3.set_title("3rd quarter sales report")

plot4.plot(xyz_x[-2:], xyz_y[-2:], linewidth = 1, color = "magenta", alpha = 0.7)
plot4.set_title("4th quarter sales report")


# In[ ]:





# In[64]:


Counter(zip(new_data["City Tier"], new_data["Gender"]))


# In[65]:


Counter(new_data["Gender"])


# In[66]:


1162/(1162+1200) * 815/(815+782+765)


# In[67]:


Counter(new_data["City Tier"])


# In[68]:


815/(815+782+765)


# In[69]:


(1200/2362) * (782/2362)


# In[70]:


0.1682008602190626/(782/2362)


# In[ ]:





# In[ ]:





# In[71]:


##Assignment 


# In[72]:


a = "/Users/User/Documents/lotofdata"


# In[73]:


##append filename into a list_of_files

list_of_files = []

for i in range(1,333):
    if i >= 100:
        list_of_files.append(f"{a}{i}.csv")
    elif i >= 10:
        list_of_files.append(f"{a}0{i}.csv")
    else:
        list_of_files.append(f"{a}00{i}.csv")


# In[74]:


list_of_files


# In[75]:


###create a generator to yeild from file iterator

def open_file(fnames):
    for fname in fnames:
        with open(fname) as f:
            yield from f


# In[76]:


###initialize generator

gen = open_file(list_of_files)


# In[ ]:





# In[ ]:





# In[77]:


output = (4500 - new_data["Total Spend"].mean()) / new_data["Total Spend"].std()
output


# In[78]:


output1 = (6000 - new_data["Total Spend"].mean()) / new_data["Total Spend"].std()
output1


# In[79]:


output2 = (8000 - new_data["Total Spend"].mean()) / new_data["Total Spend"].std()
output2


# In[80]:


##t-test


# In[ ]:


from scipy.stats import ttest_ind


# In[ ]:


new_data.columns


# In[ ]:


ttest_ind(new_data["Monthly Income"], new_data["Transaction Time"])


# In[ ]:


new_data.rename(columns = {"Age " : "Age" }, inplace = True)


# In[ ]:


new_data.rename(columns = {" Items " : "Items" }, inplace = True)


# In[ ]:


ttest_ind(new_data.Age, new_data.Items)


# In[ ]:


fem_only = new_data[new_data["Gender"] == "Female"]
mal_only = new_data[new_data["Gender"] == "Male"]


# In[ ]:


ttest_ind(fem_only["Total Spend"], mal_only["Total Spend"])


# In[ ]:


###chi square


# In[ ]:


from scipy.stats import chi2_contingency as chi


# In[ ]:


chi(pd.crosstab(new_data["Gender"], new_data["City Tier"]))


# In[ ]:





# In[ ]:


###one way ANOVA


# In[ ]:


from scipy.stats import f_oneway


# In[ ]:


tier_one = new_data[new_data["City Tier"] == "Tier 1"]
tier_two = new_data[new_data["City Tier"] == "Tier 2"]
tier_three = new_data[new_data["City Tier"] == "Tier 3"]


# In[ ]:


f_oneway(tier_one["Total Spend"], tier_two["Total Spend"], tier_three["Total Spend"])


# In[ ]:





# In[ ]:


###correlation


# In[ ]:


empty_guy = pd.DataFrame()
empty_guy["top"] = (new_data["Monthly Income"] - new_data["Monthly Income"].mean()) * (new_data["Total Spend"] - new_data["Total Spend"].mean())
empty_guy["bottom_left"] = (new_data["Monthly Income"] - new_data["Monthly Income"].mean()) ** 2
empty_guy["bottom_right"] = (new_data["Total Spend"] - new_data["Total Spend"].mean()) ** 2
topall = empty_guy["top"].sum()
bottomleftsum = empty_guy["bottom_left"].sum()
bottomrightsum = empty_guy["bottom_right"].sum()
bottomall = (bottomleftsum * bottomrightsum) ** 0.5

output = topall / bottomall
output


# In[ ]:


def my_correlation(col_1, col_2):
    var_x, var_y = col_1 - col_1.mean(), col_2 - col_2.mean()
    numerator = (var_x * var_y).sum()
    denominator = ((var_x ** 2).sum() * (var_y ** 2).sum()) ** 0.5
    return numerator / denominator


# In[ ]:


my_correlation(new_data["Monthly Income"], new_data["Total Spend"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




