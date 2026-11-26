"""The Upstox v3 full quote's circuit band and VWAP reach OpenAlgo's quote dict."""

from broker.upstox.api.data import BrokerData


def _map(quote):
    return BrokerData._quote_from_full_v3(None, quote)


def test_circuit_band_and_vwap_pass_through():
    q = _map(
        {
            "last_price": 76.5,
            "lower_circuit_limit": 60.64,
            "upper_circuit_limit": 90.96,
            "average_price": 76.42,
            "ohlc": {"open": 75, "high": 77, "low": 74},
            "volume": 10,
        }
    )
    assert q["lower_circuit_limit"] == 60.64
    assert q["upper_circuit_limit"] == 90.96
    assert q["average_price"] == 76.42
    assert q["ltp"] == 76.5


def test_missing_fields_are_zero_not_absent():
    q = _map({"last_price": 10})
    assert (
        q["lower_circuit_limit"] == 0 and q["upper_circuit_limit"] == 0 and q["average_price"] == 0
    )
