def csv_string_to_array(csv_string):
    items = []
    in_quotes = False
    current_item = ""
    for char in csv_string:
        if char == "," and not in_quotes:
            items.append(current_item)
            current_item = ""
        elif char == "\"":
            in_quotes = not in_quotes
        else:
            current_item += char

    return items


def main():
    file = "shiller_data.csv"
    data = []
    with open(file, "r") as f:
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            points = csv_string_to_array(line)
            dateparts = points[0].split(".")
            if (len(dateparts) < 2):
                continue
            obj = {
                "year": int(dateparts[0]),
                "month": int(dateparts[1]),
                "sp_composite_price": float(points[1]),
                "dividend": float(points[2]),
                "earnings": float(points[3]),
                "cpi": float(points[4]),
                "date_fraction": float(points[5]),
                "long_interest_rate_gs10": float(points[6]),
                "real_price": float(points[7]),
                "real_dividend": float(points[8]),
                "real_total_return_price": float(points[9].replace(',', "")),
                "real_earnings": float(points[10].replace(',', "")),
                "real_tr_scaled_earnings": float(points[11].replace(',', "")),
                "cape": float(points[12].replace(',', "")),
                "tr_cape": float(points[13].replace(',', "")),
                "excess_cape_yield": float(points[14].replace('%', "")),
                "monthly_total_bond_returns": float(points[15]),
                "real_total_bond_returns": float(points[16]),
            }
            data.append(obj)

    return data
