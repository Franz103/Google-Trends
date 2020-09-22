import collect # import local collect file
from pytrends.request import TrendReq


if __name__ == "__main__":
    # Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq()
    kw_list = ['aws', 'azure']
    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=kw_list)

    interest_over_time_df = collect.get_interest_over_time(pytrend,kw_list)
    
    interest_by_region_df = collect.get_interest_by_region(pytrend,kw_list)

    related_queries_dict = collect.get_related_queries(pytrend, kw_list)

    trending_searches_df = collect.get_trending_searches(pytrend)

    today_searches_df = collect.get_today_searches()

    year = 2018
    geo = 'DE' # GLOBAL or two letter country shortcut (e.g. DE, FR, US)
    language = 'en-US'
    timezone = 0
    top_charts_df = collect.get_top_charts(year, geo, language, timezone)

    kw = 'azure'
    suggestion_dict = collect.get_suggestions(kw)

    historical_interest_df = collect.get_historical_interest(pytrend, kw_list)
    