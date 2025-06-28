def get_domain_name(url):
    # url = url.replace('http://', '').replace('https://','').replace('www.','').replace('com', '').replace('.', '')
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('com', '')
    url = url.replace('www.', '')
    url = url.replace('.', '')
    return url.split(' ')[0]

print(get_domain_name("http://google.com"))

