## Dependencies
from bs4 import BeautifulSoup 
import requests

## Header files for the browser. Needed for passing the header data for making a successful query
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

## --------------- Method for searching -----------------
def search(query):
    ## Replace the spaces with '+' for browser URL encoding
    query = query.replace(" ","+")

    ## Handling Error Cases if no internet connection is present
    try:
        ## f-string url for typical google search with query
        ## --------------------------------------here is the query --------
        url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'

        ## requests function for downloading files (if no error)
        res = requests.get(url,headers=headers)

        ## bs4 function for parsing the data in html DOM model
        soup = BeautifulSoup(res.text,'html.parser')
    except:
        ## No Internet Error
        print("Make sure you have a internet connection")

    ## Handling the error cases and looking in for different result classes
    try:
        try:
            ## bs4 method for selecting a class (.RqBzHd in our case). Then getText() is called to get content of the class element
            ## and strip is use to delete the whitespaces (if any)
            ans = soup.select('.RqBzHd')[0].getText().strip()
        
        except:
            try:
                ## one of the google classes that stores title and content in different element
                title=soup.select('.AZCkJd')[0].getText().strip()
                try:
                    ans=soup.select('.e24Kjd')[0].getText().strip()
                except:
                    ans=""
                ## f-string for the title and answer i.e. result
                ans=f'{title}\n{ans}'
                
            except:
                ## Refer the above select method explanation
                try:
                    ans=soup.select('.hgKElc')[0].getText().strip()
                except:
                    ans=soup.select('.kno-rdesc span')[0].getText().strip()
    ## If not find in any of the classes return inconvinience message
    except:
        ans = "Sorry. Can't find on google"
    ## Return the answer
    return ans


## ----------------- BODY --------------------
## Asks for input that is passed into the above function and is stored into result var
result = search(str(input("Your question:\n")))
## prints result
print(result)
