#!/usr/bin/python3
"""Read HTTP logs and calculate statistics."""

import re
import sys


VALID_CODES = (200, 301, 400, 401, 403, 404, 405, 500)

LOG_PATTERN = re.compile(
    r'^(?:\d{1,3}\.){3}\d{1,3} - \[[^\]]+\] '
    r'"GET /projects/260 HTTP/1\.1" '
    r'(?P<status>\S+) (?P<size>\d+)$'
)


def print_stats(total_size, counts):
    """Print total file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in VALID_CODES:
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))

    sys.stdout.flush()


def main():
    """Read log entries and display cumulative statistics."""
    total_size = 0
    counts = {code: 0 for code in VALID_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            match = LOG_PATTERN.match(line.rstrip('\r\n'))

            if match:
                total_size += int(match.group('size'))

                try:
                    status = int(match.group('status'))
                except ValueError:
                    status = None

                if status in counts:
                    counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
