import scraperTwitter
import supabaseWriter
from supabase import *

# ##connect to supabase database

##Connect to supabase database

supabaseURL = "https://mznmolqfsdyplusolgwt.supabase.co"
supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im16bm1vbHFmc2R5cGx1c29sZ3d0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzc3NTIyNDMsImV4cCI6MTk5MzMyODI0M30.paVEfssvomg9Lq5c1QsjwrT4AhFYr4re55V9lsTf-hw"

# Create a client with the URL for your database and an anon API key

client = create_client(supabaseURL, supabaseKey)

query = "Asterix lang:fr "
limit = 200

tweets = scraperTwitter.get_tweets(query, limit)
print("Importation terminée : "+ str(len(tweets)) + " tweets trouvés")
count=0
for tweet in tweets:
    tweet = scraperTwitter.create_JSON(tweet)
    supabaseWriter.write_row(tweet)
    count+=1
    print( "Tweet " + str(count) + " / " + str(len(tweets)) + " importé")

##supabaseWriter.delete_all_rows("tweets")
