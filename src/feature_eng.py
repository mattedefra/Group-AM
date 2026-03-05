import pandas as pd
import numpy as np


FEATURE_COLS = [
    "lead_time",
    "arrival_date_year",
    "arrival_date_month",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "babies",
    "meal",
    "reserved_room_type",
    "deposit_type",
    "previous_cancellations",
    "previous_bookings_not_canceled",
    "market_segment",
    "distribution_channel",
    "booking_changes",
    "total_of_special_requests",
    "adr",
    "customer_type",
    "required_car_parking_spaces",
    "days_in_waiting_list",
    "is_repeated_guest",
    "hotel"
]


def feature_engineering(X: pd.DataFrame) -> pd.DataFrame:

    X = X.copy()

    # Keep only expected columns
    keep = [c for c in FEATURE_COLS if c in X.columns]
    X = X[keep].copy()

    # Standardize common "fake missing" strings
    X = X.replace({
        "": np.nan,
        " ": np.nan,
        "N/A": np.nan,
        "na": np.nan,
        "NA": np.nan
    })

    # Strip whitespace for categoricals
    obj_cols = X.select_dtypes(include=["object"]).columns
    for c in obj_cols:
        X[c] = X[c].str.strip()

    # ----------------------------
    # Feature Engineering
    # ----------------------------

    # Total nights stayed
    if "stays_in_weekend_nights" in X.columns and "stays_in_week_nights" in X.columns:
        X["total_nights"] = (
            X["stays_in_weekend_nights"] +
            X["stays_in_week_nights"]
        )
    else:
        X["total_nights"] = np.nan

    # Total guests
    if {"adults", "children", "babies"}.issubset(X.columns):
        X["children"] = X["children"].fillna(0)
        X["total_guests"] = (
            X["adults"] +
            X["children"] +
            X["babies"]
        )
    else:
        X["total_guests"] = np.nan

    # Convert month to numeric if needed
    if "arrival_date_month" in X.columns:
        month_map = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        X["arrival_month"] = X["arrival_date_month"].map(month_map)
    else:
        X["arrival_month"] = np.nan

    # Drop raw month column
    if "arrival_date_month" in X.columns:
        X = X.drop(columns=["arrival_date_month"])

    return X