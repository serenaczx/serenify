import webview
import subprocess
from dirscan import scan_website


window = webview.create_window('Serenify', './src/ui/home.html')
window.expose(scan_website)
webview.start(debug=True)