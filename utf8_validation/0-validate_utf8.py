#!/usr/bin/python3
"""Validate UTF-8 encoding."""


def validUTF8(data):
    """Return True if data is valid UTF-8."""
    remaining = 0
    min_cont = 0x80
    max_cont = 0xBF

    for number in data:
        byte = number & 0xFF

        if remaining > 0:
            if not min_cont <= byte <= max_cont:
                return False

            remaining -= 1
            min_cont = 0x80
            max_cont = 0xBF

        else:
            if byte <= 0x7F:
                continue

            elif 0xC2 <= byte <= 0xDF:
                remaining = 1

            elif 0xE0 <= byte <= 0xEF:
                remaining = 2
                if byte == 0xE0:
                    min_cont = 0xA0
                elif byte == 0xED:
                    max_cont = 0x9F

            elif 0xF0 <= byte <= 0xF4:
                remaining = 3
                if byte == 0xF0:
                    min_cont = 0x90
                elif byte == 0xF4:
                    max_cont = 0x8F

            else:
                return False

    return remaining == 0
