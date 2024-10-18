class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        # Initialize the numerator and denominator properties
        # Check that the denominator is non-zero

    def add(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, 
                            den)
        # Add the current fraction and the other fraction
        # Return the result as a new Fraction object

    def subtract(self, other):
         num = self.numerator * other.denominator - other.denominator * self.denominator
         den = self.denominator * other.denominator
         return Fraction(num, 
                         den)
        # Subtract the other fraction from the current fraction
        # Return the result as a new Fraction object
    def multiply(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)
        # Multiply the current fraction and the other fraction
        # Return the result as a new Fraction object

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)
        # Divide the current fraction by the other fraction
        # Check that the other fraction has a non-zero numerator
        # Return the result as a new Fraction object

    def simplify(self):
        gcd = self.gcd(abs(self.numerator), abs(self.denominator))
        num = self.numerator // gcd
        den = self.denominator // gcd
        return Fraction(num, den)
        # Simplify the current fraction to its simplest form
        # Return a new Fraction object with the simplified numerator and denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    @staticmethod
    def gcd(a,b):
        if b == 0:
            return a
        else: 
            return Fraction.gcd(b, a%b)
        # Return the string representation of the fraction in the format "numerator/denominator"


# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"
