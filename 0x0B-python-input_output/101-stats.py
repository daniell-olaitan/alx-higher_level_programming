#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def print_metrics(file_size, status_codes):
    """prints metrics"""
    res = f"File size: {file_size}\n"
    for s_c in sorted(status_codes):
        if status_codes[s_c] > 0:
            res = res + f"{s_c}: {status_codes[s_c]}\n"

    print(res, end="")


if __name__ == "__main__":
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    total_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            line = line.split()
            try:
                key = line[-2]
                if key in status_codes:
                    status_codes[key] += 1
                    total_size += int(line[-1])
                    line_count += 1
            except (IndexError, ValueError):
                pass

            if line_count == 10:
                print_metrics(total_size, status_codes)
                line_count = 0

        print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
