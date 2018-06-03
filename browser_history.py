import json
import sys

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print 'Pleast use in the format \'browser_history.py <file-name>\''
    else:
        with open(sys.argv[1]) as f:
            data = json.load(f)

        browser_history = data['Browser History']

        // TODO: Generate graph of average time spent searching during day

        // TODO: Generate graph of most frequent websites
