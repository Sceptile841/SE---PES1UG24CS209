import re

_DIGITS = re.compile(r"[0-9]+")  # ASCII digits only (int() also accepts unicode digits)


def nights_stayed(days):
    """Return number of nights for 'in-out' (e.g. '12-15'), or None if invalid."""
    if not isinstance(days, str):
        return None
    parts = days.strip().split('-')
    if len(parts) != 2:
        return None
    check_in, check_out = (p.strip() for p in parts)
    if not (_DIGITS.fullmatch(check_in) and _DIGITS.fullmatch(check_out)):
        return None
    nights = int(check_out) - int(check_in)
    if nights < 0:          # check-out before check-in is invalid
        return None
    return nights


def room_floor(room_code):
    """Return the floor (first digit of room number) for 'D-305', or None if invalid."""
    if not isinstance(room_code, str):
        return None
    parts = room_code.strip().split('-')
    if len(parts) != 2:
        return None
    number = parts[1].strip()
    if not _DIGITS.fullmatch(number):
        return None
    return int(number[0])


def booking_label(names_csv):
    """Return 'Lead +N' for a CSV of guest names, or None if invalid/empty."""
    if not isinstance(names_csv, str):
        return None
    names = [n.strip() for n in names_csv.split(',') if n.strip()]
    if not names:
        return None
    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result if result is not None else "Invalid input")

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result if result is not None else "Invalid input")

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
