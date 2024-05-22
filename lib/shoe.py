#!/usr/bin/env python3

class Shoe:
  def __init__(self, brand, size):
    self.brand = brand
    # You can add size validation here if needed
    self.size = size
    self.condition = "New"  # Add a condition attribute

  def cobble(self):
    # Implement logic to repair the shoe (change condition or other attributes)
    self.condition = "Repaired"
    print("Shoe has been repaired!")