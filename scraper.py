from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import urllib.request

req = Request("https://www.ragasurabhi.com/carnatic-music/ragas.html")
html_page = urlopen(req)

soup = BeautifulSoup(html_page)

# https://www.ragasurabhi.com/carnatic-music-mp3/raga-nayaki-signature.mp3

for link in soup.findAll('a'):
    if("/raga/" in link.get('href')):
        raga_name="_".join(link.string.split(" ")).lower()
        signature_file_path = f"https://www.ragasurabhi.com/carnatic-music-mp3/raga-{raga_name}-signature.mp3"
        urllib.request.urlretrieve(signature_file_path, f"{raga_name}_signature.mp3")