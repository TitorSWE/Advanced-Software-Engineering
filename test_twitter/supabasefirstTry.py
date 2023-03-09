from scraperTwitter import *
from supabase import *
from main import client


# Write data into the "test" tweet column of the "test" table
response = client.from_("test").insert({"username": "elonmusk", "content" : "Coucou test"}).execute()
# Get a single row from the "test" table
response = client.from_("test").select("*").execute()
print(response)
