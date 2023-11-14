import csv

def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data

def count_champions(data):
    champion_count = {}
    for row in data:
        player_name = row[0]
        if player_name in champion_count:
            champion_count[player_name] += 1
        else:
            champion_count[player_name] = 1
    return champion_count

def get_unique_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)

def display_champion_info(champion_count, countries):
    print("Wimbledon Champions:")
    for player, wins in champion_count.items():
        print(f"{player} {wins}")

    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)

def main():
    wimbledon_data = read_wimbledon_data("wimbledon.csv")
    champion_count = count_champions(wimbledon_data)
    countries = get_unique_countries(wimbledon_data)
    display_champion_info(champion_count, countries)

if __name__ == "__main":
    main()
