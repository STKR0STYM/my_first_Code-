import time
import random

# ANSI Color Codes for styling
class Style:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

# Combined Database
world_data = {
    "Asia": {
        "Afghanistan": "Kabul", "Armenia": "Yerevan", "Azerbaijan": "Baku",
        "Bahrain": "Manama", "Bangladesh": "Dhaka", "Bhutan": "Thimphu",
        "Brunei": "Bandar Seri Begawan", "Cambodia": "Phnom Penh", "China": "Beijing",
        "Cyprus": "Nicosia", "Georgia": "Tbilisi", "India": "New Delhi",
        "Indonesia": "Jakarta", "Iran": "Tehran", "Iraq": "Baghdad",
        "Israel": "Jerusalem", "Japan": "Tokyo", "Jordan": "Amman",
        "Kazakhstan": "Astana", "Kuwait": "Kuwait City", "Kyrgyzstan": "Bishkek",
        "Laos": "Vientiane", "Lebanon": "Beirut", "Malaysia": "Kuala Lumpur",
        "Maldives": "Male", "Mongolia": "Ulaanbaatar", "Myanmar": "Naypyidaw",
        "Nepal": "Kathmandu", "North Korea": "Pyongyang", "Oman": "Muscat",
        "Pakistan": "Islamabad", "Palestine": "Jerusalem", "Philippines": "Manila",
        "Qatar": "Doha", "Russia": "Moscow", "Saudi Arabia": "Riyadh",
        "Singapore": "Singapore", "South Korea": "Seoul", "Sri Lanka": "Sri Jayawardenepura Kotte",
        "Syria": "Damascus", "Tajikistan": "Dushanbe", "Thailand": "Bangkok",
        "Timor-Leste": "Dili", "Turkey": "Ankara", "Turkmenistan": "Ashgabat",
        "United Arab Emirates": "Abu Dhabi", "Uzbekistan": "Tashkent", "Vietnam": "Hanoi",
        "Yemen": "Sana'a"
    },
    "Africa": {
        "Algeria": "Algiers", "Angola": "Luanda", "Benin": "Porto-Novo",
        "Botswana": "Gaborone", "Burkina Faso": "Ouagadougou", "Burundi": "Gitega",
        "Cabo Verde": "Praia", "Cameroon": "Yaounde", "Chad": "N'Djamena",
        "Comoros": "Moroni", "Djibouti": "Djibouti", "Egypt": "Cairo",
        "Eritrea": "Asmara", "Eswatini": "Mbabane", "Ethiopia": "Addis Ababa",
        "Gabon": "Libreville", "Gambia": "Banjul", "Ghana": "Accra",
        "Guinea": "Conakry", "Kenya": "Nairobi", "Lesotho": "Maseru",
        "Liberia": "Monrovia", "Libya": "Tripoli", "Madagascar": "Antananarivo",
        "Malawi": "Lilongwe", "Mali": "Bamako", "Mauritania": "Nouakchott",
        "Mauritius": "Port Louis", "Morocco": "Rabat", "Mozambique": "Maputo",
        "Namibia": "Windhoek", "Niger": "Niamey", "Nigeria": "Abuja",
        "Rwanda": "Kigali", "Senegal": "Dakar", "Seychelles": "Victoria",
        "Sierra Leone": "Freetown", "Somalia": "Mogadishu", "South Africa": "Pretoria",
        "South Sudan": "Juba", "Sudan": "Khartoum", "Tanzania": "Dodoma",
        "Togo": "Lome", "Tunisia": "Tunis", "Uganda": "Kampala",
        "Zambia": "Lusaka", "Zimbabwe": "Harare", "Algeria":  "Algiers", "Kenya": "Nairobi", "Egypt": "Cairo",
        "Nigeria": "Abuja", "South Africa": "Pretoria", "Ghana": "Accra"
    },
    "Europe": {
        "Albania": "Tirana", "Andorra": "Andorra la Vella", "Austria": "Vienna",
        "Belarus": "Minsk", "Belgium": "Brussels", "Bosnia and Herzegovina": "Sarajevo",
        "Bulgaria": "Sofia", "Croatia": "Zagreb", "Czech Republic": "Prague",
        "Denmark": "Copenhagen", "Estonia": "Tallinn", "Finland": "Helsinki",
        "France": "Paris", "Germany": "Berlin", "Greece": "Athens",
        "Hungary": "Budapest", "Iceland": "Reykjavik", "Ireland": "Dublin",
        "Italy": "Rome", "Latvia": "Riga", "Liechtenstein": "Vaduz",
        "Lithuania": "Vilnius", "Luxembourg": "Luxembourg", "Malta": "Valletta",
        "Moldova": "Chisinau", "Monaco": "Monaco", "Montenegro": "Podgorica",
        "Netherlands": "Amsterdam", "North Macedonia": "Skopje", "Norway": "Oslo",
        "Poland": "Warsaw", "Portugal": "Lisbon", "Romania": "Bucharest",
        "San Marino": "San Marino", "Serbia": "Belgrade", "Slovakia": "Bratislava",
        "Slovenia": "Ljubljana", "Spain": "Madrid", "Sweden": "Stockholm",
        "Switzerland": "Bern", "Ukraine": "Kyiv", "United Kingdom": "London",
        "Vatican City": "Vatican City","France": "Paris", "Germany": "Berlin", "Italy": "Rome",
        "Spain": "Madrid", "United Kingdom": "London", "Sweden": "Stockholm"
    },
    "North_America": {
       "Antigua and Barbuda": "Saint John's", "Bahamas": "Nassau", "Barbados": "Bridgetown",
        "Belize": "Belmopan", "Canada": "Ottawa", "Costa Rica": "San Jose",
        "Cuba": "Havana", "Dominica": "Roseau", "Dominican Republic": "Santo Domingo",
        "El Salvador": "San Salvador", "Grenada": "Saint George's", "Guatemala": "Guatemala City",
        "Haiti": "Port-au-Prince", "Honduras": "Tegucigalpa", "Jamaica": "Kingston",
        "Mexico": "Mexico City", "Nicaragua": "Managua", "Panama": "Panama City",
        "Saint Kitts and Nevis": "Basseterre", "Saint Lucia": "Castries",
        "Saint Vincent and the Grenadines": "Kingstown", "Trinidad and Tobago": "Port of Spain",
        "United States": "Washington, D.C."
    },
    "South_America": {
         "Argentina": "Buenos Aires", "Bolivia": "Sucre", "Brazil": "Brasilia",
         "Chile": "Santiago", "Colombia": "Bogota", "Ecuador": "Quito",
         "Guyana": "Georgetown", "Paraguay": "Asuncion", "Peru": "Lima",
         "Suriname": "Paramaribo", "Uruguay": "Montevideo", "Venezuela": "Caracas"
    },
   "Oceania":{
         "Australia": "Canberra", "Fiji": "Suva", "Kiribati": "Tarawa",
         "Marshall Islands": "Majuro", "Micronesia": "Palikir", "Nauru": "Yaren",
         "New Zealand": "Wellington", "Palau": "Ngerulud", "Papua New Guinea": "Port Moresby",
         "Samoa": "Apia", "Solomon Islands": "Honiara", "Tonga": "Nuku'alofa",
         "Tuvalu": "Funafuti", "Vanuatu": "Port Vila"
    },


}

