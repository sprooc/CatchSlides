from funcs.GetSlideClass import GetSlides
from funcs import get_SE2, get_os, get_db
if __name__=='__main__':
  abs_loc = "./"
  for sub_class in GetSlides.__subclasses__():
    print(sub_class.__name__)
    sub_class.get_slides(abs_loc)
