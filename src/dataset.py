from .point import Point
from typing import List, Tuple

class Dataset:
    """Represents a dataset of Points with its categories."""

    def __init__(self, points:List[Point]):
        assert points is not None, "points is None"
        assert len(points) > 0, "points is empty"
        self.points = points
    
    def get_point_at(self, coordinates:Tuple[float, float]) -> Point:
        """Returns the point at the given coordinates."""
        assert coordinates is not None
        x_0, x_1 = coordinates
        assert x_0 is not None, "x_0 is None"
        assert x_1 is not None, "x_1 is None"
        for point in self.points:
            if point.x[0] == x_0 and point.x[1] == x_1:
                return point
        return None
    
    @classmethod
    def from_raw(cls, positive_points:List[Tuple[float, float]], negative_points:List[Tuple[float, float]], unclassified_points:List[Tuple[float, float]]=[]) -> 'Dataset':
        """Creates a Dataset from raw data."""
        assert positive_points is not None, "positive_points is None"
        assert negative_points is not None, "negative_points is None"
        
        positives = [Point(x_0, x_1, Point.Category.POSITIVE) for x_0, x_1 in positive_points]
        negatives = [Point(x_0, x_1, Point.Category.NEGATIVE) for x_0, x_1 in negative_points]
        unclassified = [Point(x_0, x_1, Point.Category.UNCLASSIFIED) for x_0, x_1 in unclassified_points]
        
        return cls(positives + negatives + unclassified)