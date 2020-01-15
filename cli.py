import click
from requests import get


def validate_token(token):
    weather = get("http://api.weatherstack.com/current?access_key=" + token + "&query=london")
    data = weather.json()
    if list(data)[1] == "error":
        raise ValueError("Token is not valid")
    return token


@click.command()
@click.option('--city', prompt='enter cities', help='enter cities')
@click.option('--token', prompt='Your token', help='enter token')
@click.option('--units', '--T', prompt='enter units', help='desired units')
def main(city, token, units):
    validate_token(token)
    units_type = 'f'
    if units == 'Celsius':
        units_type = 'm'
    city_list = city.split(",")
    for x in city_list:
        weather = get(
            "http://api.weatherstack.com/current?access_key=" + token + "&query=" + x + "&units=" + units_type)
        data = weather.json()
        temperature = data["current"]["temperature"]
        print("the weather in", x, "today is", temperature, units)


if __name__ == '__main__':
    main()
