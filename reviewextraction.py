from google_play_scraper import app

result = app(
    'com.nianticlabs.pokemongo',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)
f=open("guru99.txt", "w+")
f.write(""+str(result))
print(result)
