"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax, country_code="USA"):
        """Initialize melon order attributes."""
        self.species = species.lower()
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
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

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species=species, qty=qty, country_code=country_code, order_type="international", tax=0)
        self.passed_inspection = False

    def passed_inspection(passed):
        """Record the fact than an order has been inspected."""

        self.passed_inspection = passed