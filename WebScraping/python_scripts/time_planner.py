from bs4 import BeautifulSoup
from python_scripts.requesting_urls import get_html
import re
import logging
from datetime import datetime


def log(msg):
    """ prints msg on the screen. Is used to show the progress to user. """
    logging.info(msg)


def fetch_html():
    """ fetches and returns the specified html
    :return: html document read by get_html()
    """
    url = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup'  # 2019-2020
    # url = 'https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup'  # 2020-2021
    html = get_html(url)
    if html.status_code == 200: return html
    else: return None


def get_decipline_dict(table):
    """ turns table caption into dictionary with discipline abbreviation as key,
    and full discipline name as value.
    :param table: the table we are working on
    :return: a dictionary in this format {'SL': 'Slalom', ... }
    """
    caption_text = table.find('caption').text
    regex = r'(?<=Event Key: ).*'
    dicip_list = re.search(regex, caption_text).group(0).split(', ')
    dicip_dict = {}
    for dicip in dicip_list:
        l = dicip.split(' – ')
        dicip_dict[l[0]] = l[1]
    return dicip_dict


def extract_table_data(rows, dis_dict):
    """ extract data from tables.
    :param rows: list of the rows of a given table
    :param dis_dict: is a dictionary which maps discipline abbreviation to full discipline name.
    :return: a 2d list as a table that contains extracted data in this format: [ [Date, Venue, Discipline], ... ].
    """
    log("Extracting data from rows.")
    date_reg = r'\d?\d \w{0,9} \d{4}'
    slip_rows = []
    for j in range(1, len(rows)):
        slip_cols = []
        cells = rows[j].find_all('td')
        for i in range(len(cells)):  # loop until you find date column
            cell_text = cells[i].get_text(strip=True)
            d = re.search(date_reg, cell_text)
            if d:
                date = datetime.strptime(d.group(0), '%d %B %Y').strftime("%d/%m/%Y")  # format date
                slip_cols.append(date)
                n = re.search(r"[A-Z]{2}", cells[i + 1].get_text(strip=True))  # get next col
                if n:  # check if next col i discipline
                    slip_cols.append(slip_rows[j - 2][1])  # append venue, take it from last appended row to slip table
                    slip_cols.append(dis_dict[n.group(0)])  # append discipline
                else:
                    n = re.search(r"[A-Z]{2}", cells[i + 2].get_text(strip=True)).group(0)
                    slip_cols.append(cells[i + 1].get_text(strip=True))
                    slip_cols.append(dis_dict[n])
        slip_rows.append(slip_cols)
    log("Created slip table (2D list).")
    return slip_rows


def get_markdown_header(cell_len):
    """ Creates the markdown header : | HEADER | HEADER | Header |
                                      |:------:|:------:|:------:|
    :param cell_len: lenght of the longest cell + 4
    :return: header as shown above
    """
    spc_d = (cell_len - len('Date') - 4)
    spc_d = (spc_d // 2) if (spc_d % 2) == 0 else (spc_d // 2) + 1
    spc_v = (cell_len - len('Venue') - 4)
    spc_v = (spc_v // 2) if (spc_v % 2) == 0 else (spc_v // 2) + 1
    spc_dis = (cell_len - len('Discipline') - 4)
    spc_dis = (spc_dis // 2) if (spc_dis % 2) == 0 else (spc_dis // 2) + 1
    spc_w = (cell_len - len('WHO WINS?') - 4)
    spc_w = (spc_w // 2) if (spc_w % 2) == 0 else (spc_w // 2) + 1
    header = '|' + ' ' * spc_d + 'DATE' + ' ' * spc_d + '|' \
             + ' ' * (spc_v - 1) + 'Venue' + ' ' * spc_v + '|' \
             + ' ' * spc_dis + 'Discipline' + ' ' * spc_dis + '|' \
             + ' ' * spc_w + 'WHO WINS?' + ' ' * (spc_w - 1) + '|\n' \
             + '|' + (':' + '-' * (cell_len - 6) + ':|') * 4
    return header


def create_markdown_table(list_table):
    """ Creates a markdown table.
    :param list_table: a 2d list that represents the table that should be created.
    :return: a markdown table
    """
    log("Creating markdown table.")
    cell_len = len('Discipline') + 4
    markdown_table = []
    for row in list_table:  # get the biggest column size
        for col in row:
            if len(col) > cell_len: cell_len = len(col)
    markdown_table.append(get_markdown_header(cell_len + 6))

    for row in list_table:
        row_s = '|'
        for col in row:
            row_s += ' ' + col + ' ' * (cell_len - len(col)) + ' |'
        row_s += ' ' * (cell_len + 2) + '|'
        markdown_table.append(row_s)
    log("Markdown table fully created.")
    return markdown_table


def produce_betting_slip(markdown_table):
    """ Creates a betting slip in the file <datetime_filter/betting_slip_empty.md>
    :param markdown_table: a list of rows (string) that represents the markdown table.
    """
    log("Producing betting slip.")
    with open('../datetime_filter/betting_slip_empty.md', 'w') as outfile:
        for row in markdown_table:
            outfile.write(row + '\n')


def extract_events():
    """ Extracts data from wikipedia table. More specifically, extracts data that represent,
    date, venue and discipline column """
    log("Fetching html.")
    html = fetch_html()
    if html is None: return

    log("Creating soup.")
    soup = BeautifulSoup(html.content, 'lxml')
    log("Getting main table.")
    table = soup.find('table', {'class': 'wikitable plainrowheaders'})
    log('Mapping discipline abbreviation to full discipline name.')
    disciplines_dict = get_decipline_dict(table)

    log("Extracting rows.")
    rows = table.find_all('tr')
    table_list = extract_table_data(rows, disciplines_dict)
    markdown_table = create_markdown_table(table_list)
    produce_betting_slip(markdown_table)


#  I intentionally make the url request here and not in the main.py (like I did for other tasks
#  for keeping clean structure), because the assignment says this explicitly.
if __name__ == '__main__':
    # logging library is used to print status on screen under execution
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    # logging.disable(logging.INFO)  # use this call if you wish to disable logging
    extract_events()
    log("Program finish.")
