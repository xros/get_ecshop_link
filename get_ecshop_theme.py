#!/usr/bin/env python2
"""
Copyright to Alexander Liu . Aug, 2015
You are free to use and have fun
Usage: 
    To get attachment download link from: http://bbs.ecshop.com/viewthread.php?tid=128540
    It looks like
    *****************
    "http://bbs.ecshop.com/attachment.php?aid=MzY3NjV8NjNkMWQxZjN8MTQzODYzNjk0NnxkMTRjV09wckREZ2JPdXlmZHgvZk1rcVFUVk5Zd2wzcUdiaWR5bXplQU56TEp2bw%3D%3D"
    *****************

    It will be redirected to somewhere by HTTP rediect
    *****************
    "http://www2.shopex.cn/customer-download.html?target_name=RUNTaG9wJUU4JUFFJUJBJUU1JTlEJTlCJUU5JTk5JTg0JUU0JUJCJUI2JUU0JUI4JThCJUU4JUJEJUJE&referer_url=aHR0cCUzQSUyRiUyRmJicy5lY3Nob3AuY29tJTJGdmlld3RocmVhZC5waHAlM0Z0aWQlM0QxMjg1NDA=&product_cat_p=1003&product_cat_c=1016&clues_source_p=1009&clues_source_c=1033&target_download=aHR0cCUzQSUyRiUyRmJicy5lY3Nob3AuY29tJTJGYXR0YWNobWVudC5waHAlM0ZhaWQlM0RNelkzTmpWOE5qTmtNV1F4WmpOOE1UUXpPRFl6TmprME5ueGtNVFJqVjA5d2NrUkVaMkpQZFhsbVpIZ3ZaazFyY1ZGVVZrNVpkMnd6Y1VkaWFXUjViWHBsUVU1NlRFcDJidyUzRCUzRCUyNmlmZG93biUzRDE=&new_product_cat=bWFpbmxhbmQlM0ElRTUlODUlQjYlRTQlQkIlOTYlMkYlRTYlOEUlODglRTYlOUQlODMlRTQlQkElQTclRTUlOTMlODElMkZFY3Nob3AlM0ExMDE4&encode=true"
    *****************
    
    And the link above would lead people to a page where you have to leak your phone calls to sales.
    So now you don't have to.
    Just put the link there, don't forget the sambol quotation -> ""
    *****************
    $~ python get_ecshop_download.py "http://www2.shopex.cn/customer-download.html?target_name=RUNTaG9wJUU4JUFFJUJBJUU1JTlEJTlCJUU5JTk5JTg0JUU0JUJCJUI2JUU0JUI4JThCJUU4JUJEJUJE&referer_url=aHR0cCUzQSUyRiUyRmJicy5lY3Nob3AuY29tJTJGdmlld3RocmVhZC5waHAlM0Z0aWQlM0QxMjg1NDA=&product_cat_p=1003&product_cat_c=1016&clues_source_p=1009&clues_source_c=1033&target_download=aHR0cCUzQSUyRiUyRmJicy5lY3Nob3AuY29tJTJGYXR0YWNobWVudC5waHAlM0ZhaWQlM0RNelkzTmpWOE5qTmtNV1F4WmpOOE1UUXpPRFl6TmprME5ueGtNVFJqVjA5d2NrUkVaMkpQZFhsbVpIZ3ZaazFyY1ZGVVZrNVpkMnd6Y1VkaWFXUjViWHBsUVU1NlRFcDJidyUzRCUzRCUyNmlmZG93biUzRDE=&new_product_cat=bWFpbmxhbmQlM0ElRTUlODUlQjYlRTQlQkIlOTYlMkYlRTYlOEUlODglRTYlOUQlODMlRTQlQkElQTclRTUlOTMlODElMkZFY3Nob3AlM0ExMDE4&encode=true"
    *****************

    Then a link would come out:

    *****************
    http://bbs.ecshop.com/attachment.php?aid=MzY3NjV8NjNkMWQxZjN8MTQzODYzNjk0NnxkMTRjV09wckREZ2JPdXlmZHgvZk1rcVFUVk5Zd2wzcUdiaWR5bXplQU56TEp2bw==&ifdown=1
    *****************

    You could download it from any browser as you like without leaking your phone number to anyone.
"""
import base64, urllib
import sys

def show_help():
    print('''
Try something like this, and do not forget the quotation mark:
$~ python get_ecshop_download.py "http://www2.shopex.cn/customer-download.html?target_name=RUNTaG9wJUU4JUFFJUJBJUU1JTlEJTlCJUU5JTk5JTg0JUU0JUJCJUI2JUU0JUI4JThCJUU4JUJEJUJE&referer_url=aHR0cCUzQSUyRiUyRmJicy5lY3Nob3AuY29tJTJGdmlld3RocmVhZC5waHAlM0Z0aWQlM0QxMjg1NDA=&product_cat_p=1003&product_cat_c=1016&clues_source_p=1009&clues_source_c=1033&target_download=aHR0cCUzQSUyRiUyRmJicy5lY3Nob3AuY29tJTJGYXR0YWNobWVudC5waHAlM0ZhaWQlM0RNelkzTmpWOE5qTmtNV1F4WmpOOE1UUXpPRFl6TmprME5ueGtNVFJqVjA5d2NrUkVaMkpQZFhsbVpIZ3ZaazFyY1ZGVVZrNVpkMnd6Y1VkaWFXUjViWHBsUVU1NlRFcDJidyUzRCUzRCUyNmlmZG93biUzRDE=&new_product_cat=bWFpbmxhbmQlM0ElRTUlODUlQjYlRTQlQkIlOTYlMkYlRTYlOEUlODglRTYlOUQlODMlRTQlQkElQTclRTUlOTMlODElMkZFY3Nob3AlM0ExMDE4&encode=true"
            
You may get a download link like this:
http://bbs.ecshop.com/attachment.php?aid=MzY3NjV8NjNkMWQxZjN8MTQzODYzNjk0NnxkMTRjV09wckREZ2JPdXlmZHgvZk1rcVFUVk5Zd2wzcUdiaWR5bXplQU56TEp2bw==&ifdown=1
''')

            


def get_download_link(encrypted_url=None):
    """
    """
    if encrypted_url != None and "?" in str(encrypted_url) and "&" in str(encrypted_url):
        pass
    else:
        print("Please input valid encrypted URL")
        show_help()
        return

    param = str(encrypted_url).split("?")[1:]
    if len(param) == 0:
        print("Please input valid encrypted URL")
        return
        
    all_param = param[0].split("&")
    target_download = None

    for i in all_param:
        string = i.split("=")
        name = string[0]
        value = string[1]
        if name == "target_download":
            target_download = value
        else:
            pass

    if target_download is None:
        return None
    else:
        return urllib.unquote(base64.decodestring(target_download + "="))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please input ecshop theme download URL")
        show_help()
    else:
        result = get_download_link(sys.argv[1])
        if result is not None:
            print(result) 
