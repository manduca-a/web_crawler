

PhantomCrawler is a security testing and research tool that simulates website interactions from different proxy IP addresses to analyze how websites behave under varied network and geolocation conditions.

**Features:**
- Utilizes a list of proxy IP addresses from a specified file.
- Supports both HTTP and HTTPS proxies.
- Allows users to input the target website URL, proxy file path, and a static port.
- Makes HTTP requests to the specified website using each proxy.
- Parses HTML content to extract and visit links on the webpage.

**Usage:**
- **POC Testing:** Simulate website interactions to assess functionality under different proxy setups.
- **Traffic Behavior Testing:** Analyze how websites respond to requests originating from different IP addresses and network locations.
- **Proxy Rotation Testing:** Evaluate the effectiveness of rotating proxy IPs.
- **Web Scraping Testing:** Assess web scraping tasks under different proxy configurations.
- **DDoS Awareness:** Caution: The tool has the potential for misuse as a DDoS tool. Ensure responsible and ethical use.

⚠️ **Get New Proxies** with port and add in `proxies.txt` in this format `protocol://50.168.163.176:80`

- You can add it from here: https://free-proxy-list.net/ these free proxies are not validated some might not work so first validate these proxies before adding.

**How to Use:**
1. Clone the repository:
   
2. Install dependencies:
   
```
pip3 install -r requirements.txt
```

3. Run the script to check proxies validity:

```
python3 proxy_checking.py
```

4. Run the Crawler 
```
python3 PhantomCrawler.py
```

5. Insert your URL

6. Insert path to your proxies list

```
proxies.txt
```


**Disclaimer:**
PhantomCrawler is intended for educational and testing purposes only. Users are cautioned against any misuse, including potential DDoS activities. Always ensure compliance with the terms of service of websites being tested and adhere to ethical standards.

---
