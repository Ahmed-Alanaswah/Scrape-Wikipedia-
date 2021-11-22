import requests
URL='https://en.wikipedia.org/wiki/History_of_Mexico'


from bs4 import BeautifulSoup

res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
def get_citations_needed_count(URL):
   
    citationNeeded= soup.find_all('a',title="Wikipedia:Citation needed")
    return len(citationNeeded)

Arr=[]
def get_citations_needed_report(URL):
   
    citationNeeded= soup.find_all('a',title="Wikipedia:Citation needed")
    for i in citationNeeded:
        Arr.append(i.parent.parent.parent.get_text())

    return "\n".join(Arr)

print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))