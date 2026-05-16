import concurrent.futures
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Disable warnings for unverified HTTPS requests

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/PhantomCrawler'

VERSION = '0.0.1'

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

banner = r'''                                                                                                   
┏┓┓           ┏┓       ┓    
┃┃┣┓┏┓┏┓╋┏┓┏┳┓┃ ┏┓┏┓┓┏┏┃┏┓┏┓
┣┛┛┗┗┻┛┗┗┗┛┛┗┗┗┛┛ ┗┻┗┻┛┗┗ ┛                
Test website behaviour under varied proxy configurations.       
'''


def print_banners():
    print(f'{C}{banner}{W}\n')
    print(f'{G}[+] {Y}Version      : {W}{VERSION}')
    print(f'{G}[+] {Y}Created By   : {W}Spyboy')
    print(f'{G} ╰➤ {Y}Twitter      : {W}{twitter_url}')
    print(f'{G} ╰➤ {Y}Discord      : {W}{discord}')
    print(f'{G} ╰➤ {Y}Website      : {W}{website}')
    print(f'{G} ╰➤ {Y}Blog         : {W}{blog}')
    print(f'{G} ╰➤ {Y}Github       : {W}{github}\n')


print_banners()


# Function to read proxy IPs from a file
def read_proxy_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


# Get user input for website URL
website_url = input(f"{R}Enter the website URL: {W}")

# Get user input for the proxy list file
proxy_file_path = input(f"{R}Enter the path to the proxy list file: {W}")  # valid_proxy.txt

# Read proxy list from the specified file
proxies = read_proxy_list(proxy_file_path)


def visit_link(proxy, website_url, link):
    try:
        absolute_link = requests.compat.urljoin(website_url, link)
        with requests.get(absolute_link, proxies=proxy, timeout=5) as response:
            response.raise_for_status()
            print(f"{C}Proxy {proxy['http']} - {G}Visiting: {absolute_link}")
    except requests.exceptions.RequestException:
        print(f"{R}Error with proxy {proxy['http']}{Y}")


# Make requests concurrently using threading
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for proxy_info in proxies:
        proxy_info = proxy_info.strip()
        if not proxy_info:
            continue

        try:
            parsed = urlparse(proxy_info)
            protocol = parsed.scheme
            ip_port = parsed.netloc

            if not protocol:
                protocol = "http"
                ip_port = proxy_info

            proxy_url = f"{protocol}://{ip_port}"
            proxy = {
                "http": proxy_url,
                "https": proxy_url
            }
            
            # set verify=False to ignore SSL certificate errors
            with requests.get(website_url, proxies=proxy, timeout=5, verify=False) as response:
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')

                links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

                for link in links:
                    futures.append(executor.submit(visit_link, proxy, website_url, link))
                    
        except requests.exceptions.RequestException as e:
            print(f"{R}Error with proxy {proxy_url} {Y}: {e}")
        except Exception as parser_error:
            print(f"{R}Error parsing line '{proxy_info}': {parser_error}")

    concurrent.futures.wait(futures)
