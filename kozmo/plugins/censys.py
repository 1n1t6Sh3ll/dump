from requests import get

def censyss(new, original, params, ip, hostname, inp):
    dirty_response = get('https://censys.io/ipv4/%s/raw' % ip).text
    clean_response = dirty_response.replace('&#34;', '"')
    response = clean_response.split('<code class="json">')[1].split('</code>')[0]
    print (response)