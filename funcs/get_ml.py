import requests
import re
import os
import zipfile

from GetSlideClass import GetSlides
from requests.auth import HTTPBasicAuth

class GetSlidesML(GetSlides):
    def get_slides(abs_loc):
        url = 'https://www.lamda.nju.edu.cn/ML2024Spring/'
        username = 'ML2024'
        password = 'ML@NJU2024'
        session = requests.Session()
        session.auth = HTTPBasicAuth(username, password)
        response = session.get(url)
        print(response.text)


GetSlidesML.get_slides("./")
