import requests

def fetch_random_user_free_api():
    # url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    print(data)
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        # return [{"username": username, "country": country}]
        return username, country
    else:
        raise Exception("Failed to fetch data from the API")


def main():
    try:
        username, country = fetch_random_user_free_api()
        print(f"Username: {username}, \nCountry: {country}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()