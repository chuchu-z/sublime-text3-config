import sublime
import sublime_plugin
import os


class copyfilenameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        file_name = self.view.file_name()
        base_name = os.path.basename(file_name)
        list_name = base_name.split('.')
        # print(list_name)
        sublime.set_clipboard(list_name[0])
        # print('get_clipboard: ' + sublime.get_clipboard())
