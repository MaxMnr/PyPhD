"""General-purpose utilities."""

def convert_covid_label(value):
    # Assure value is a str 
    assert isinstance(value, str)
    if value in ["Positif faible", "Positif"]:
        return 1
    elif value in ["Négatif"]:
        return 0
    else:
        return -1