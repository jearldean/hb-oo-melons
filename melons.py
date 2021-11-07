"""Classes for melon orders."""

import sys
from random import choice


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax, country_code="USA"):
        """Initialize melon order attributes."""
        self.species = species.lower()
        self.qty = qty
        if self.qty > 100:
            raise TooManyMelonsError('We can not sell more than 100 melons.')
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""

        splurge_pricing = choice(range(5, 10))
        base_price = splurge_pricing
        if "christmas" in self.species:
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species=species, qty=qty, order_type="domestic", tax=0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species=species, qty=qty, country_code=country_code, order_type="international", tax=0.17)


class GovernmentMelonOrder(AbstractMelonOrder):
    """A security-inspected melon order."""

    def __init__(self, species, qty, country_code="USA"):
        """Initialize melon order attributes.
        
        The optional country_code will allow our government to ship our fine, inspected
        melons to troops stationed all over the world.
        """
        
        order_type="domestic" if country_code == "USA" else "international"
        super().__init__(species=species, qty=qty, country_code=country_code, order_type=order_type, tax=0)
        self.passed_inspection = False

    def passed_or_failed_inspection(self, passed: bool):
        """Record the fact than an order has been inspected."""

        self.passed_inspection = passed

class TooManyMelonsError(Exception):
    """Because of a rise in money laundering through wholesale melon purchases, 
    UberMelon can not allow orders of more than 100 melons."""

    def __init__(self, message):
        self.message = message


melon_instance = GovernmentMelonOrder(species="wATer", qty=100)
print(melon_instance.species)
print(melon_instance.qty)
print(melon_instance.shipped)
print(melon_instance.tax)
print(melon_instance.country_code)
print(melon_instance.order_type)
print(melon_instance.passed_inspection)
melon_instance.passed_or_failed_inspection(passed=True)
print(melon_instance.passed_inspection)
print(melon_instance.get_total())
print(melon_instance.get_total())
print(melon_instance.get_total())
print(melon_instance.get_total())
