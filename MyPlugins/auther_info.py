import sublime
import sublime_plugin
import datetime


class autherinfoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents":"/**""\n"
                # "* ===================================== ""\n"
                "* @Author:      chuchu-z""\n"
                "* @DateTime:    ""%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                # "* @Description: Description ""\n"
                "**/""\n"
            }
        )
