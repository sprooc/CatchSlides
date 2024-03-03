from funcs.info import *
from NJUlogin import pwdLogin  # 向大神致敬！！！
class GetSlides:
  def get_slides(abs_loc):
    pass
  def login_selearning():
    dest = 'https://selearning.nju.edu.cn/login/index.php?authCAS=CAS'
    mobile_headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2007J1SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 cpdaily/9.0.15 wisedu/9.0.15'
    }
    pwdlogin = pwdLogin(username, password)
    session = pwdlogin.login(dest)
    return pwdlogin