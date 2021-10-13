#自定义table插件，为了加上css， 适应bootstrap4， 参考了https://www.cnblogs.com/JiangLe/p/12682912.html

# https://github.com/Python-Markdown/markdown/wiki/Tutorial-2---Altering-Markdown-Rendering
# https://getbootstrap.com/docs/5.1/content/tables/

from markdown import extensions
from markdown.treeprocessors import Treeprocessor
class BootstrapTreeprocessor(Treeprocessor):
    def run(self, root):
        for element in root.iter("table"):
            element.set("class", "table table-hover table-bordered")

        for element in root.iter("thead"):
            element.set("class", "table-light")



class BootStrap_table_Extension(extensions.Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(BootstrapTreeprocessor(md), 'bootstrap',12)
        md.registerExtension(self)
