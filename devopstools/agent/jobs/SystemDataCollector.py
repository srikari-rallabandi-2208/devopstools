import subprocess
import json
import time

def get_top_results():
    try:
        command = "top -b -n 1 -o %CPU | head -n 17"  # Adjust the command based on your requirements
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        lines = output.strip().split('\n')
        cpu_data = lines[6:13]  # Extract CPU data from the output
        mem_data = lines[14:17]  # Extract memory data from the output

        top_data = {
            'cpu': cpu_data,
            'memory': mem_data
        }

        return top_data
    except subprocess.CalledProcessError as e:
        print("Error executing top command:", e)
        return None

def get_ps_results():
    try:
        command = "ps -ef --no-headers -o pid,ppid,user,%cpu,%mem,cmd"
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        lines = output.strip().split('\n')
        headers = ['PID', 'PPID', 'User', '%CPU', '%MEM', 'Command']
        ps_data = []

        for line in lines:
            line_data = line.split(None, 5)
            ps_entry = {header: value for header, value in zip(headers, line_data)}
            ps_data.append(ps_entry)

        return ps_data
    except subprocess.CalledProcessError as e:
        print("Error executing ps command:", e)
        return None


def save_results_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print("Results saved to", data, filename)

def main():
    time_period = 5  # Time period in seconds for which the top command will be executed
    filename = 'top_results.json'  # Name of the output JSON file

    while True:
        top_results = get_ps_results() #get_top_results()
        if top_results:
            save_results_to_json(top_results, filename)
        time.sleep(time_period)

if __name__ == '__main__':
    main()
