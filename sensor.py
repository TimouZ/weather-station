#!/usr/bin/env python3
"""
Moc class for development without
physically connected sensors

"""

import random


class Sensor:
    def __init__(self, low_val, high_val):
        self.low_val = low_val
        self.high_val = high_val

    def get_data(self):
        return round(random.uniform(self.low_val, self.high_val), 2)
