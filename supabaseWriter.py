from supabase import *

supabaseURL = "https://mznmolqfsdyplusolgwt.supabase.co"
supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im16bm1vbHFmc2R5cGx1c29sZ3d0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzc3NTIyNDMsImV4cCI6MTk5MzMyODI0M30.paVEfssvomg9Lq5c1QsjwrT4AhFYr4re55V9lsTf-hw"

# ##connect to supabase database
# Create a client with the URL for your database and an anon API key
client = create_client(supabaseURL, supabaseKey)

tweetTest = [{"username": "elonmusk", "content" :"Coucou test","likeCount": 0,"replyCount": 2,"retweetCount": 3,"quoteCount": 4}]

# Write a row into the tweets table
def write_row(tweet):
    response = client.from_("tweets").insert(tweet).execute()
    print(response)


#delete all the rows of the database
def delete_all_rows(database):
    response = client.from_(database).delete().execute()
    print(response)
