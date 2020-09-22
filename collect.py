from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()
kw_list = ['aws', 'azure']

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=kw_list)

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print("Printing interest over time for {}".format(str(kw_list)))
print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print("Printing interest by region for {}".format(str(kw_list)))
print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print("Printing related queries for {}".format(str(kw_list)))
print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print("Printing trending searches")
print(trending_searches_df.head())

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print("Printing today's searches")
print(today_searches_df.head())

# Get Google Top Charts
# More detail on arguments https://pypi.org/project/pytrends/#top-charts
year = 2018
geo = 'DE' # GLOBAL or two letter country shortcut (e.g. DE, FR, US)
language = 'en-US'
timezone = 0
top_charts_df = pytrend.top_charts(year, hl=language, tz=timezone, geo=geo)
print("Printing search charts for year {} and region {}".format(year, geo))
print(top_charts_df.head())

# Get Google Keyword Suggestions
kw = 'azure'
suggestions_dict = pytrend.suggestions(keyword=kw)
print("Printing keyword suggestions for {}".format(kw))
print(suggestions_dict)

# Get historical Google Interest
historical_interest_df = pytrend.get_historical_interest(kw_list)
print("Printing the historical Google interest over time for the following keywords {}".format(str(kw_list)))
print(historical_interest_df.head())
print(historical_interest_df.tail())
print(historical_interest_df.shape)