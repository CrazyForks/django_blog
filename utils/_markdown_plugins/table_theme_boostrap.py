#自定义table插件，为了加上css， 适应bootstrap4， 参考了https://www.cnblogs.com/JiangLe/p/12682912.html
from markdown import extensions
from markdown.treeprocessors import Treeprocessor
class BootstrapTreeprocessor(Treeprocessor):
    def run(self, node):
        for child in node.getiterator():
            # 如果是 table
            if child.tag == 'table':
                child.set("class", "table table-bordered")
            if child.tag == 'thead':
                child.set("class", "thead-dark")
            # elif child.tag == 'h2':
            #     child.set("class", "h5 text-secondary mb-4")
            # elif child.tag == 'img':
            #    child.set("class","img-fluid")
        return node
class BootStrap_table_Extension(extensions.Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        self.processor = BootstrapTreeprocessor()
        self.processor.md = md
        self.processor.config = self.getConfigs()
        md.treeprocessors.add('bootstrap', self.processor, '_end')
