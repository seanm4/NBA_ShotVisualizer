from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the App.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "App.ipynb", "--allow-websocket-origin=*"])
