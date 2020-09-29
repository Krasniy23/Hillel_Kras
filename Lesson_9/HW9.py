import csv

o = 'tz_opendata_z01012020_po01092020.csv'
brand = {}
color = {}
year = {}
fuel = {}

def csv_reader():
    csv1 = csv.DictReader(o, delimiter=',')
    for row in csv1:
        if brand in row["BRAND"]:
            if (row["BRAND"] is None) or (row["BRAND"] == ""):
                pass
        if color in row["COLOR"]:
            if row["COLOR"] is None or (row["COLOR"] == ""):
                pass
        if year in row["MAKE_YEAR"]:
            if row["MAKE_YEAR"] is None or (row["MAKE_YEAR"] == ""):
                pass
        if fuel in row["FUEL"]:
            if row["FUEL"] is None or (row["FUEL"] == ""):
                pass
