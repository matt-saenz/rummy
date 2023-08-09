"""Utilities for the play_rummy.py script."""


def get_int(message: str, allow_empty: bool = False) -> int:
    resp = input(message + ": ")

    if allow_empty:
        if resp == "":
            return 0

    while True:
        try:
            integer = int(resp)
            break
        except ValueError:
            resp = input("Oops! Input must be an integer. Please try again: ")

    return integer


def confirm(message: str) -> bool:
    resp = input(message + " (y/n)? ")

    while True:
        if resp in {"y", "n"}:
            break

        resp = input("Oops! Valid inputs are 'y' or 'n'. Please try again: ")

    return resp == "y"
