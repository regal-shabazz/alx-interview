#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys

class LogParser:
    def __init__(self):
        self.total_file_size = 0
        self.status_codes_stats = {
            '200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0
        }
        self.line_count = 0

    def parse_line(self, line):
        '''Parse a single line of the log.'''
        parts = line.split()
        if len(parts) == 7:
            status_code = parts[-2]
            if status_code.isdigit() and status_code in self.status_codes_stats:
                return {
                    'status_code': status_code,
                    'file_size': int(parts[-1])
                }
        return None

    def update_stats(self, line_info):
        '''Update statistics based on the parsed line.'''
        if line_info:
            status_code = line_info['status_code']
            file_size = line_info['file_size']
            self.total_file_size += file_size
            self.status_codes_stats[status_code] += 1
            self.line_count += 1

    def print_statistics(self):
        '''Print current statistics.'''
        print(f'Total file size: {self.total_file_size}')
        for code, count in sorted(self.status_codes_stats.items()):
            if count > 0:
                print(f'{code}: {count}')
        sys.stdout.flush()

    def run(self):
        '''Start parsing and print statistics after every 10 lines.'''
        try:
            for line in sys.stdin:
                line_info = self.parse_line(line.strip())
                if line_info:
                    self.update_stats(line_info)
                if self.line_count % 10 == 0:
                    self.print_statistics()
        except KeyboardInterrupt:
            self.print_statistics()

if __name__ == '__main__':
    parser = LogParser()
    parser.run()