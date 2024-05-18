import subprocess
import re
def scan_website(url):
    result = subprocess.run(['dirsearch', '-u', url], capture_output=True, text=True)
    # 正则匹配 “Output File: ”后面的路径
    result = result.stdout
    output_file = re.search(r'Output File: (.*)', result).group(1)
    with open(output_file, 'r') as f:
        file_content = f.read()
    return file_content

if __name__ == '__main__':
    website_url = 'https://47918cbc-b342-4823-8d2f-74ab4130198b.challenge.ctf.show/'
    scan_result = scan_website(website_url)
