"""博客园绕过登陆，访问登陆后的页面：方式一抓包获取cookie"""
import requests
import urllib3
urllib3.disable_warnings()
s = requests.session()
s.verify = False

def cnblog_fabu(i):
    url = "https://home.cnblogs.com/ajax/ing/Publish"
    c = requests.cookies.RequestsCookieJar()#对象是set
    c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8AHUmC2ZwXVKl7whpe9_lasUNdmseMkOSMpVSE4UNSwuqumap-b0ySKAtViiiLfPC1tSUM1RqXjGoBBk6U9bfacp-Xv6cdKWagF_ZESZ8Bd2uD6x9MVn1dV3Z6WkBwLIQ-lQuGi8ODsqmAnSg2NfkaT3jtN8J6DeQPNXNQsetIg9lSE1ZsRHejjmsBgG2B-egDlsjOJIOT6FEIgZkOv-KHf7GRypA3TEvQSCjoS8of13mrKwifA48mdxadRKF3JfuIXa7Ads_oEkcK7jTzxSD3uI_hWxQUHBjWU8QjrrU7vSyNeZgJVbyb3Ob5ohFs-Bgo5pvqO6LTj2G92Sx31ELkJOcaukvE9ri1o3W4Chpq0cCQcUWVK0ey2ZLfa4SGt0KO71ikcOlrwnNNC9DfO_lEFMfk9UBMwijKWLkGG5-ZXh8xf-NSM8LsEWq5BLg8aw1YeIkqBC_8NpCLhhPH4Q3gnR9g_VaZLzkMWrBXo0J5nT4gOasS9wr_G_llMXoyl5tgYUMcpfRH-KAnDtByY9OUbve_IZaP9tZT5QEYhC_DgPaXqQ2H2bgKTLrBKuyBRlPA")
    #c.set(".CNBlogsCookie", "13AFF6911EDA47684A837D3FDD4C2DF35C598496EA49ED1AA629A38B7EAD6CCF1581C112D8DC9BB70378291F4244E826DA2C2F0F8850205F092CA8B076A85F032F909B50C54B8C2651ACB585C362E8E471D72F00")
    s.cookies.update(c)

    h = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {
        "content": i,
        "publicFlag": 1
    }
    r = s.post(url, json=body, headers=h)
    print(r.json())

if __name__ == '__main__':
    for i in range(5211310, 5211315):
        cnblog_fabu(i)



"""优化了第一种方式"""
import requests
import urllib3

urllib3.disable_warnings()
s = requests.session()
s.verify = False


def cnblog_fabu(i):
    url = "https://home.cnblogs.com/ajax/ing/Publish"
    #直接把cookie更新到头部
    h = {
        "Cookie": ".Cnblogs.AspNetCore.Cookies=CfDJ8AHUmC2ZwXVKl7whpe9_las_6wIcBtkx2le7cxiKordBwRZqNABuLS5vWh9JyQjO0N1HNFz796Z6fu0mVPTblPpCwGRqItllPaMUqt7hkvoQz0fESLzMTUsQomNb4op-MpI7HeIj2R3b2cf-GXRKWCz4emafz2gPXMe4IKpuq1UPD586KIIm42xYB_u-ZZxcbNYHbRymB_wVss1lOBTsAvOyGG95xdJ_OAmBs2M7D2CspiSHmfAvh-r17APQA4kGWWF24P8UuB-rBvo4rr0D3XceVHlzcXfsG8i3jSSvaQcb40eyuHOC5ilPPaD---oiCRdsvBtYk09572Er7MAv5qkaJOB7b0JfWcEZNfhNlkGuTOA2C2FJAfcKiFADF8w2OhuMIW3vVM7544CSZywnf8ujAoTwEBkrUIsI5rKlf-zOjqaFX8C7-te5PU5k3f05u981OgltAU-7QOJxhbbdzXVxiOyHudu5B2n4RE4x_2OGnoN2pvSKR7UifXrXP61xL6q8gA_UvTdf357ELtUHrjBoFmtRvScnM_b4VPLagZB5RrVLkD49_STrMHpL8vsNpA"
    }
    # s.headers.update(h)
    body = {
        "content": i,
        "publicFlag": 1
    }
    r = s.post(url, json=body, headers=h)
    print(r.json())


if __name__ == '__main__':
    for i in range(5211316, 5211318):
        cnblog_fabu(i)











