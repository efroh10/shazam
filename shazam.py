from getResponse import getResponse

search = input('What song would you like to search for?')

if(len(getResponse('search', 'term', search)) == 0):
    print('No songs match that search!')
else:
    hitList = getResponse('search', 'term', search)['tracks']['hits']

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

if(len(getResponse('songs/list-recommendations', 'key', key)) == 0):
    print('No Recommendations for This Song')
else:
    recommendations = getResponse('songs/list-recommendations', 'key', key)['tracks']
    for x in recommendations:
        print('Check out ' + x['title'] + ' by ' + x['subtitle'])
