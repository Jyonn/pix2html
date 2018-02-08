from urllib.parse import urlencode

from selenium import webdriver
from sele import get_tree, get_html


driver = webdriver.Chrome()
driver.set_window_size(1278, 1300)


def grab_dict_baidu():
    with open('characters.txt') as f:
        words = f.readline()
    for index, w in enumerate(words):
        print(index, w)
        filename = 'dictbd%s' % index
        tree = get_tree(driver, 'http://dict.baidu.com/s?%s' % urlencode({'wd': w}), filename)
        get_html(tree, filename)

grab_dict_baidu()
# tree = get_tree(driver, 'http://baidu.com/', 'bd')
# get_html(tree, 'bd')
driver.quit()
