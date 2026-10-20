#!/usr/bin/python3
"""Parse HTTP logs and calculate statistics."""

import sys


VALID_CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_stats(total_size, counts):
    """Print cumulative log statistics."""
    print("File size: {}".format(total_size))

    for code in VALID_CODES:
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))

    sys.stdout.flush()


def main():
    """Read log lines and calculate cumulative statistics."""
    total_size = 0
    counts = {code: 0 for code in VALID_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    file_size = int(parts[-1])
                    total_size += file_size
                except ValueError:
                    pass

                try:
                    status = int(parts[-2])
                    if status in counts:
                        counts[status] += 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
