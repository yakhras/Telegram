import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define keyword mappings
KEYWORDS = {
    "SL": ["sl", "stop loss", "s/l"],
    "TP": ["tp", "take profit", "target"],
    "ENTRY": ["sell now", "sell"]
}

def clean_keyword(token_text):
    """Normalize token text for comparison."""
    return token_text.lower().strip()

def find_keyword(text, keywords):
    """Check if any keyword exists in the text."""
    for keyword in keywords:
        if keyword in text:
            return True
    return False

# def extract_trade_details(text):
#     """Extract trade details using a hybrid NLP + regex approach."""
#     doc = nlp(text)
#     details = {"Entry": None, "Entry Range": None, "SL": None, "TPs": []}

#     for sent in doc.sents:  # Process sentence by sentence
#         tokens = [clean_keyword(t.text) for t in sent]

#         # Check for Entry
#         if find_keyword(" ".join(tokens), KEYWORDS["ENTRY"]):
#             entry_match = re.search(r"(\d+[.\-]?\d*)", sent.text)
#             if entry_match:
#                 # Check for entry range (e.g., 2669.2667 or 2669-2667)
#                 range_match = re.findall(r"\d+[.\-]?\d*", sent.text)
#                 if len(range_match) > 1:
#                     # Replace dots with dashes for consistency
#                     range_values = [
#                         float(value.replace(".", "")) if "." in value else float(value)
#                         for value in range_match
#                     ]
#                     details["Entry Range"] = range_values
#                 else:
#                     details["Entry"] = float(entry_match.group().replace(".", ""))

#         # Check for SL
#         elif find_keyword(" ".join(tokens), KEYWORDS["SL"]):
#             sl_match = re.search(r"\d+", sent.text)
#             if sl_match:
#                 details["SL"] = int(sl_match.group())

#         # Check for TPs
#         elif find_keyword(" ".join(tokens), KEYWORDS["TP"]):
#             tp_match = re.findall(r"\d+(?:-\d+)*", sent.text)
#             for match in tp_match:
#                 if '-' in match:  # Split hyphenated TPs
#                     details["TPs"].extend(map(int, match.split('-')))
#                 else:
#                     details["TPs"].append(int(match))

#     return details

def extract_trade_details(text):
    """Extract trade details using a hybrid NLP + regex approach."""
    doc = nlp(text)
    details = {"Entry": None, "Entry Range": None, "SL": None, "TPs": []}

    for sent in doc.sents:  # Process sentence by sentence
        tokens = [clean_keyword(t.text) for t in sent]

        # Extract Entry or Entry Range
        extract_entry_details(sent, tokens, details)

        # Extract SL (Stop Loss)
        extract_sl_details(sent, tokens, details)

        # Extract TPs (Take Profits)
        extract_tp_details(sent, tokens, details)

    return details


def extract_entry_details(sent, tokens, details):
    """Extract Entry and Entry Range from a sentence."""
    if find_keyword(" ".join(tokens), KEYWORDS["ENTRY"]):
        entry_match = re.search(r"(\d+[.\-]?\d*)", sent.text)
        if entry_match:
            # Check for entry range (e.g., 2669.2667 or 2669-2667)
            range_match = re.findall(r"\d+[.\-]?\d*", sent.text)
            if len(range_match) > 1:
                # Replace dots with dashes for consistency
                range_values = [
                    float(value.replace(".", "")) if "." in value else float(value)
                    for value in range_match
                ]
                details["Entry Range"] = range_values
            else:
                details["Entry"] = float(entry_match.group().replace(".", ""))


def extract_sl_details(sent, tokens, details):
    """Extract Stop Loss (SL) from a sentence."""
    if find_keyword(" ".join(tokens), KEYWORDS["SL"]):
        sl_match = re.search(r"\d+", sent.text)
        if sl_match:
            details["SL"] = int(sl_match.group())


def extract_tp_details(sent, tokens, details):
    """Extract Take Profits (TPs) from a sentence."""
    if find_keyword(" ".join(tokens), KEYWORDS["TP"]):
        tp_match = re.findall(r"\d+(?:-\d+)*", sent.text)
        for match in tp_match:
            if '-' in match:  # Split hyphenated TPs
                details["TPs"].extend(map(int, match.split('-')))
            else:
                details["TPs"].append(int(match))


# Example message
message = """
XAUUSD SELL  2669.2667
Sl : 2674
Tp 2664
Tp 2656
Tp 2650
Tp 2640
"""

# Parse the message
trade_details = extract_trade_details(message)
print(trade_details)