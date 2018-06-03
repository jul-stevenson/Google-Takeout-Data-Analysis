import json
import sys
import time

from matplotlib import pyplot

"""
Generate a dictionary describing search frequency per hour.

Args:
    browser_history: List of searches
Returns:
    relative_frequency_per_hour: Dict of hour (military time) to search frequency
"""
def GenerateRelativeFrequencyPerHour(browser_history):
    hour_totals = [0] * 24
    relative_frequency_per_hour = [0] * 24
    total_searches = 0.0

    for search in browser_history:
        total_searches += 1
        usec_time = search['time_usec']
        hour = int(time.strftime("%H", time.gmtime(usec_time)))
        hour_totals[hour] += 1


    for i in range(len(relative_frequency_per_hour)):
        relative_frequency_per_hour[i] = hour_totals[i]/total_searches

    return relative_frequency_per_hour

def PlotRelativeFrequencyPerHour(search_frequency_per_hour):
    p = pyplot.plot(list(range(0, 24)), search_frequency_per_hour)
    pyplot.xlim(0, 24)
    pyplot.ylim(ymin=0)
    pyplot.xlabel('Hour')
    pyplot.ylabel('Frequency')
    pyplot.title('Relative Search Frequency Per Hour')
    pyplot.savefig('relative_search_frequency_per_hour.png')

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print 'Pleast use in the format \'browser_history.py <file-name>\''
    else:
        with open(sys.argv[1]) as f:
            data = json.load(f)

        browser_history = data['Browser History']

        relative_frequency_per_hour = GenerateRelativeFrequencyPerHour(browser_history)
        PlotRelativeFrequencyPerHour(relative_frequency_per_hour)

        # TODO: Generate graph of most frequent websites
