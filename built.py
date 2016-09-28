__author__ = 'BackOffice-3'
import builtwith

url = input("Enter url")
website = builtwith.parse(url)
print(website)


if website['cms'] == ['WordPress']:
    print("True", url)
else:
    print("False")


for key, value in website.items():
    print(key + ":",", ".join(value))







