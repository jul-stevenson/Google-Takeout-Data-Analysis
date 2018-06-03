import json
import sys
import time

"""
Generate a dictionary describing search frequency per hour.

Args:
    browser_history: List of searches
Returns:
    search_frequency_per_hour: Dict of hour (military time) to search frequency
"""
def GenerateSearchFrequencyPerHour(browser_history):
    hour_totals = [0] * 24
    search_frequency_per_hour = [0] * 24
    total_searches = 0.0

    for search in browser_history:
        total_searches += 1
        usec_time = search['time_usec']
        hour = int(time.strftime("%H", time.gmtime(usec_time)))
        hour_totals[hour] += 1


    for i in range(len(search_frequency_per_hour)):
        search_frequency_per_hour[i] = hour_totals[i]/total_searches

    return search_frequency_per_hour




if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print 'Pleast use in the format \'browser_history.py <file-name>\''
    else:
        with open(sys.argv[1]) as f:
            data = json.load(f)

        browser_history = data['Browser History']

        # TODO: Generate graph of average time spent searching during day
        GenerateSearchFrequencyPerHour(browser_history)

        # TODO: Generate graph of most frequent websites
