from lark import Lark, Transformer
import json

grammar = """
    ?start: element+

    ?element: "<" tag ">" content "</" tag ">"   -> tagcontent

    ?content: element+                          -> elements
            | value                             -> value

    tag: /[a-zA-Z_][a-zA-Z0-9_-]*/
    value: /[^<]+/

    %import common.WS_INLINE
    %ignore WS_INLINE
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='start')


class xmlToDict(Transformer):
    def tagcontent(self, items):
        tag, content = items
        return {tag: content}

    def value(self, items):
        return items[0]

    def elements(self, items):
        result = {}
        for item in items:
            result.update(item)
        return result

    def start(self, items):
        result = {}
        for item in items:
            result.update(item)
        return result


xmltree = parser.parse(open("test2.xml", encoding='UTF-8').read())


def dict(tree):
    if tree.data == 'tagcontent':
        tag = tree.children[0].children[0].value
        content = dict(tree.children[1])
        return {tag: content}
    elif tree.data == 'value':
        k = tree.children[0].children[0].value
        return k
    elif tree.data == 'elements':
        result = {}
        for child in tree.children:
            result.update(dict(child))
        return result
    elif tree.data == 'start':
        result = {}
        for child in tree.children:
            result.update(dict(child))
        return result
    return None


result = dict(xmltree)
print(json.dumps(result, ensure_ascii=False, indent=4))