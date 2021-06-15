import requests

search = input('What song would you like to search for?')

url = "https://shazam.p.rapidapi.com/search"

querystring = {
    "term": search,  # no need to use curly braces or anything?
    "locale": "en-US",
    "offset": "0",
    "limit": "5"
}

headers = {
    'x-rapidapi-key': "4819b84ebdmshd3385dc9375d94cp104332jsnf63093179aec",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

response = requests.request(
    "GET", url, headers=headers, params=querystring
)

hitList = response.json()['tracks']['hits']

counter = 1

for x in hitList:
    print(
        f'{counter}: ' +
        x['track']['title'] +
        ' by ' + x['track']['subtitle']
    )
    counter += 1

suggest = int(input(
    'Enter the number of the correct song to get recommendations'
))

key = hitList[suggest-1]['track']['key']

url2 = "https://shazam.p.rapidapi.com/songs/list-recommendations"

querystring2 = {
    "key": key,  # no need to use curly braces or anything?
    "locale": "en-US"
}

response2 = requests.request(
    "GET", url2, headers=headers, params=querystring2
)

recommendations = response2.json()['tracks']

for x in recommendations:
    print('Check out ' + x['title'] + ' by ' + x['subtitle'])
