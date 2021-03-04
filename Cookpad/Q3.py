import requests

recipe1 = requests.get('https://static.cookpad.com/hr/screen/category-1.json').json()
recipe2 = requests.get('https://static.cookpad.com/hr/screen/category-2.json').json()
list1 = recipe1['subcategories'][0]['subcategories']
list2 = recipe2['subcategories'][0]['subcategories']
print(list1)
print(list2)
print(list1+list2)
