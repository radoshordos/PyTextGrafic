__author__ = 'Rados'

from math import sqrt

# http://docs.python-guide.org/en/latest/writing/style/

class Picture(object):
    DEFAULT_COLOR = "O"
    picture = []
    width = 0
    height = 0


    def create(self, width, height, color=DEFAULT_COLOR):
        self.width = width
        self.height = height

        for x in list(range(width)):
            self.picture.append([color] * height)

    def show(self, separator=" "):
        for row in self.picture:
            print(separator.join(row))

    def point(self, width, height, color):
        self.picture[width][height] = str(color)

    def area(self, x1, y1, x2, y2, color):
        for x in list(range(x1, x2)):
            for y in list(range(y1, y2)):
                self.picture[x][y] = color

    def clear(self):
        self.area(0, 0, self.width, self.height, self.DEFAULT_COLOR)

    def line(self, x1, y1, x2, y2, color):
        if x1 > x2:  # swap x
            x1, x2 = x2, x1
        if y1 > y2:  # swap y
            y1, y2 = y2, y1
        for x in list(range(x1, x2 + 1)):
            line = []
            for y in list(range(y1, y2 + 1)):
                line.append(Picture.__distance(x, y, x1, y1) + Picture.__distance(x, y, x2, y2))
            minimum = min(line)
            for point in list(range(0, len(line))):
                if line[point] == minimum:
                    self.point(x, y1 + point, color)

    @staticmethod
    def __distance(my_x, my_y, orig_x, orig_y):
        return Picture.__abs_number(abs(orig_x - my_x), abs(orig_y - my_y))

    @staticmethod
    def __abs_number(x, y):
        return sqrt(x ** 2 + y ** 2)

    # Backtracking algorithm
    def fill(self, width, height, new_color):
        old_color = self.__get_color(width, height)
        if self.__is_exists_point(width, height, old_color):
            list_new = [[width, height]]
            list_used = []

            count = len(list_new);
            for i in list(range(0, 1000)):
                if len(list_new) > 0:
                    point = list_new.pop()
                    for i in self.__add_useful_neighborhood(point, old_color):



                        if point not in list_used and point not in list_new:
                            list_new.append(i)
                    self.__set_new_color(point[0], point[1], new_color)
                    list_used.append(point)
                count = len(list_new);

    def __get_color(self, width, height):
        return self.picture[width][height]

    def __is_exists_point(self, width, height, old_color):
        if 0 <= width < self.width:
            if 0 <= height < self.height:
                if self.__get_color(width, height) == old_color:
                    return True
        return False

    def __set_new_color(self, width, height, new_color):
        self.picture[width][height] = new_color



    def __add_useful_neighborhood(self, list, old_color):
        new_points = []
        if self.__is_exists_point(list[0] - 1, list[1], old_color):
            new_points.append([list[0] - 1, list[1]])
        if self.__is_exists_point(list[0] + 1, list[1], old_color):
            new_points.append([list[0] + 1, list[1]])
        if self.__is_exists_point(list[0], list[1] - 1, old_color):
            new_points.append([list[0], list[1] - 1])
        if self.__is_exists_point(list[0], list[1] + 1, old_color):
            new_points.append([list[0], list[1] + 1])
        return new_points


#
#pic = Picture()
#pic.create(20, 20, "P")
#pic.line(2, 5, 16, 8, "X")
#pic.area(2, 5, 6, 8, "g")
#pic.fill(2, 2, "w")
#pic.fill(2, 2, "0")
#pic.show()