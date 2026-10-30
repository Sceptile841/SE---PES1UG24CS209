"""Programme schedule for a radio station.

Books show slots, lists the morning shows, checks slot timing and removes
slots.
"""
import os
import sqlite3

CONN = sqlite3.connect(":memory:")
CONN.execute(
    "CREATE TABLE slots ("
    "id INTEGER PRIMARY KEY, show TEXT, host TEXT, "
    "start_hour INTEGER, minutes INTEGER)"
)
# Secret is read from the environment, never hardcoded in source control.
STUDIO_PASSWORD = os.environ.get("STUDIO_PASSWORD", "")


def add_slot(show, host, start_hour, minutes):
    """Book a slot using a parameterised query (no SQL injection)."""
    CONN.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) "
        "VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a human readable label for a slot."""
    return f"{show} hosted by {host}"


def overlap_free(first_end_hour, second_start_hour):
    """Return True if the first slot ends before the second one starts.

    Replaces the old eval() of a formula string with plain arguments.
    """
    return first_end_hour <= second_start_hour


def morning_shows():
    """Return the names of all shows starting before noon."""
    rows = CONN.execute("SELECT show FROM slots WHERE start_hour < 12")
    return [row[0] for row in rows]


def remove_slot(slot_id):
    """Remove a slot by its id."""
    CONN.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Run a short demonstration."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free(7 + 1, 13), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()
