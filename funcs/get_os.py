import requests
import re
import os

from funcs.GetSlideClass import GetSlides


class GetSlidesOS(GetSlides):
    def get_slides(abs_loc):
        base_loc = abs_loc + "Spring2024//ComputerOperatingSystem//slides//"
        if not os.path.exists(base_loc):
            os.makedirs(base_loc)
        pwdlogin = GetSlides.login_selearning()
        url = 'https://selearning.nju.edu.cn/course/view.php?id=156'
        response = pwdlogin.get(url)
        module_numbers = re.findall(
            r'<li class="activity resource modtype_resource " id="module-(\d+)', response.content.decode("UTF-8"))
        module_names = re.findall(
            r'<span class="instancename">(.{1,30})<span class="accesshide " > 文件</span>', response.content.decode("UTF-8"))
        for id, name in zip(module_numbers, module_names):
            slide_url = 'https://selearning.nju.edu.cn/mod/resource/view.php?id=' + id
            slide_response = pwdlogin.get(slide_url)
            slide_loc = base_loc + name + ".pdf"
            if os.path.exists(slide_loc):
                continue
            open(slide_loc, 'wb').write(slide_response.content)