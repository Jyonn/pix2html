import json
from common import fullpage_screenshot


def get_tree(driver, url, filename):
    driver.get(url)
    fullpage_screenshot(driver, 'dataset/%s.png' % filename)

    tree_ = driver.execute_script("""
    return (function () {
        function same_info(a, b) {
            return a.x == b.x && a.y == b.y && a.width == b.width && a.height == b.height;
        }
        
        function traversal(node) {
            var t = {}, ct;
            t.info = node.getBoundingClientRect().toJSON();
            t.info.tag = node.nodeName;
            delete t.info.top;
            delete t.info.bottom;
            delete t.info.left;
            delete t.info.right;
            //if (!t.info.width || !t.info.height)
            //    return null;
            if (window.getComputedStyle(node)['visibility'] == 'hidden' || window.getComputedStyle(node)['display'] == 'none') {
                return null;
            }
            var i = 0, childNodes = node.childNodes, item;
            t.children = [];
            for(; i < childNodes.length; i++) {
                item = childNodes[i];
                if (item.nodeType === 1) {
                    ct = traversal(item);
                    if (ct && ct.info.width && ct.info.height && !same_info(t.info, ct.info))
                        t.children.push(ct);
                    else if (ct && ct.children)
                        t.children = t.children.concat(ct.children);
                }
            }
            if (!t.children.length)
                delete t.children;
            //else
            //    for (i = 0; i < t.children.length; i++)
            //        if (same_info(t.info, t.children[i].info))
            //            return t.children = t.children;
            return t;
        }
    
        tree = traversal(document.body);
        return tree;
    })();
    """)
    tree_['url'] = url
    with open('dataset/%s.json' % filename, 'wb+') as f:
        f.write(json.dumps(tree_).encode())
    return tree_
#
# tree = get_tree('https://www.baidu.com/more/')
#


def get_html(tree, filename):
    def add_ele(d):
        assert isinstance(d, dict)
        info = d['info']
        html_eles = '''  <div class="ele %s" style="top: %spx; left: %spx; width: %spx; height: %spx"></div>\n''' \
                     % (info['tag'], info['y'], info['x'], info['width'], info['height'])
        if 'children' in d.keys():
            for item in d['children']:
                html_eles += add_ele(item)
        return html_eles

    html = add_ele(tree)

    html_all = """<html>
<head>
  <style>
    .ele {
      position: absolute;
      background-color: rgba(0, 0, 0, 0.1);
    }
    .ele.IMG {
      background-color: rgba(255, 0, 0, 0.1);
    }
    .ele.INPUT, .ele.TEXTAREA {
      background-color: rgba(0, 255, 0, 0.1);
    }
    .ele.A {
      background-color: rgba(0, 0, 255, 0.1);
    }
    .ele.BUTTON {
      background-color: rgba(255, 255, 0, 0.1);
    }
  </style>
</head>
<body>
%s
</body>
</html>
    """ % html

    with open('dataset/%s.html' % filename, 'wb+') as f:
        f.write(html_all.encode())
