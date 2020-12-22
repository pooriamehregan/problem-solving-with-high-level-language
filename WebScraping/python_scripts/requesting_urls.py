import requests as req


def write_to_file(output, text, url):
    """ Writes url and the html string to the given file (output)
    :param output: the file to save to
    :param text: html response
    :param url: requested url
    """
    with open(output, 'w') as outputfile:
        s = 'URL: ' + url + '\n\n' + text
        outputfile.write(s)


def get_html(url, params=None, output=None):
    """ makes a url request of a given website and returns and optionally writes
    response html to a txt file.
    :param url: requesting url
    :param params: parameters to the to get methode(to url)
    :param output: name of the destination file to save the result to.
    :return: the html that was read. To get text version, add <.text> at the end of returned value.
    """
    resp = req.get(url, params=params)
    if output:
        write_to_file(output, resp.text, url)
    return resp
