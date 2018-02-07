(function () {
    var tree = {};

    function traversal(t, node) {
        t.info = node.getBoundingClientRect();
        t.children = [];
        var i = 0, childNodes = node.childNodes, item;
        for(; i < childNodes.length; i++) {
            var ct = {};
            item = childNodes[i];
            if (item.nodeType === 1) {
                traversal(ct, item);
                t.children.push(ct);
            }
        }
    }

    traversal(tree, document.body);

    return tree;
})();