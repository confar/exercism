def precision_of_two_points(f):
    def two_points(self=None):
        return round(f(self), 2)
    return two_points


class SpaceAge(object):
    seconds_in_day = 86400
    day_in_year = 365.25

    def __init__(self, seconds):
        self.seconds = seconds

    @precision_of_two_points
    def on_earth(self):
        return self.seconds / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_mercury(self):
        return self.seconds / 0.2408467 / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_venus(self):
        return self.seconds / 0.61519726 / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_mars(self):
        return self.seconds / 1.8808158 / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_jupiter(self):
        return self.seconds / 11.862615 / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_saturn(self):
        return self.seconds / 29.447498 / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_uranus(self):
        return self.seconds / 84.016846 / self.seconds_in_day / self.day_in_year

    @precision_of_two_points
    def on_neptune(self):
        return self.seconds / 164.79132 / self.seconds_in_day / self.day_in_year
