import sys


class Command(object):

    blocks = None
    stack = None

    def run(self, f_input, f_output):
        self.blocks = []
        self.stack = []
        self.parse(f_input)
        self.render(f_output, format='html')

    def parse(self, f_input):
        while True:
            line = f_input.readline()

            if line == '':  # EOF as documented in readline
                break

            line = line.strip()

            if line == '':
                self.blocks.append(LineBreak())
                if self.stack:
                    self.stack.pop()

            if line[0] == '#':
                self.blocks.append(Header(line))

            if line[0] == '*':
                self.append_list_element(line)

    def render(self, f_output, format='html'):
        for block in self.blocks:
            block.render(f_output, format='html')

    def append_list_element(self, line):
        if not self.stack:
            unordered_list = UnorderedList()
            self.blocks.append(unordered_list)
            self.stack.append(unordered_list)
        else:
            unordered_list = self.stack[-1]
            assert isinstance(unordered_list, UnorderedList)

        unordered_list.append(line)


class Node(object):
    pass


class Header(Node):

    def __init__(self, line):
        assert line[0] == '#'
        words = line.split(' ')
        self.header_level = len(words[0])
        self.body = line[self.header_level + 1:]

    def render(self, f_output, format='html'):
        f_output.write('<h%s>' % self.header_level)
        f_output.write(self.body.encode('utf-8'))
        f_output.write('</h%s>' % self.header_level)


class LineBreak(Node):

    def render(self, f_output, format='html'):
        f_output.write('<br/>')


class UnorderedList(Node):

    def __init__(self):
        self.elements = []

    def append(self, line):
        assert line[0] == '*'
        self.elements.append(line[2:])

    def render(self, f_output, format='html'):
        f_output.write('<ul>')
        for elem in self.elements:
            f_output.write('<li>')
            f_output.write(elem.encode('utf8'))
            f_output.write('</li>')
        f_output.write('</ul>')


def main():  # noqa
    Command().run(sys.stdin, sys.stdout)
