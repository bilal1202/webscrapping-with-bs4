#!/usr/bin/env python
# coding: utf-8

# # web-scrapping
# 
# Use the "Run" button to execute the code.

# In[1]:



   
import requests #this module is used for making request build for humans
import bs4  #python most popular library for webscrappig also known as beautfiulsoup

#this res shows the request and .get is used to parse the html of website in ""
res = requests.get("https://www.geeksforgeeks.org/python-programming-language/?ref=shm") 
#print(type(res))
#print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(type(soup))
#print(soup.prettify())



print ("------------------------------------------------------------------------------------------------------------")
print("|                                                    WEBSCRAPPER                                            |")
print ("------------------------------------------------------------------------------------------------------------")


print("+  Select any one of the given options to run the various functions of WEBSCRAPPER ")
print("***********************************************************************************")
print("0.See the title of the page")
print("1.See all the headlines of the page")
print("2.See all the images source")
print("3.See all the text available on the page")
print("4.See all the links in the pages.")
print("5.See the sidebar on the page")
print("6.See one of the navigation bar on the page")

#asking the user to enter the choice for performing actions

print("Enter the choice : ")
a = int(input(">"))

if a == 0:
	title_text = soup.select('title')
	# print(title_text)
	print(title_text[0].getText())
	# print(soup.p['class']) #to check the class of pararapgh tag
elif a == 1:
	headlines = soup.select('.mw-headline')
	# print(headlines)
	# print(headlines[0].get_text())  # will give only one headline

	for item in headlines:
		print(item.text)


elif a == 2:
	images = soup.find_all('img')
	# print(images)

	for item_images in images:
		print(item_images['src']+ '\n')



elif a == 3:
	text1 = soup.find_all('p')

	for item_text in text1:
		print(item_text.text)




elif a == 4:
	for link in soup.find_all('a'):
		print(link.get('href'))


elif a == 5:
	side_bar = soup.find_all('li')
	# print(side_bar)

	for item_side_bar in side_bar:
		print(item_side_bar.text)


elif a == 6:
	tag_heading = soup.select('h2 > span ')

	for item_tag_heading in tag_heading:
		print(item_tag_heading.text)
	print("========================================================================================")

	tag_heading_content = soup.select('.toctext')
	# print(tag_heading_content)

	for item_tag_heading_content in tag_heading_content:
		print(item_tag_heading_content.text)



# In[ ]:





# In[ ]:





# In[ ]:




