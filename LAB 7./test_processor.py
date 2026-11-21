from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label


@given(st.text() | st.none())
def test_nights_stayed_no_crash(s):
    try:
        nights_stayed(s)
    except Exception as e:
        assert False, f"nights_stayed crashed with: {e!r} on input {s!r}"


@given(st.text() | st.none())
def test_room_floor_no_crash(s):
    try:
        room_floor(s)
    except Exception as e:
        assert False, f"room_floor crashed with: {e!r} on input {s!r}"


@given(st.text() | st.none())
def test_booking_label_no_crash(s):
    try:
        booking_label(s)
    except Exception as e:
        assert False, f"booking_label crashed with: {e!r} on input {s!r}"


# ---- Extra property checks: results must be sane, not just non-crashing ----

@given(st.integers(0, 10**6), st.integers(0, 10**6))
def test_nights_stayed_valid_range(a, b):
    result = nights_stayed(f"{a}-{b}")
    if b >= a:
        assert result == b - a
    else:
        assert result is None


@given(st.text() | st.none())
def test_nights_stayed_never_negative(s):
    result = nights_stayed(s)
    assert result is None or result >= 0


@given(st.text(alphabet="ABCDEFabcdef", min_size=1, max_size=3), st.integers(100, 999))
def test_room_floor_valid(letter, num):
    assert room_floor(f"{letter}-{num}") == num // 100


@given(st.text() | st.none())
def test_room_floor_range(s):
    result = room_floor(s)
    assert result is None or 0 <= result <= 9


@given(st.lists(st.text(alphabet="abcdefghij", min_size=1, max_size=8), min_size=1, max_size=6))
def test_booking_label_valid(names):
    label = booking_label(", ".join(names))
    assert label == names[0][0].upper() + names[0][1:] + f" +{len(names) - 1}"
