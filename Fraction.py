# Define your Fraction class here
class Fraction():

  def __init__(self, numerator, denominator):
    self.numerator = numerator
    if denominator != 0:
      self.denominator = denominator
    else:
      raise ValueError()

  def get_numerator(self):
    return self.numerator
  def get_denominator(self):
    return self.denominator

  def set_numerator(self, new_numerator):
    self.numerator = new_numerator

  def set_denominator(self, new_denominator):
    if new_denominator != 0:
      self.denominator = new_denominator
    else:
      raise ValueError()

  def __str__(self):
    return str(self.numerator) + '/' + str(self.denominator)

  def add(self, otherFraction):
    value = self.numerator/self.denominator + otherFraction.numerator/otherFraction.denominator
    reduced = False
    i = 1
    while reduced == False:
      checking = value*i
      if str(checking)[-2:] == '.0' or type(checking) == int:
        reduced = True
        self.set_numerator(int(value*i))
        self.set_denominator(i)
      else:
        i += 1

  def subtract(self, otherFraction):
    value = self.numerator/self.denominator - otherFraction.numerator/otherFraction.denominator
    reduced = False
    i = 1
    while reduced == False:
      checking = value*i
      if str(checking)[-2:] == '.0' or type(checking) == int:
        reduced = True
        self.set_numerator(int(value*i))
        self.set_denominator(i)
      else:
        i += 1

  def multiply(self, otherFraction):
    value = self.numerator/self.denominator * otherFraction.numerator/otherFraction.denominator
    reduced = False
    i = 1
    while reduced == False:
      checking = value*i
      if str(checking)[-2:] == '.0' or type(checking) == int:
        reduced = True
        self.set_numerator(int(value*i))
        self.set_denominator(i)
      else:
        i += 1

  def __reduce(self):
    value = self.numerator/self.denominator
    reduced = False
    i = 1
    while reduced == False:
      checking = value*i
      if str(checking)[-2:] == '.0' or type(checking) == int:
        reduced = True
        self.set_numerator(int(value*i))
        self.set_denominator(i)
      else:
        i += 1



if __name__ == '__main__':

  pass