def quiz():
    print(f"{Style.HEADER}{Style.BOLD}--- Global Capital Quiz ---{Style.ENDC}")
    print(f"{Style.GREEN}Choose a region: 1: Asia, 2: Africa, 3: Europe, 4: North_America, 5: South_America, 6: Oceania")

    choice = input(f"{Style.BLUE}Enter number (1-6): ")
    regions = ["Asia", "Africa", "Europe", "North_America", "South_America", "Oceania"]

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print(f"{Style.RED}Invalid choice! Exiting.{Style.ENDC}")
        return

    region_name = regions[int(choice)-1]
    data = world_data[region_name]
    countries = list(data.keys())
    random.shuffle(countries)

    coins = 0
    print(f"\n{Style.BOLD}Starting {region_name} Quiz! Type 'exit' at any time to quit.{Style.ENDC}\n")

    for country in countries:
        user_answer = input(f"What is the capital of {Style.BLUE}{country}{Style.ENDC}? ").strip()

        if user_answer.lower() == 'exit':
            print(f"{Style.RED}Quiz terminated by user.{Style.ENDC}")
            break

        if user_answer.lower() == data[country].lower():
            coins += 10
            print(f"{Style.GREEN}Correct!{Style.ENDC} Coins: {coins}")
        else:
            print(f"{Style.RED}Wrong!{Style.ENDC} It was {data[country]}.")

        print("-" * 30)
        time.sleep(0.5)

    print(f"\n{Style.BOLD}Game Over! Total coins: {coins}{Style.ENDC}")

if __name__ == "__main__":
    quiz()
