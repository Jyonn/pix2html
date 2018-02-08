import random

from bs4 import BeautifulSoup, Tag

from old import ytb
from old.base import *

ytb.data[type_] = body

data = ytb.data

soup = BeautifulSoup('', "html.parser")
tag = soup.new_tag(data[type_])
css = ''

output_html = "output.html"
output_css = "output.css"


def get_rgb(l):
    return 'rgb(%s, %s, %s)' % (l[0], l[1], l[2])


def get_random_string(length, choices="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    s = ''
    for i in range(length):
        s += random.choice(choices)
    return s


def generate_css(d):
    assert isinstance(d, dict)
    id_ = get_random_string(length=6)
    c_dict = {
        position: 'absolute',
    }
    if position in d.keys():
        c_dict['top'] = '%spx' % d[position][1]
        c_dict['left'] = '%spx' % d[position][0]
    if size in d.keys():
        c_dict['width'] = '%spx' % d[size][0]
        c_dict['height'] = '%spx' % d[size][1]
    if background in d.keys():
        if d[background] == image:
            c_dict['background-size'] = 'cover'
            c_dict['background-position'] = '50%'
            c_dict['background-repeat'] = 'no-repeat'
            c_dict['background-image'] = 'url("https://unsplash.6-79.cn/random/regular?r=%s")' % random.random()
        else:
            c_dict['background'] = get_rgb(d[background])
    if border in d.keys():
        c_dict['border'] = '%s %spx solid' % (get_rgb(d[border][0]), d[border][1])
    if border_radius in d.keys():
        c_dict['border-radius'] = "%spx %spx" % (d[border_radius][0], d[border_radius][1])
    if text in d.keys():
        c_dict['color'] = get_rgb(d[text][0])
        c_dict['font-size'] = '%spx' % d[text][1]
    c = '#%s {\n' % id_
    for item in c_dict.keys():
        c += '  %s: %s;\n' % (item, c_dict[item])
    c += '}\n\n'
    return c, id_


def insert_json2html(d, t):
    assert isinstance(d, dict)
    assert isinstance(t, Tag)
    global css
    global soup

    c, id_ = generate_css(d)
    css += c
    t['id'] = id_
    if text in d.keys():
        t.string = d[text][2]
    if children in d.keys():
        for child in d[children]:
            assert isinstance(child, dict)
            if type_ not in child.keys():
                child[type_] = div
            new_t = soup.new_tag(child[type_])
            insert_json2html(child, new_t)
            t.append(new_t)

insert_json2html(data, tag)
soup.append(tag)

html = """<html>
  <head>
    <link rel="stylesheet" href="%s" type="text/css" />
  </head>
</html>
%s
""" % (output_css, soup.prettify())

with open(output_html, 'wb+') as f:
    f.write(html.encode())
with open(output_css, 'wb+') as f:
    f.write(css.encode())
