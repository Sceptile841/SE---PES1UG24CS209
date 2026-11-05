"""Lab 6 - Code (line) coverage tests for hotel_booking.py"""
import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# ---------- booking_cost ----------
def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000


def test_peak_extra_guests_long_stay():
    # rate 6000 + 1500 = 7500 ; 7 nights = 52500 ; +2 guests*500*7 = 7000 -> 59500 ; -10% -> 53550
    assert booking_cost("suite", 7, 4, True) == 53550


def test_unknown_room_raises():
    with pytest.raises(ValueError):
        booking_cost("penthouse", 2, 2, False)


def test_invalid_nights_raises():
    with pytest.raises(ValueError):
        booking_cost("standard", 0, 2, False)


# ---------- cancellation_refund ----------
def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000


def test_half_refund_non_member():
    assert cancellation_refund(1000, 3, False) == 500


def test_no_refund_member_bonus():
    assert cancellation_refund(1000, 0, True) == 250


# ---------- room_upgrade ----------
def test_no_rooms_free():
    assert room_upgrade("standard", True, 0) == "standard"


def test_standard_member_upgrade():
    assert room_upgrade("standard", True, 3) == "deluxe"


def test_deluxe_member_upgrade():
    assert room_upgrade("deluxe", True, 3) == "suite"
