import re
import altair as alt
import altair_viewer
import pandas as pd


def plot_reported_cases(county='all_counties', time_start='2020-01-01', time_end='2020-11-10'):
    """ plot a bar plot which shows number of reported new cases of covid-19 vs date.

    :param county: the county to show plot for.
    :type county: str, optional
    :param time_start: start date
    :type time_start: str, optional
    :param time_end: end date
    :type time_end: str, optional
    :return: altair Chart
    :rtype: altair.vegalite.v4.api.LayerChart
    """
    duration = main(county, time_start, time_end)
    chart_title = 'Reported cases of covid 19 in ' + re.sub(r'_', ' ', county)

    brush = alt.selection_single(on='mouseover', empty='none')

    chart = alt.Chart(duration, title=chart_title).mark_bar().encode(
        x=alt.X('yearmonthdate(Dato):T', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('Nye tilfeller', title='New cases'),
        color=alt.condition(brush, alt.value('red'), alt.value('lightgray')),
        tooltip=[alt.Tooltip('Dato', title='Date: '),
                 alt.Tooltip('Nye tilfeller', title='New cases: ')]
    ).properties(
        selection=brush
    )
    return chart


def plot_cumulative_cases(county='all_counties', time_start='2020-01-01', time_end='2020-11-10'):
    """ plot a line plot which shows cumulative number of reported cases of covid-19 vs date.

    :param county: the county to show plot for.
    :type county: str, optional
    :param time_start: start date
    :type time_start: str, optional
    :param time_end: end date
    :type time_end: str, optional
    :return: altair Chart
    :rtype: altair.vegalite.v4.api.LayerChart
    """
    duration = main(county, time_start, time_end)
    chart_title = 'Reported cases of covid 19 in ' + re.sub(r'_', ' ', county)
    brush = alt.selection_single(on='mouseover', empty='none')

    static_chart = alt.Chart(duration, title=chart_title).mark_line().encode(
        x=alt.X('yearmonthdate(Dato):T', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('Kumulativt antall', title='Cumulative number of cases'),
        color=alt.value('lightgray')
    )
    pop_up_chart = alt.Chart(duration).mark_point(size=100).encode(
        x=alt.X('yearmonthdate(Dato):T'),
        y=alt.Y('Kumulativt antall'),
        color=alt.condition(brush, alt.value('red'), alt.value('transparent')),
        tooltip=[alt.Tooltip('Dato', title='Date: '),
                 alt.Tooltip('Kumulativt antall', title='Cumulative number: ')]
    ).properties(
        selection=brush
    )

    return alt.layer(static_chart, pop_up_chart)


def main(county='all_counties', time_start='2020-01-01', time_end='2020-11-10'):
    """ reads data from a .csv file and generates a labeled,3 nice plot of date vs. ”number of reported cases” or
    date vs. ”cumulative number of cases”.

    :param county: the county to show plot for.
    :type county: str, optional
    :param time_start: start date
    :type time_start: str, optional
    :param time_end: end date
    :type time_end: str, optional
    :return: DataFrame that contains information of the given time frame
    :rtype: pandas.DataFrame
    """
    file_name = 'csv_files/' + county + '.csv'
    reported = pd.read_csv(file_name,
                           sep=';',
                           parse_dates=['Dato'],
                           dayfirst=True)

    start_time = pd.to_datetime(time_start).date()
    end_time = pd.to_datetime(time_end).date()

    duration = reported[(reported['Dato'].dt.date >= start_time) & (reported['Dato'].dt.date <= end_time)]
    return duration


def plot_both(county='all_counties', time_start='2020-01-01', time_end='2020-11-10', aggr='layer'):
    """ displaying Number of reported cases and Cumulative number of cases in one plot

    :param aggr: how to concatenate to charts: can be h (for horizontal), v (for vertical), layer (for layered)
    :type aggr: str, optional
    :param county: the county to show plot for.
    :type county: str, optional
    :param time_start: start date
    :type time_start: str, optional
    :param time_end: end date
    :type time_end: str, optional
    :return: altair Chart
    :rtype: altair.vegalite.v4.api.LayerChart
    """
    rep_cas = plot_reported_cases(county, time_start, time_end)
    cum_cas = plot_cumulative_cases(county, time_start, time_end)

    if aggr == 'h':
        chart = alt.hconcat(rep_cas, cum_cas)
    elif aggr == 'v':
        chart = alt.vconcat(rep_cas, cum_cas)
    else:
        chart = alt.layer(cum_cas, rep_cas).resolve_scale(y='independent')
    return chart

