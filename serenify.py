import webview
import subprocess
from dirscan import scan_website
from info import search_info


window = webview.create_window('Serenify', './src/ui/home.html')
window.expose(scan_website, search_info)
webview.start(debug=True)