
import cookielib
import urllib2, urllib
import time
import re
import traceback

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36'),
                     ('Accept', 'text/html, */*; q=0.01'), 
                     ('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'), 
                     ('Connection', 'keep-alive'),
                     ('Referer', 'http://shegongku.org/passwd/'),
                     ('X-Requested-With', 'XMLHttpRequest')
                     ]

def get_page(url, data=None):
    resp = None
    n = 0
    while n < 5:
        n = n + 1
        try:
            resp = opener.open(url, data)
            page = resp.read()
            return page
        except:
            #traceback.print_exc()
            print "Will try after 2 seconds ..."
            time.sleep(2.0)
            continue
        break
    return "Null"



def get_rs(key):
    url = 'http://shegongku.org/passwd/index.php/Index/search/key/%s/vcode/' % key
    p = get_page(url)
    rs = re.findall(r"<tr><td>(.*?)</td></tr>", p)
    return rs


if __name__ == "__main__":
    print get_rs("abc")
