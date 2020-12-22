""" A flask web server.

    Attributes:
        current_county (str): the current selected county chosen by the user. Is shown as h1 header.
        counties (dict): name and corresponding parameter (which is passed to plotter methods) of all counties
            plus all_counties.
        app (Flask): the flask server.

"""

from python_scripts import web_visualization
from flask import Flask, render_template, request
import tempfile

app = Flask(__name__, static_url_path='/', static_folder='docs/_build/html/', template_folder="../templates")


@app.route('/')
def root():
    """ This is our root function which doesn't do anything other than calling than plot_visualization to render html.

    :return: plot_visualization()
    """
    return plot_visualization()


@app.route('/plot_chart')
def plot_visualization():
    """ Renders plot_chart.html.
    It sets header of html to be county name,
    and fills dropdown menu with counties.

    :return: render_template('plot_chart.html', counties=counties, county=current_county)
    """
    return render_template('plot_chart.html', counties=counties, county=current_county)


@app.route('/plot_chart.json')
def plot_visualization_json():
    """ This function gets called by plot_chart.html template. It creates a layered chart,
    then reads and returns it as json.

    :return: layered chart as json
    """
    plot = web_visualization.plot_both(counties[current_county])
    temp = tempfile.NamedTemporaryFile(suffix='.json')
    plot.save(temp.name)

    with open(temp.name) as file:
        return file.read()


@app.route('/plot_chart_1.json')
def plot_visualization_json_1():
    """ This function gets called by plot_chart.html template. It creates a new cases chart,
    then reads and returns it as json.

    :return: new cases chart as json
    """
    plot = web_visualization.plot_reported_cases(counties[current_county])
    temp = tempfile.NamedTemporaryFile(suffix='.json')
    plot.save(temp.name)

    with open(temp.name) as file:
        return file.read()


@app.route('/plot_chart_2.json')
def plot_visualization_json_2():
    """ This function gets called by plot_chart.html template. It creates a Cumulative number chart,
    then reads and returns it as json.

    :return: Cumulative number chart as json
    """
    plot = web_visualization.plot_cumulative_cases(counties[current_county])
    temp = tempfile.NamedTemporaryFile(suffix='.json')
    plot.save(temp.name)

    with open(temp.name) as file:
        return file.read()


@app.route('/handle_selection', methods=['POST'])
def handle_selection():
    """ Handles dropdown selection by updating the chart to chosen value on dropdown.

    :return: calls root which starts re-rendering process of html.
    """
    global current_county
    current_county = request.form.get("selected")
    return root()


@app.route('/show_help_doc')
@app.route('/<path:path>')
def show_doc(path='index.html'):
    return app.send_static_file(path)


if __name__ == '__main__':
    current_county = 'All Counties'
    counties = {'All Counties': 'all_counties',
                'Agder': 'agder',
                'Innlandet': 'innlandet',
                'Møre og Romsdal': 'more_og_romsdal',
                'Nordland': 'nordland',
                'Oslo': 'oslo',
                'Rogaland': 'rogaland',
                'Troms og Finnmark': 'troms_og_finnmark',
                'Trondelag': 'trondelag',
                'Vestfold og Telemark': 'vestfold_og_telemark',
                'Vestland': 'vestland',
                'Viken': 'viken'
                }
    app.run(debug=True)
