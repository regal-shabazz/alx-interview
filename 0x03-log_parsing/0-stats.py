#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re

class LogParser:
    def __init__(self):
        self.total_file_size = 0
        self.status_codes_stats = {
            '200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0
        }

    def extract_input(self, input_line):
        '''Extracts sections of a line of an HTTP request log.'''
        pattern = r'\s*(?P<ip>\S+)\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]\s*"(?P<request>[^"]*)"\s*(?P<status_code>\S+)\s*(?P<file_size>\d+)'
        match = re.match(pattern, input_line)
        if match:
            status_code = match.group('status_code')
            file_size = int(match.group('file_size'))
            return {'status_code': status_code, 'file_size': file_size}
        return None

    def update_metrics(self, line_info):
        '''Updates the metrics from a given HTTP request log.'''
        if line_info:
            status_code = line_info.get('status_code', '0')
            if status_code in self.status_codes_stats:
                self.status_codes_stats[status_code] += 1
            self.total_file_size += line_info['file_size']

    def print_statistics(self):
        '''Prints the accumulated statistics of the HTTP request log.'''
        print(f'File size: {self.total_file_size}', flush=True)
        for status_code, num in sorted(self.status_codes_stats.items()):
            if num > 0:
                print(f'{status_code}: {num}', flush=True)

    def run(self):
        '''Starts the log parser.'''
        try:
            while True:
                line = input()
                line_info = self.extract_input(line)
                self.update_metrics(line_info)
                if len(self.status_codes_stats) % 10 == 0:
                    self.print_statistics()
        except (KeyboardInterrupt, EOFError):
            self.print_statistics()

if __name__ == '__main__':
    parser = LogParser()
    parser.run()