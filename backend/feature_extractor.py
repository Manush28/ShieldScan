import re
import numpy as np
import tldextract


def get_main_domain(url):
    ext = tldextract.extract(url)
    return ext.domain


def has_number_letter_mix(domain):
    letters = sum(c.isalpha() for c in domain)
    digits = sum(c.isdigit() for c in domain)
    return 1 if letters > 0 and digits > 0 else 0


def calculate_entropy(url):
    prob = [float(url.count(c)) / len(url) for c in dict.fromkeys(list(url))]
    entropy = -sum([p * np.log2(p) for p in prob])
    return entropy


def extract_features(url):
    features = {}

    features["length"] = len(url)
    features["dots"] = url.count(".")
    features["hyphens"] = url.count("-")
    features["special_chars"] = len(re.findall(r'[^\w]', url))

    features["has_ip"] = int(bool(re.search(r"\d+\.\d+\.\d+\.\d+", url)))
    features["https"] = int(url.startswith("https"))

    features["entropy"] = calculate_entropy(url)

    ext = tldextract.extract(url)
    domain = ext.domain

    features["domain"] = domain
    features["tld"] = ext.suffix

    features["num_letter_mix"] = has_number_letter_mix(domain)

    return features
