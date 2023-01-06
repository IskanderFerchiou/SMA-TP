from pygame.math import Vector2

class Fustrum:

    def __init__(self, parent, r):
        self.radius = r
        self.parent = parent

    def inside(self, obj):
        if hasattr(obj, "position"):
            if isinstance(obj.position, Vector2):
                if obj.position.distance_to(self.parent.position) < self.radius:
                    return True
        return False
