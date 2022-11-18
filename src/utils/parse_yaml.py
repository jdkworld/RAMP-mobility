from yaml import safe_load
from src.config import ROOT


def parse_yaml(inputfile):
    with open(inputfile) as f:
        d = safe_load(f)
    return d