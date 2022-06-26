import requests # python3 -m pip install requests beautifulsoup4
from bs4 import BeautifulSoup

laburos = open("laburos.txt", "a")
trabajo = input("Ingresa el trabajo que estás buscando: ").replace(" ", "%20")

print(trabajo)
url = "https://ar.indeed.com/jobs?q="+trabajo+"&"+"l=Argentina"

if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all("div", attrs = {"class": "job_seen_beacon"}) 
for job in results:
    try:
        titleElement = job.find("a", attrs={"class": "jcs-JobTitle"})
        title = titleElement.get_text()
        company = job.find("span", attrs={"class": "companyName"}).get_text()
        joblink = "https://ar.indeed.com" + titleElement["href"]
        salary = job.find("div", attrs={"class": "heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly"})
        salary = salary.get_text() if salary else 'n/a'
            
        job = "\nTitulo: {}\nEmpresa: {}\nSalario: {}\nLink: {}a\n"

        job = job.format(title, company, salary, joblink)
        print(job)
        laburos.write(job)
    except Exception as e:
        print("Exception: {}".format(e))
        pass

laburos.close()