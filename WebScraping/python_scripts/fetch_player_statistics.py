import logging
from bs4 import BeautifulSoup
from python_scripts.requesting_urls import get_html
import re
import matplotlib.pyplot as plt


def log(msg):
    """ prints msg on the screen. Is used to show the progress to user. """
    logging.info(msg)


def isfloat(string):
    """ Check if a string is a float value in following format ([0-9].[0-9]).
    :param string: the string to be checked.
    :return: a boolean, True if float, False otherwise.
    """
    r = re.search(r'^\d*\.\d$', string)
    return r and r.group(0)


def create_soup(url):
    """ Creates and returns soup.
    :param url: url to be requested.
    :return: A BeautifulSoup
    """
    html = get_html(url)
    if html is None: return
    return BeautifulSoup(html.content, 'lxml')


def get_point_index(rows):
    """ Extracts PPG, BPG, and RPG indices from table header to later find them in the table rows.
    :param rows: rows of the table.
    :return: a dictionary mapping keys to PPG, BPG, and RPG indices.
    """
    # get header titles as a list, and remove \n and empty strings
    header = list(filter(None, rows[0].text.split('\n')))
    RPG_indx = BPG_indx = PPG_indx = 0
    for i in range(len(header)):
        title = header[i]
        if title == 'RPG':
            RPG_indx = i
        elif title == 'BPG':
            BPG_indx = i
        elif title == 'PPG':
            PPG_indx = i
    return {'RPG_indx': RPG_indx, 'BPG_indx': BPG_indx, 'PPG_indx': PPG_indx}


def get_player_stats(player_url):
    """ Extracts and returns player stats.
    :param player_url: link to players wikipedia profile.
    :return: list of statics: [PPG, BPG, RPG]
    """
    soup = create_soup(player_url)
    table = soup.find('table', {'class': 'sortable'})
    if table: rows = table.find_all('tr')
    else: return [0, 0, 0]  # player stats doesn't exists, give it lowest score

    scores = get_point_index(rows)
    RPG = BPG = PPG = 0
    for i in range(1, len(rows)):
        row = rows[i].find_all('td')
        if row[0] and row[0].a and row[0].a['title'] and row[0].a['title'] == '2019–20 NBA season':
            a = str(row[scores['RPG_indx']].text)
            if isfloat(a): RPG = float(a)
            else: RPG = 0
            b = str(row[scores['BPG_indx']].text)
            if isfloat(b): BPG = float(b)
            else: BPG = 0
            c = str(row[scores['PPG_indx']].text)
            if isfloat(c): PPG = float(c)
            else: PPG = 0
    return [PPG, BPG, RPG]


def get_team(team_url):
    """ Returns info on top tree players. Example: < [['Antetokounmpo, Giannis',
    'https://en.wikipedia.org/wiki/Giannis_Antetokounmpo', [29.5, 1.0, 13.6]],...] >
    :param team_url: url to the specified team.
    :return: 2d list containing top three player's info.
    """
    log("Handling a team's stats.")
    soup = create_soup(team_url)
    roster_rows = soup.find('table', {'class': 'toccolours'}).find_all('tr')[2].find_all('tr')
    players = []
    for i in range(1, len(roster_rows)):
        cell = roster_rows[i].contents[5]
        player_name = cell.get_text(strip=True).strip()
        player_url = base_url + cell.a['href']
        player_points = get_player_stats(player_url)
        players.append([player_name, player_url, player_points])
    return sorted(players, key=lambda player: player[2][0], reverse=True)[0:3]  # top three


def get_finalists(main_table):
    """ Extracts and returns semifinalists' stats and info.
    :param main_table:
    :return: list of semifinalists' stats and info. [[team_name, url, [[player_name, url, points], ... ]], ... ]
    """
    log("Extracting semifinalists.")
    table_rows = main_table.find_all('tr')
    semi_fin_rows = [4, 6, 16, 18, 28, 30, 40, 42]
    stats = []
    for i in range(len(table_rows)):
        if i in semi_fin_rows:
            row = table_rows[i].find_all('td')
            a_tag = row[3].find('a')
            team_name = a_tag.text.strip()
            team_url = base_url + a_tag['href'].strip()
            stats.append([team_name, team_url, get_team(team_url)])
    return stats


def save_plot(plot, p):
    """ Saves plot to .png file.
    :param plot: the plot to be saved
    :param p: type of plot: PPG, BPG, RPG as int 0, 1, or 2 in same order.
    """
    plot.xticks(rotation=90)
    plot.tight_layout()
    if p == 0: plot.savefig('NBA_player_statistics/players_over_ppg.png')
    elif p == 1: plot.savefig('NBA_player_statistics/players_over_bpg.png')
    elif p == 2: plot.savefig('NBA_player_statistics/players_over_rpg.png')
    plot.close()


def plot_stats(semi_finalists):
    """ Creates plots for top three players of 8 NBA semifinalist teams 2019-20.
    :param semi_finalists: list containing semifinalists' data.
    """
    log('Creating plots.')
    for i in range(3): # should be changed to 3
        for j in range(8):
            names = []; points = []
            team = semi_finalists[j][2]
            for z in range(3):
                names.append(team[z][0])
                points.append(team[z][2][i])
                plt.bar(names, points)
        save_plot(plt, i)


def extract_url(url):
    """ this is the first method getting called. Calls another methods to
    extract and plot NBA stats.
    :param url: link to NBA season
    """
    soup = create_soup(url)
    log("Finding main table.")
    bracket_section = soup.find('span', {'id': 'Bracket'})
    main_table = bracket_section.find_next('table')
    semi_finalists = get_finalists(main_table)
    plot_stats(semi_finalists)


if __name__ == '__main__':
    base_url = 'https://en.wikipedia.org'
    _url = 'https://en.wikipedia.org/wiki/2020_NBA_playoffs'
    # logging library is used to print status on screen under execution
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    # logging.disable(logging.INFO)  # use this call if you wish to disable logging

    extract_url(_url)
    log("Program finish.")
