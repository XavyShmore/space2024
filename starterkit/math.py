import math


class Math:
    @staticmethod
    def angle_between_vectors(vector1, vector2) -> float:
        dot_product = vector1.x * vector2.x + vector1.y * vector2.y
        magnitude_product = math.sqrt(vector1.x ** 2 + vector1.y ** 2) * math.sqrt(vector2.x ** 2 + vector2.y ** 2)

        cosine_similarity = dot_product / magnitude_product
        angle_radians = math.acos(cosine_similarity)

        angle_degrees = math.degrees(angle_radians)

        return angle_degrees
