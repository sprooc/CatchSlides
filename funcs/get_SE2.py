import requests
from funcs.GetSlideClass import GetSlides
import os
class GetSlidesSE(GetSlides):
  def get_slides(abs_loc):
    base_loc = abs_loc + "Spring2024//SoftwareEngineeringAndComputingII//slides//"
    if not os.path.exists(base_loc):
      os.makedirs(base_loc)
    site_url = "https://p.internal-paas.seec.seecoder.cn/api/courseWare/getCourseWaresByCourseId?courseId=7"
    page_response = requests.get(site_url, verify=False)
    for course in page_response.json()["data"]:
      slide_url = course['courseWareVO']['fileUrl']
      slide_loc = base_loc + course['courseWareVO']['name']
      if os.path.exists(slide_loc):
        continue
      slide_response = requests.get(slide_url)
      open(slide_loc, 'wb').write(slide_response.content)