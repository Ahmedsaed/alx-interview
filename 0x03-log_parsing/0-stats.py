#!/usr/bin/python3
"""Parse log file and print stats"""
import re


def print_stats(total_size, status_counts):
    """Print stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Parse log file and print stats"""
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[([\d\- :.]+)\] "'\
              r'(GET [^"]+ HTTP/1\.1)" (\d+) (\d+)'

    total_size = 0
    total_lines = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}

    try:
        while True:
            log_line = input()

            match = re.match(pattern, log_line)

            if match:
                file_size = int(match.group(5))
                total_size += file_size

                status_code = int(match.group(4))
                if status_code in status_counts:
                    status_counts[status_code] += 1

                total_lines += 1

                if total_lines % 10 == 0:
                    print_stats(total_size, status_counts)
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
