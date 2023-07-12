import requests
import json

from jobs.SystemDataCollector import *

def post_top_results():
    top_results = get_top_results()
    url = 'http://localhost:8000/api/save-top-results/'
    headers = {'Content-Type': 'application/json'}

    payload = {
        'cpu_data': top_results['cpu'],
        'memory_data': top_results['memory']
    }

    if top_results:
        print(top_results)
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.status_code == 201:
                print('Top results saved successfully.')
            else:
                print('Failed to save top results:', response.json().get('message'))
        except requests.exceptions.RequestException as e:
            print('Error:', str(e))
    else:
        print("No Data")

def main():
    post_top_results()

if __name__ == '__main__':
    main()




