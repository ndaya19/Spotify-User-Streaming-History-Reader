Just something I made because all the websites I've seen that provide this service are locked behind a paywall.

How to use:

1. Download spotify account data here: https://www.spotify.com/uk/account/privacy/

2. Place the "StreamingHistory" JSON files in the same directory as main.py (or edit the directory variable to where you put them

3. If you want stats from a specific date, edit the cutoff_date variable. By default this is set to December 31 2023 so only stats from January 1 2024 and onwards are processed

4. Otherwise, set lifetime to True to process data from the earliest date recorded in the StreamingHistory JSON files

5. Stats are displayed in descending order, by default showing the top 10 entries. Edit the items_to_display variable to change how many entries are displayed. 

6. Run the script