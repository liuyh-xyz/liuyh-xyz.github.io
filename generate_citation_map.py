import os

# 让发往本机（geckodriver 等）的连接绕过 Clash 代理，避免 Selenium 本地通信超时；
# 访问 Google Scholar 的外部请求仍走系统代理。
os.environ['no_proxy'] = 'localhost,127.0.0.1,::1'
os.environ['NO_PROXY'] = 'localhost,127.0.0.1,::1'

from citation_map import generate_citation_map
from scholarly import scholarly

if __name__ == '__main__':
    scholar_id = '61-9fbgAAAAJ'  # This is my Google Scholar ID. Replace this with your ID.
    # 第二阶段需要逐个访问 1017 位作者主页，多进程模式下子进程无法弹浏览器解验证码，
    # 因此用单进程串行；遇到验证码时 scholarly 会自动弹出 Firefox，手动解决即可。
    scholarly.set_retries(10)
    generate_citation_map(scholar_id, num_processes=1)
