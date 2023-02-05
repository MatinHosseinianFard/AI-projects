m = 3
Australia = {
    'WA': {'color': 0, 'neighbours': ['NT', 'SA'], 'rem_val': [color for color in range(1, m+1)]},
    'NT': {'color': 0, 'neighbours': ['WA', 'SA', 'Q'], 'rem_val': [color for color in range(1, m+1)]},
    'SA': {'color': 0, 'neighbours': ['WA', 'NT', 'Q', 'NSW', 'V'], 'rem_val': [color for color in range(1, m+1)]},
    'Q': {'color': 0, 'neighbours': ['NT', 'SA', 'NSW'], 'rem_val': [color for color in range(1, m+1)]},
    'NSW': {'color': 0, 'neighbours': ['SA', 'Q', 'V'], 'rem_val': [color for color in range(1, m+1)]},
    'V': {'color': 0, 'neighbours': ['SA', 'NSW'], 'rem_val': [color for color in range(1, m+1)]},
    'T': {'color': 0, 'neighbours': [], 'rem_val': [color for color in range(1, m+1)]},
}

m = 4
Sweden = {
    'Norrbotten': {'color': 0, 'neighbours': ['Vasterbotten'], 'rem_val': [color for color in range(1, m+1)]},
    'Vasterbotten': {'color': 0, 'neighbours': ['Norrbotten', 'Jamtland', 'Vaster-norrland'], 'rem_val': [color for color in range(1, m+1)]},
    'Jamtland': {'color': 0, 'neighbours': ['Vasterbotten', 'Dalarna', 'Gavleborg', 'Vaster-norrland'], 'rem_val': [color for color in range(1, m+1)]},
    'Vaster-norrland': {'color': 0, 'neighbours': ['Vasterbotten', 'Jamtland', 'Gavleborg'], 'rem_val': [color for color in range(1, m+1)]},
    'Gavleborg': {'color': 0, 'neighbours': ['Vaster-norrland', 'Jamtland', 'Dalarna', 'Vasteras', 'Uppsala'], 'rem_val': [color for color in range(1, m+1)]},
    'Dalarna': {'color': 0, 'neighbours': ['Jamtland', 'Varmland', 'Orebro', 'Vasteras', 'Gavleborg'], 'rem_val': [color for color in range(1, m+1)]},
    'Varmland': {'color': 0, 'neighbours': ['Dalarna', 'VastraGotaland', 'Orebro'], 'rem_val': [color for color in range(1, m+1)]},
    'Orebro': {'color': 0, 'neighbours': ['Dalarna', 'Varmland', 'VastraGotaland', 'Ostergotland', 'Soderman-land', 'Vasteras'], 'rem_val': [color for color in range(1, m+1)]},
    'Vasteras': {'color': 0, 'neighbours': ['Dalarna', 'Orebro', 'Soderman-land', 'Uppsala', 'Gavleborg'], 'rem_val': [color for color in range(1, m+1)]},
    'Uppsala': {'color': 0, 'neighbours': ['Gavleborg', 'Vasteras', 'Stockholm'], 'rem_val': [color for color in range(1, m+1)]},
    'VastraGotaland': {'color': 0, 'neighbours': ['Varmland', 'Halland', 'Jonkoping', 'Orebro'], 'rem_val': [color for color in range(1, m+1)]},
    'Ostergotland': {'color': 0, 'neighbours': ['Orebro', 'Jonkoping', 'Kalmar', 'Soderman-land'], 'rem_val': [color for color in range(1, m+1)]},
    'Soderman-land': {'color': 0, 'neighbours': ['Vasteras', 'Orebro', 'Ostergotland', 'Stockholm'], 'rem_val': [color for color in range(1, m+1)]},
    'Stockholm': {'color': 0, 'neighbours': ['Uppsala', 'Soderman-land'], 'rem_val': [color for color in range(1, m+1)]},
    'Halland': {'color': 0, 'neighbours': ['VastraGotaland', 'Skane', 'Kronoberg', 'Jonkoping'], 'rem_val': [color for color in range(1, m+1)]},
    'Jonkoping': {'color': 0, 'neighbours': ['VastraGotaland', 'Halland', 'Kronoberg', 'Kalmar', 'Ostergotland'], 'rem_val': [color for color in range(1, m+1)]},
    'Kronoberg': {'color': 0, 'neighbours': ['Jonkoping', 'Halland', 'Skane', 'Blekinge', 'Kalmar'], 'rem_val': [color for color in range(1, m+1)]},
    'Kalmar': {'color': 0, 'neighbours': ['Ostergotland', 'Jonkoping', 'Kronoberg', 'Blekinge'], 'rem_val': [color for color in range(1, m+1)]},
    'Skane': {'color': 0, 'neighbours': ['Halland', 'Kronoberg', 'Blekinge'], 'rem_val': [color for color in range(1, m+1)]},
    'Blekinge': {'color': 0, 'neighbours': ['Kronoberg', 'Skane', 'Kalmar'], 'rem_val': [color for color in range(1, m+1)]},
    'Gotland': {'color': 0, 'neighbours': [], 'rem_val': [color for color in range(1, m+1)]}
}
