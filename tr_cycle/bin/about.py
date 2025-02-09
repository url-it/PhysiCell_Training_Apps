from ipywidgets import Output
from IPython.display import display, HTML
import os
class AboutTab(object):
    def __init__(self):
        self.tab = Output(layout={'height': 'auto'})
        base_path = os.path.dirname(os.path.abspath(__file__))
        about_html_path = os.path.abspath(os.path.join(base_path, '../doc/about.html'))
        if not os.path.isfile(about_html_path):
            raise FileNotFoundError(f"No such file or directory: '{about_html_path}'")
        self.tab.append_display_data(HTML(filename=about_html_path))
