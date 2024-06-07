from enum import IntEnum

class Point:
    """Represents a point in R^2 with its category."""

    class Category(IntEnum):
        """Represents the category of a point."""
        POSITIVE = 1
        NEGATIVE = -1
        UNCLASSIFIED = 0


    def __init__(self, x_0:float, x_1:float, category:Category):
        
        assert category in Point.Category, "Invalid category"
        assert x_0 is not None, "x_0 is None"
        assert x_1 is not None, "x_1 is None"

        self.x = (x_0, x_1)
        self.category = category

    def __str__(self):
        return f"Point({self.x[0]}, {self.x[1]}, {self.category.name})"