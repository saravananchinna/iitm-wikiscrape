from http.server import BaseHTTPRequestHandler
import urllib.parse
import json
import httpx
from bs4 import BeautifulSoup

class handler(BaseHTTPRequestHandler):

    def htmlToMark(htmlTag,text):
        result=""
        number = htmlTag[2:3]
        for i in range(int(number)):
            result=result+'#'
        result=result+" "+text
        print (result)
        return result
    
    def do_GET(self):

        query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()

        country=""
        for queryParam in query_params:
            print(queryParam)
            if (queryParam=="country"):
                country = query_params.get("country")[0]
        print(country)

        try:
            print('indise of try block')
            response = httpx.get("https://en.wikipedia.org/wiki/"+country,follow_redirects=True)
            if response.status_code==200:
                print(response.status_code) 
                # print(response.text)  

                html= response.text

                headerTagString = ""
                soup = BeautifulSoup(html, "html.parser")   
                for heading in soup.find_all(['h1', 'h2','h3','h4','h5','h6']):
                    # print(heading)
                    print(str(heading.text))
                    finalText= handler.htmlToMark(str(heading),heading.text)
                    
                    headerTagString= headerTagString+str(finalText)+"\n"
    
        except:
            print('sonething wrong')
        self.wfile.write(headerTagString.encode('utf-8'))

        return 
    
    