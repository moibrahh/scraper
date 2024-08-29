from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/acer-vg271u-m3bmiipx-27-wqhd-144hz-using-hdmi-port-180hz-using-display-port-nitro-ips-black/p/N82E16824011467?Item=N82E16824011467&cm_sp=Homepage_SS-_-P4_24-011-467-_-08292024"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify)

prices = doc.find_all(text= "$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)