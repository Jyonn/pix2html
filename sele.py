from selenium import webdriver


def get_tree(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    tree_ = driver.execute_script("""
    return (function () {
        function same_info(a, b) {
            return a.x == b.x && a.y == b.y && a.width == b.width && a.height == b.height;
        }
        
        function traversal(node) {
            var t = {}, ct;
            t.info = node.getBoundingClientRect().toJSON();
            delete t.info.top;
            delete t.info.bottom;
            delete t.info.left;
            delete t.info.right;
            //if (!t.info.width || !t.info.height)
            //    return null;
            if (window.getComputedStyle(node)['visibility'] == 'hidden' || window.getComputedStyle(node)['display'] == 'none')
                return null;
            var i = 0, childNodes = node.childNodes, item;
            t.children = [];
            for(; i < childNodes.length; i++) {
                item = childNodes[i];
                if (item.nodeType === 1) {
                    ct = traversal(item);
                    if (ct && ct.info.width && ct.info.height)
                        t.children.push(ct);
                    else if (ct && ct.children)
                        t.children = t.children.concat(ct.children);
                }
            }
            if (!t.children.length)
                delete t.children;
            else if (t.children.length == 1 && same_info(t.info, t.children[0].info))
                return t.children[0];
            return t;
        }
    
        tree = traversal(document.body);
        return tree;
    })();
    """)
    driver.quit()
    tree_['url'] = url
    return tree_

tree = get_tree('https://430060.com/ac/21')
print(tree)

html_eles = ""


def add_ele(d):
    assert isinstance(d, dict)
    global html_eles
    info = d['info']
    html_eles += '''  <div class="ele" style="top: %spx; left: %spx; width: %spx; height: %spx"></div>\n''' \
                 % (info['y'], info['x'], info['width'], info['height'])
    if 'children' in d.keys():
        for item in d['children']:
            add_ele(item)

add_ele(tree)

html = """<html>
<head>
  <style>
    .ele {
      position: absolute;
      background-color: rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
%s
</html>
""" % html_eles

with open('sele.html', 'wb+') as f:
    f.write(html.encode())
