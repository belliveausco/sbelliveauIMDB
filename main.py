import requests
import secrets


# Scott Belliveau

def no_1_show():
    a = open("data.txt", "a+")
    a.write(f"Ratings for No 1 TV Show")
    a.write(f"\n")
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt5491994"  # look up tt number code for shows you are looking at
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for key, value in data.items():
        if key != 'ratings':
            a.write(f"{key, value}""\n")
        elif key == 'ratings':
            ratings_list = list(value)
            for x in ratings_list:
                a.write(f"{x}""\n")
    a.write(f"\n")
    a.close()


def no_50_show():
    a = open("data.txt", "a+")
    a.write(f"Ratings for No 50 TV Show")
    a.write(f"\n")
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt0081834"  # look up tt number code for shows you are looking at
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for key, value in data.items():
        if key != 'ratings':
            a.write(f"{key, value}""\n")
        elif key == 'ratings':
            ratings_list = list(value)
            for x in ratings_list:
                a.write(f"{x}""\n")
    a.write(f"\n")
    a.close()


def no_100_show():
    a = open("data.txt", "a+")
    a.write(f"Ratings for No 100 TV Show")
    a.write(f"\n")
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt0096697"  # look up tt number code for shows you are looking at
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for key, value in data.items():
        if key != 'ratings':
            a.write(f"{key, value}""\n")
        elif key == 'ratings':
            ratings_list = list(value)
            for x in ratings_list:
                a.write(f"{x}""\n")
    a.write(f"\n")
    a.close()


def no_200_show():
    a = open("data.txt", "a+")
    a.write(f"Ratings for No 200 TV Show")
    a.write(f"\n")
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt2100976"  # look up tt number code for shows you are looking at
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for key, value in data.items():
        if key != 'ratings':
            a.write(f"{key, value}""\n")
        elif key == 'ratings':
            ratings_list = list(value)
            for x in ratings_list:
                a.write(f"{x}""\n")
    a.write(f"\n")
    a.close()


def the_wheel_of_time():
    a = open("data.txt", "a+")
    a.write(f"Ratings for The Wheel of Time TV Show")
    a.write(f"\n")
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"  # look up tt number code for shows you are looking at
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for key, value in data.items():
        if key != 'ratings':
            a.write(f"{key, value}""\n")
        elif key == 'ratings':
            ratings_list = list(value)
            for x in ratings_list:
                a.write(f"Ratings")
                a.write(f"{x}""\n")
    a.write(f"\n")
    a.close()


def top_250_shows():
    a = open("data.txt", "a+")
    a.write(f"Top 250 TV Shows""\n\n""")
    loc = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    top_250_list = data["items"]
    for i in range(0, 250):
        top_250_dictionary = top_250_list[i]
        for key, value in top_250_dictionary.items():
            a.write(f"{(key, str(value))}""\n\n")
    a.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    no_1_show()
    no_50_show()
    no_100_show()
    no_200_show()
    the_wheel_of_time()
    top_250_shows()