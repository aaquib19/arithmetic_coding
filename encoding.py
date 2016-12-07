import decimal
from decimal import Decimal


decimal.getcontext().prec = 100


def encode(string, probabilities):
    """Encodes provided string using arithmetic coding."""
    assert len(string) < 29, "String length must be less than 29 but is {}.".format(len(string))
    string = string + "#"
    lower_bound = Decimal(0)
    upper_bound = Decimal(1)

    for s in string:
        cur_range = Decimal(upper_bound - lower_bound)
        upper_bound = lower_bound + cur_range * probabilities.get(s)[1]
        lower_bound = lower_bound + cur_range * probabilities.get(s)[0]

    return lower_bound


def decode(encoded, probabilities):
    decoded = ""
    new_encoded = encoded
    symbol = get_char_in_range(new_encoded, probabilities)

    while symbol != "#" and len(decoded) < 30:
        decoded += symbol
        cur_range = Decimal(probabilities.get(symbol)[1] - probabilities.get(symbol)[0])
        new_encoded = (new_encoded - probabilities.get(symbol)[0]) / cur_range
        symbol = get_char_in_range(new_encoded, probabilities)

    return decoded[:-1]


def get_char_in_range(encoded, probabilities):
    for k, v in probabilities.items():
        if encoded >= probabilities.get(k)[0] and encoded < probabilities.get(k)[1]:
            return k

if __name__ == "__main__":
    probabilities = {
        "a": (Decimal(0.00), Decimal(0.10)),
        "b": (Decimal(0.10), Decimal(0.15)),
        "c": (Decimal(0.15), Decimal(0.19)),
        "d": (Decimal(0.19), Decimal(0.25)),
        "e": (Decimal(0.25), Decimal(0.30)),
        "f": (Decimal(0.30), Decimal(0.35)),
        "g": (Decimal(0.35), Decimal(0.38)),
        "h": (Decimal(0.38), Decimal(0.40)),
        "i": (Decimal(0.40), Decimal(0.43)),
        "j": (Decimal(0.43), Decimal(0.48)),
        "k": (Decimal(0.48), Decimal(0.55)),
        "l": (Decimal(0.55), Decimal(0.56)),
        "m": (Decimal(0.56), Decimal(0.59)),
        "n": (Decimal(0.59), Decimal(0.67)),
        "o": (Decimal(0.67), Decimal(0.70)),
        "p": (Decimal(0.70), Decimal(0.77)),
        "q": (Decimal(0.77), Decimal(0.80)),
        "r": (Decimal(0.80), Decimal(0.83)),
        "s": (Decimal(0.83), Decimal(0.88)),
        "t": (Decimal(0.88), Decimal(0.91)),
        "u": (Decimal(0.91), Decimal(0.92)),
        "v": (Decimal(0.92), Decimal(0.94)),
        "w": (Decimal(0.93), Decimal(0.95)),
        "x": (Decimal(0.95), Decimal(0.97)),
        "y": (Decimal(0.95), Decimal(0.98)),
        "z": (Decimal(0.98), Decimal(0.99)),
        "#": (Decimal(0.99), Decimal(1.0))
    }

    probabilities2 = {
        "a": (0.00, 0.30),
        "b": (0.30, 0.45),
        "c": (0.45, 0.70),
        "d": (0.70, 0.80),
        "e": (0.80, 1.00)
    }

    string = "jamalmoirjamalmoirjamalmoir"
    encoded = encode(string, probabilities)
    decoded = decode(encoded, probabilities)

    print("Original: {} | Encoded: {} | Decoded: {}".format(string, encoded, decoded))
