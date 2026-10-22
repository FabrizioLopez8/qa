import unittest

def main():
  for i in range (0, 100):
    print(fizzOrBuzz(i))    

def fizzOrBuzz(num):
  if not isDivisibleByThreeAndFive(num):
      return num
  else:
    return (checkDivisionByThree(num) + checkDivisionByFive(num))

def checkDivisionByThree(num):
  if num % 3 == 0:
    return "Fizz"
  else: return ""

def checkDivisionByFive(num):
  if num % 5 == 0:
    return "Buzz"
  else: return ""

def isDivisibleByThreeAndFive(num):
  if num % 3 == 0 or num % 5 == 0:
    return True
  else: return False

class FizzBuzzTest(unittest.TestCase):

  def test_fizzNumber(self):
    self.assertEqual("Fizz", fizzOrBuzz(27))

  def test_buzzNumber(self):
    self.assertEqual("Buzz", fizzOrBuzz(25))

  def test_fizzBuzzNumber(self):
    self.assertEqual("FizzBuzz", fizzOrBuzz(30))

  def test_number(self):
    self.assertEqual(29, fizzOrBuzz(29))


main()
unittest.main(defaultTest='FizzBuzzTest', argv=[''], verbosity=2, exit=False)