from bs4 import BeautifulSoup
import requests
import csv

headers = requests.utils.default_headers()


##scraping in disguise##
headers.update({
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
})

results = []

for i in range(1,51):
    
    url1 = f'https://www.jumia.com.ng/smartphones/?page={i}#catalog-listing'

    url2 = 'https://www.jumia.com.ng/smartphones/'
    
    if i == 1:
        url = url2
    else:
        url = url1

    my_response = requests.get(url, headers)

    child_soup = BeautifulSoup(my_response.content, features = "lxml")

    # print(child_soup)

    first_search = child_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})

    # print(first_search.prettify())

    second_search = first_search.find_all('article', attrs = {"class" : "prd _fb col c-prd"})

    new_file = open("C:/Users/User/Desktop/jumia_smartphones.csv",mode = "w", encoding = "utf-8", newline = "")

    pen = csv.writer(new_file)

    ##the header 
    pen.writerow(["phone brand", "specifications", "old price", "new price", "phone rating"])
    mined_data = []

    # print(second_search)

    for soup in second_search:
    # print(soup.prettify())

        inner_container = soup.find("a")
    # print(inner_container.prettify())

    ### FOR PHONE BRAND ###
    try:
       phone_brand = inner_container["data-brand"]

    except: 
        phone_brand = None

    ### FOR PHONE SPECIFICATION ###
    try:
       phone_specification = inner_container["data-name"]

    except:
        phone_specification = None

    ### FOR OLD PRICE ###
    try:
        third_search = inner_container.find("div", attrs = {"class" : "old"})

        old_value = third_search.text
        if "," in old_value:
           step_one = old_value.lstrip("₦ ")
           step_two = step_one.replace("," , "")
           old_price = int(step_two)
        else:
            step_one = old_value.lstrip("₦ ")
            old_price = int(step_one)
    except:
        old_price = None

    ## NEW PRICE ##
    try:
        fourth_search = inner_container.find("div", attrs = {"class" : "prc"})
        new_value = fourth_search.text
        if "," in new_value:
          step_one = new_value.lstrip("₦ ")
          step_two = step_one.replace("," , "")
          new_price = int(step_two)
        #   print(new_price)
        else:
            step_one = new_value.lstrip("₦ ")
            old_price = int(step_one)
    except:
        new_price = None


    
    ### FOR RATING ###
    try:
       fifth_search = inner_container.find("div", attrs = {"class" : "stars _s"})
       rating_entry = fifth_search.text
       step_one = rating_entry.split(" out ")[0]
       phone_rating = float(step_one)

       print(phone_rating)

       print(inner_container.prettify())
    except:
       phone_rating = None

    results.append([phone_brand, phone_specification, old_price, new_price, phone_rating])

jumia_data = results
# jumia_data = [(i[10], i[1], i[2], i[4] for i in jumia_data)]

# pen.writerows(results)
# new_file.close()







