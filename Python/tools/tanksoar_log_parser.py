import re
import pandas as pd

rx_dict = {
    'run': re.compile(r'Run: (?P<run>[0-9]+) '),
    'tank': re.compile(r'\[Tank: (?P<tank>[^]]*)\]'),
    'team': re.compile(r'\[Team: (?P<team>[0-9]+)\]'),
    'points': re.compile(r'\[Points: (?P<points>[-0-9]+)\]'),
    'status': re.compile(r'\[Status: (?P<status>[a-z]+)\]'),
    'kills': re.compile(r'\[Kills: (?P<kills>[0-9]+)\]'),
    'deaths': re.compile(r'\[Deaths: (?P<deaths>[0-9]+)\]'),
    'missiles_fired': re.compile(r'\[Missiles Fired: (?P<missiles_fired>[0-9]+)\]'),
    'energy_used': re.compile(r'\[Energy Used:(?P<energy_used>[0-9]+)\]'),
}


def _parse_line(line):
    keys = []
    matches = []
    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            keys.append(key)
            matches.append(match)
    return matches


def parse_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        line = file.readline()
        while line:
            line_stats = dict()
            dict_pairs = _parse_line(line)
            for pair in dict_pairs:
                key = list(pair.groupdict().keys())[0]
                value = list(pair.groupdict().values())[0]
                line_stats[key] = value

            line = file.readline()
            if line_stats:
                data.append(line_stats)
            #print(line_stats)
    data = pd.DataFrame(data)
    #data.set_index(['run', 'tank', 'team', 'status', 'kills', 'deaths', 'missiles_fired', 'energy_used', 'points'], inplace=True)
    data = data.apply(pd.to_numeric, errors='ignore')
    #data = data.groupby(level=data.index.names).first()
    #data = data.apply(pd.to_numeric, errors='ignore')
    return data


if __name__ == '__main__':
    filepath = 'tanksoar.log'
    output_file = 'tanksoar.csv'
    data = parse_file(filepath)
    data.to_csv(output_file)
    print(data)