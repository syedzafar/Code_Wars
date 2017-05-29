# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#




def domain_name(url):
    url = url.split('//')[-1]

    url = url.split('/')[0]

    url = url.split('.')[-2]

    return url





    # if url[10] == '.':
    #
    #     y = url.find('.com')
    #     f = url[:y][11:]
    #     return str(f)
    #
    # if url[11] == '.':
    #     z = url.find('.com')
    #     z = url[:z][12:]
    #     return str(z)
    #
    # if url[4] != 's' and url[8] != 'w':
    #
    #     c = url.find('.com')
    #     d = url[:c][7:]
    #     return str(d)
    # if url[4] == 's' and url[7] == 'w':
    #     a = url.find('.com')
    #     b = url[:a][8:]
    #     return str(b)
