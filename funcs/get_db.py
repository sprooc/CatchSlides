import requests
import re
import os
import zipfile

from funcs.GetSlideClass import GetSlides


class GetSlidesDB(GetSlides):
    def get_slides(abs_loc):
        base_loc = abs_loc + "Spring2024//DatabaseManagement//slides//"
        if not os.path.exists(base_loc):
            os.makedirs(base_loc)
        pwdlogin = GetSlides.login_selearning()
        url = 'https://selearning.nju.edu.cn/course/view.php?id=154'
        response = pwdlogin.get(url)
        module_folders = re.findall(
            r'href="https://selearning.nju.edu.cn/mod/folder/view.php\?id=(\d+)">', response.content.decode("UTF-8"))
        session_key = re.search(
            r'sesskey=(.{1,10})"', response.content.decode("UTF-8")).group(1)
        chinese_numbers = ["一", "二", "三",
                           "四", "五", "六", "七", "八", "九", "十"]
        chap = 0
        for folder_id in module_folders:
            data = {'id': folder_id, 'sesskey': session_key}
            folder_url = 'https://selearning.nju.edu.cn/mod/folder/download_folder.php'
            slide_response = pwdlogin.post(folder_url, data=data)
            slide_loc = base_loc + "第" + chinese_numbers[chap] + "章" + ".zip"
            chap += 1
            if os.path.exists(slide_loc):
                continue
            open(slide_loc, 'wb').write(slide_response.content)
            with zipfile.ZipFile(slide_loc, 'r') as zip_ref:
                zip_ref.extractall(slide_loc[0: -4])
            os.remove(slide_loc)


