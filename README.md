# 240801-spotify_song_popularity
This is a project which lists the most popular songs of an artist on spotify ordered by the popularity score by spotify. Before running the program, you have to make a spotify dev account, create an app, get the client_id + client_secret and put these in a .env file with the variable names CLIENT_ID and CLIENT_SECRET. To use the program, run the program with the spotify artist url as the first argument. To get the artist url, search up the artist on the webapp and extract the artist url from the url. Here are some examples:
- python3 main.py 2YZyLoL8N0Wb9xBt1NhZWg **(Kendrick Lamar)**
- python3 main.py 6RHTUrRF63xao58xh9FXYJ **(IVE)**
- python3 main.py 4gzpq5DPGxSnKTe4SA8HAU **(Coldplay)**

This was my first project using the spotify api. The setup was pretty similar to making a discord bot but with a couple less steps. I will probably revisit the spotify api some time in the future with a project that involves using user data such as listing their top tracks.

It was quite time consuming figuring out how to store the bearer token to authorise the api requests since it involved writing to a file under the condition that the last token was extracted less than an hour ago. Overall, it required a variety of techniques but none of them were too difficult.
