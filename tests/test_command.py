# -*- encoding: utf-8 -*-
from StringIO import StringIO
import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        self.f_output = StringIO()

    def _get_command(self):
        from ndkrm import Command
        return Command()

    def test_header(self):
        markdown = StringIO('# Title')
        self._get_command().run(markdown, self.f_output)
        self.assertEqual(self.f_output.getvalue(), u"<h1>Title</h1>")

    def test_header_utf8(self):
        markdown = StringIO(u"# †☤тł℮".encode('utf-8'))
        self._get_command().run(markdown, self.f_output)
        self.assertEqual(self.f_output.getvalue(),
                         u"<h1>†☤тł℮</h1>".encode('utf-8'))

    def test_unordered_list(self):
        markdown = StringIO('''* First line
                                * Second line''')
        self._get_command().run(markdown, self.f_output)
        self.assertEqual(self.f_output.getvalue(),
                         u"<ul><li>First line</li><li>Second line</li></ul>")

    def test_unordered_list_utf8(self):
        markdown = StringIO(u"""* ℉їґṧ☂ ł☤η℮
                                * ϟℯḉ◎ηḓ℮ ℓ☤ᾔℯ""".encode('utf-8'))
        self._get_command().run(markdown, self.f_output)
        self.assertEqual(self.f_output.getvalue(),
                         (u"<ul><li>℉їґṧ☂ ł☤η℮</li>"
                          u"<li>ϟℯḉ◎ηḓ℮ ℓ☤ᾔℯ</li></ul>".encode('utf-8')))
