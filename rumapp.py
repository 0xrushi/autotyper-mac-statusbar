import rumps
from time import sleep
import pyautogui

# Assuming 4 spaces for a tab;
tab_replacement = '    '

class AutoTyper(rumps.App):
    def __init__(self):
        super(AutoTyper, self).__init__("AutoTyper", icon='icons/logo.icns')
        self.menu = [rumps.MenuItem("Launch AutoType window", callback=self.text_window)]

    def text_window(self, _):
        response = rumps.Window(title="Enter your text to auto type",
                                message="The script will launch in 5 seconds",
                                default_text="",
                                ok="Submit").run()
        if response.clicked:
            sleep(5)            
            multi_line_text = response.text
            lines = multi_line_text.replace('\t', tab_replacement).split('\n')

            for line in lines:
                pyautogui.typewrite(line)
                pyautogui.press('enter')
                sleep(0.1)

if __name__ == "__main__":
    AutoTyper().run()
