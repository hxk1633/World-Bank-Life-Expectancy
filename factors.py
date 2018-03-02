"""
Harrison Kaiser
2017 December 10
This program computes the median life expectancies of each year for each country in a income group and region
Uses turtle graphics to plot a line graph
"""

from utils import *
import turtle as t

def COLORS():
    """
    :return: list - colors to be used for graphs
    """
    return ["red", "blue", "green", "orange", "yellow", "violet", "black"]

def X_AXIS_LEN():
    """
    :return: int - length of x-axis
    """
    return 420

def Y_AXIS_LEN():
    """
    :return: int - length of y-axis
    """
    return 400

def draw_key(lst):
    """
    This funciton draws the key given a list of strings
    :param lst: list - contains strings for the key
    """
    colors = COLORS()
    t.setpos(-200, 250)
    i = 0
    for group in lst:
        t.color(colors[i])
        t.write(group, False)
        t.up()
        t.fd(50)
        t.down()
        t.fd(70)
        t.up()
        t.left(90)
        t.back(20)
        t.right(90)
        t.back(120)
        t.down()
        i = i + 1

def ORIGIN():
    """
    :return: int - origin for x and y
    """
    return -210

def plot_graph(data):
    """
    This function plots a line graph
    :param data: dictionary - keys are year and value is a median life expectancy for that year
    """
    colors = COLORS()
    i = 0
    for group in data:
        ii = 1
        x = ORIGIN()
        y = ORIGIN() + ((group[1960] * (Y_AXIS_LEN() // 9)) // 10)
        t.up()
        t.setpos(x, y)
        t.color(colors[i])
        t.down()
        for year in range(1961, 2016):
            y = ORIGIN() + ((group[year]*(Y_AXIS_LEN()//9))//10)
            x = ORIGIN() + ((X_AXIS_LEN()//55) + ii)
            t.setpos(x, y)
            ii = ii + 7.5
        i = i + 1

def find_median(data):
    """
    This function calculates median for each year for all groups
    :param data: dictionary - key is year and value is list of life epectancies for that year
    :return: dictionary - computed value for each year in each group
    """
    for group in data:
        for year in group.keys():
            sorted = quickSortFactors(group[year])
            if len(sorted) % 2 == 0:
                idx1 = (len(sorted)//2) - 1
                idx2 = ((len(sorted)//2) + 1) - 1
                median = (sorted[idx1] + sorted[idx2])//2
                group[year] = median
            else:
                idx = ((len(sorted) + 1) // 2) - 1
                group[year] = sorted[idx]
    return data

def region_medians(data):
    """
    This function reads the data from filters and builds a list of dictionaries representing each region
    :param data: list - information about all filtered countries
    :return: list - contains dictionaries for each region
    """
    region_groups = []
    sub = {}
    sa = {}
    eca = {}
    lac = {}
    me = {}
    na = {}
    eap = {}
    for year in range(1960, 2016):
        sub[year] = []
        sa[year] = []
        eca[year] = []
        lac[year] = []
        me[year] = []
        na[year] = []
        eap[year] = []

    for nation in data:
        if nation.region == "Sub-Saharan Africa":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    sub[year].append(le[year])
        elif nation.region == "South Asia":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    sa[year].append(le[year])
        elif nation.region == "Europe & Central Asia":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    eca[year].append(le[year])
        elif nation.region == "Latin America & Caribbean":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    lac[year].append(le[year])
        elif nation.region == "Middle East & North Africa":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    me[year].append(le[year])
        elif nation.region == "North America":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    na[year].append(le[year])
        elif nation.region == "East Asia & Pacific":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    eap[year].append(le[year])

    region_groups.append(sub)
    region_groups.append(sa)
    region_groups.append(eca)
    region_groups.append(lac)
    region_groups.append(me)
    region_groups.append(na)
    region_groups.append(eap)
    medians = find_median(region_groups)
    return medians

def income_medians(data):
    """
    This function reads the data from filters and builds a list of dictionaries representing each region
    :param data: list - information about all filtered countries
    :return: list - contains dictionaries for each region
    """
    income_groups = []
    high = {}
    low = {}
    upper = {}
    lower = {}
    for year in range(1960, 2016):
        high[year] = []
        low[year] = []
        upper[year] = []
        lower[year] = []

    for nation in data:
        if nation.income == "Low income":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    low[year].append(le[year])
        elif nation.income == "High income":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    high[year].append(le[year])
        elif nation.income == "Upper middle income":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    upper[year].append(le[year])
        elif nation.income == "Lower middle income":
            le = nation.le_data
            for year in le.keys():
                if le[year] == 0.0:
                    continue
                else:
                    lower[year].append(le[year])

    income_groups.append(low)
    income_groups.append(upper)
    income_groups.append(lower)
    income_groups.append(high)
    medians = find_median(income_groups)
    return medians


def draw_graph():
    """
    Draws x-axis, y-axis and labels the axi
    """
    t.up()
    t.setpos((ORIGIN(), ORIGIN()))
    t.down()
    t.fd(X_AXIS_LEN())
    t.back(X_AXIS_LEN())
    t.left(90)
    t.fd(Y_AXIS_LEN())
    t.up()
    for num in range(90, -1, -10):
        t.back(1)
        t.right(90)
        if num != 50:
            t.back(15)
            t.write(str(num), False, align="left")
            t.fd(15)
        else:
            t.back(15)
            t.write(str(num), False, align="left")
            t.back(50)
            t.write("Life\nExp.", False, align="left")
            t.fd(65)
        if num != 0:
            t.left(90)
            t.back(44)
    t.left(90)
    t.back(10)
    t.right(90)
    t.write("1960", False)
    t.fd(X_AXIS_LEN()/2)
    t.left(90)
    t.back(20)
    t.right(90)
    t.write("Year", False)
    t.fd(Y_AXIS_LEN()/2)
    t.left(90)
    t.fd(20)
    t.right(90)
    t.write("2015", False)


def draw_income_graph(lst):
    """
    This function draws all components of a line graph and plots the data
    Prompts the user to hit enter key to continue
    :param lst: list - strings for keys
    """
    t.title("Life Expectancy versus Income Category")
    draw_graph()
    draw_key(lst)
    data = income_medians(filter_region(read_data("worldbank_life_expectancy"), "all"))
    plot_graph(data)
    t.write("Hit enter in the console to continue...")

def draw_region_graph(lst):
    """
    This function draws all components of a line graph and plots the data
    :param lst: list - strings for keys
    """
    t.reset()
    t.title("Life Expectancy versus Region")
    draw_graph()
    draw_key(lst)
    data = region_medians(filter_region(read_data("worldbank_life_expectancy"), "all"))
    plot_graph(data)
    t.done()

def main():
    """
    Plots the income graph, then it asks user to hit enter...
    If the user does hit enter, then it plots the region graph
    """
    money = ["Low income", "Upper middle income", "Lower middle income", "High income"]
    regions = ["Sub-Saharan Africa", "South Asia", "Europe & Central Asia", "Latin America & Caribbean", "Middle East & North Africa", "North America", "East Asia & Pacific"]
    draw_income_graph(money)
    user = input("Hit enter to clear turtle screen and draw region graph...")
    if user == "":
        draw_region_graph(regions)

main()