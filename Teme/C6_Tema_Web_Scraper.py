import requests
from bs4 import BeautifulSoup


def scrape_web_data():
    # URL we want to scrape
    url = "https://www.lpf.ro/liga-1"

    # PING PONG with URL
    page = requests.get(url)

    # check if the server respond
    if page.status_code == 200:

        # we use BSoup for parsing the content
        soup = BeautifulSoup(page.text, "html.parser")

        # Save title and data
        clasament_title = soup.find('div', class_="section-title").text.strip()
        tabel_with_results_playoff = soup.find_all('tr', class_='echipa_row Calificare playoff')
        tabel_with_results_playout = soup.find_all('tr', class_='echipa_row Grupă playout')

        data_list = []

        for row in tabel_with_results_playoff:
            team_pos_playoff = row.find('td', class_='poz').text.strip()
            team_name_playoff = row.find('td', class_='echipa').text.strip()
            team_form_playoff = row.find('td', class_='hiddenMobile forma_echipa_content').text.strip()
            team_point_playoff = row.find('td', class_='puncte').text.strip()

            data_list.append("Pozitia: {:<5} | Nume echipa: {:<25} | Format meciuri: {:<10} | Puncte: {:<5}".
                             format(team_pos_playoff, team_name_playoff, team_form_playoff, team_point_playoff))

        for row in tabel_with_results_playout:
            team_pos_playout = row.find('td', class_='poz').text.strip()
            team_name_playout = row.find('td', class_='echipa').text.strip()
            team_form_playout = row.find('td', class_='hiddenMobile forma_echipa_content').text.strip()
            team_point_playout = row.find('td', class_='puncte').text.strip()

            # Formating the data
            data_list.append("Pozitia: {:<5} | Nume echipa: {:<25} | Format meciuri: {:<10} | Puncte: {:<5}".
                             format(team_pos_playout, team_name_playout, team_form_playout, team_point_playout))

        return clasament_title, data_list


# Method to write data to file
def write_data_to_file(locatie, data):
    with open(locatie, 'w') as file:
        file.write('\n'.join(data))


# Method for reading from file
def read_data_from_file(file):
    try:
        with open(file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file} not found ...")
        return None


# Setting the file_path
file_path = "rezultat.txt"

clasament, date_noi = scrape_web_data()

if date_noi:
    write_data_to_file(file_path, [f"{clasament}"] + date_noi)

read_data = read_data_from_file(file_path)
if read_data:
    print(read_data)
