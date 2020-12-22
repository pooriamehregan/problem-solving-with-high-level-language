import re


def get_html_body(html):
    """ extracts html body an returns it
    :param html: html string
    :return: the body of html
    """
    # get html body
    regex_body = r"<body(.|\n)*</body>"
    return re.search(regex_body, html).group(0)


def get_month_digit(month):
    """ Maps a string month to its corresponding numerical value.
    :param month: A String month like January
    :return: A digit month, for instance 01 for January.
    """
    digit_month = {
        'January': '01', 'Jan': '01',
        'February': '02', 'Feb': '02',
        'March': '03', 'Mar': '03',
        'April': '04', 'Apr': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08', 'Aug': '08',
        'September': '09', 'Sept': '09',
        'October': '10', 'Oct': '10',
        'November': '11', 'Nov': '11',
        'December': '12', 'Dec': '12'
    }
    return digit_month.get(month)


# assumes month is always a string
def reformat_dates(dates):
    """ takes inn a reference to a list of string dates and puts them into the following format: YYYY/MM/DD
    and also sorts dates.
    :param dates: list of dates
    :return a formatted date list
    """
    split_reg = r', | |-'  # is used to split day, month and year
    month = None
    year = None
    for i in range(len(dates)):
        day = None  # month and year values are guarantied to be changed in each iteration, but not day,
        # therefore manually set day to 0
        s = re.split(split_reg, dates[i])
        for j in range(len(s)):  # for each date
            if s[j].isalpha():  # if its string, then its a month
                month = '/' + get_month_digit(s[j])
            elif s[j].isdigit():  # its a year or day
                if len(s[j]) == 4:
                    year = s[j]
                else:
                    if len(s[j]) == 1:  # if day is a single digit put 0 in front of it
                        day = '/0' + s[j]
                    else:
                        day = '/' + s[j]
        if len(s) > 0:
            if day is not None:
                dates[i] = year + month + day
            else:
                dates[i] = year + month

    return sorted(dates, key=lambda d: tuple(map(int, d.split('/'))))


def find_dates(html, out=None):
    """ receives a string of html and returns a list of all dates found in the text in the following format.
    :param html: an html string
    :param out: an optional argument which specifies th file the results should be written to.
    :return: a list of string dates in the following format: YYYY/MM/DD
    """
    body = get_html_body(html)

    DAY = r'(([0-2]?[0-9])|(3[0-1]))'
    # case sensitivity should be ignored when using month
    # _S a _D represent string and digit respectively. This separation is because DD/MM format is invalid when year is
    # not present and MM is digit.
    MONTH = r'((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)' \
            r'|(November)|(December)|(Jan)|(Feb)|(Mar)|(Apr)|(Aug)|(Sept)|(Oct)|(Nov)|(Dec))'
    # MONTH_D = r'((0?[9])|(1[0-2]))' was not used due to confusion about if numerical months were allowed
    YEAR = r'([1-9][0-9]{3})'

    DMY = rf'(({DAY} )?{MONTH} {YEAR})'
    MDY = rf'({MONTH}( {DAY})?, {YEAR})'
    YMD = rf'({YEAR} {MONTH}( {DAY})?)'
    ISO = rf'({YEAR}-{MONTH}(-{DAY})?)'
    regex = rf'({DMY}|{MDY}|{YMD}|{ISO})'

    dates = re.findall(regex, body, re.IGNORECASE)
    for i in range(len(dates)):  # remove tuples (that resulted by findall) from list
        dates[i] = dates[i][0]
    dates = reformat_dates(dates)

    if out:  # write dates to file
        with open(out, 'w') as outfile:
            for date in dates:
                outfile.write(date + '\n')
    return dates
