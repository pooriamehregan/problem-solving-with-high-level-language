import re


def find_urls(html, base_url=None, out=None):
    """ receives a string of html and returns a list of all urls found in the text.
    :param base_url: used to handle relative urls
    :param out: name of the file to output to.
    :param html: a string of html
    :return: a list of all urls found in the text
    """
    # get html body
    regex_body = r"<body(.|\n)*</body>"
    body = re.search(regex_body, html).group(0)
    regex_tags = r'<a.*?</a>'
    tags = re.findall(regex_tags, body)
    # Get everything inside href", exluding links that start with #, and rest of the link when # is encountered.
    # also // is stripped from the beginning of the links that have it.
    regex_stripped = r'(((?<=href=")|(?<=href="//))/?\w.*?(?=[#"]))'
    link_list = re.findall(regex_stripped, str(tags))
    # got this line from stack overflow to remove tuples that are returned by findall(when using groups in regex).
    link_list = [tuple(j for j in i if j)[-1] for i in link_list]

    for i in range(len(link_list)):  # add base url to relative links
        link = link_list[i]
        if len(link) > 0 and link[0] == '/' and base_url:
            link_list[i] = base_url + link
    if out:  # write link to file
        with open(out, "w") as outfile:
            for link in link_list:
                outfile.write(link + '\n')
    return link_list


def find_articles(html, base_urls=None, out=None):
    """ calls find urls and returns only urls to Wikipedia articles.
    :param base_urls:
    :param out: name of the file to output to.
    :param html: html text to examine
    :return: list of urls to Wikipedia articles
    """
    link_list = find_urls(html, base_urls)  # get all links in html
    # this regex finds only wikipedia links, and excludes links that contain <:> other than the one in <https:>
    regex_wiki_links = r'((https?://)?(\w*\.)?(wikipedia\.org)[^:]*?(?=\'))'
    wiki_links = re.findall(regex_wiki_links, str(link_list))
    for i in range(len(wiki_links)):  # remove tuples (that resulted by findall) from list
        wiki_links[i] = wiki_links[i][0]
    if out:  # write to file
        with open(out, "w") as outfile:
            for link in wiki_links:
                outfile.write(link + '\n')
    return wiki_links
