class PointsForPlace:
    def get_points_for_place(self, place):
        points = 0
        validation = PointsForPlace.validation_place(place)
        if validation is not True:
            print(validation)
        else:
            points += 101 - place
        return points

    @staticmethod
    def validation_place(place):
        if place > 100:
            return f'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return f'Спортсмен не может занять нулевое или отрицательное место'
        else:
            return True

class PointsForMeters:
    def get_points_for_meters(self, meters):
        points = 0
        validation = PointsForMeters.validation_meters(meters)
        if validation is not True:
            print(validation)
        else:
            points = meters * 0.5
        return points
    
    @staticmethod
    def validation_meters(meters):
        if meters < 0:
            return f'Количество метров не может быть отрицательным'
        return True

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, place, meters):
        total = super().get_points_for_place(place) + super().get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(11))
points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(7))
total_points = TotalPoints()
print(total_points.get_points_for_place(100))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))