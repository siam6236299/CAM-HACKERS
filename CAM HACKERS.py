import requests
import re

# AUTHOR: SIAM ISLAM
AUTHOR = "SIAM ISLAM"

# optional: big ASCII banner if pyfiglet is installed
try:
    import pyfiglet
    def make_banner(text):
        return pyfiglet.figlet_format(text)
except Exception:
    def make_banner(text):
        # fallback simple big-ish text
        return "\n" + " " * 4 + text + "\n"

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# print big red banner
banner = make_banner("CAM HACKER")
print(RED + banner + RESET)

# print author line
print(RED + f"AUTHOR: {AUTHOR}" + RESET)

# your original logic
country_code = input("Enter Country Code:")
url = f"http://www.insecam.org/en/bycountry/{country_code}/"
headers = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Accept-Language': 'en-US;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1'
}

res = requests.get(url, headers=headers)
find_ip = re.findall(r'http://\d+\.\d+\.\d+\.\d+:\d+', res.text)

# print each found IP in green
for ip in find_ip:
    print(GREEN + ip + RESET)