__author__ = 'Rados'

from math import sqrt

print('---------------------------------------------------')
print('--- https://github.com/radoshordos/PyTextGrafic ---')
print('---------------------------------------------------')


class Picture(object):
    DEFAULT_COLOR = "O"
    picture = []
    width = 0
    height = 0

    def create(self, x, y, color=DEFAULT_COLOR):
        self.width = x
        self.height = y

        for y in list(range(y)):
            self.picture.append([color] * x)

    def show(self, separator=""):
        for row in self.picture:
            print(separator.join(row))

    def point(self, x, y, color):
        self.picture[y - 1][x - 1] = str(color)

    def area(self, x1, y1, x2, y2, color):
        """
        Vyplní obdelníkovou plochu zvolenou barvou
        """
        for x in list(range(x1 - 1, x2)):
            for y in list(range(y1 - 1, y2)):
                self.picture[y][x] = color

    def clear(self):
        """
        Nastaví hodnoty, které byly při voláni funkce create x y
        """
        self.area(1, 1, self.width, self.height, self.DEFAULT_COLOR)

    def line(self, x1, y1, x2, y2, color):
        """
        Algoritmus vyhledavá nejkratší cestu mezi 2 zvolenými body.
        Používá k tomu výpočet absolutní hodnoty komplexního čísla.
        Nejkratší cesta je následně přetřena zvolenou barvou.
        """
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

    def fill(self, x, y, new_color):
        """
        Backtracking algoritmus pro prohledánání bodů k obarvení
        Vyhledavaji se body (down, top, left, right)
        """
        old_color = self.__get_color(x, y)
        list_new = [[x, y]]
        list_used = []
        counter = len(list_new)
        while counter > 0:
            point = list_new.pop()
            px = point[0]
            py = point[1]
            if self.__is_exists_new_point(px - 1, py, old_color, list_new, list_used):
                list_new.append([px - 1, py])
            if self.__is_exists_new_point(px + 1, py, old_color, list_new, list_used):
                list_new.append([px + 1, py])
            if self.__is_exists_new_point(px, py - 1, old_color, list_new, list_used):
                list_new.append([px, py - 1])
            if self.__is_exists_new_point(px, py + 1, old_color, list_new, list_used):
                list_new.append([px, py + 1])
            self.picture[py - 1][px - 1] = new_color
            list_used.append(point)
            counter = len(list_new)

    def __is_exists_new_point(self, x, y, old_color, list_new, list_used):
        if 0 < x <= self.width:
            if 0 < y <= self.height:
                if self.__get_color(x, y) == old_color:
                    if [x, y] not in list_new:
                        if [x, y] not in list_used:
                            return True
        return False


    def __get_color(self, x, y):
        return self.picture[y - 1][x - 1]

def valid_command(inp, cmd):
    if inp.lower() == cmd:
        return True
    return False


choice = ""
pic = Picture()

while choice != 'exit':
    choice = str(input("Zadej příkaz:"))
    command = choice.split(" ")

    try:
        if valid_command(command[0].lower(), 'create'):
            pic.create(int(command[1]), int(command[2]))
        elif valid_command(command[0].lower(), 'point'):
            pic.point(int(command[1]), int(command[2]), str(command[3]))
        elif valid_command(command[0].lower(), 'line'):
            pic.line(int(command[1]), int(command[2]), int(command[3]), int(command[4]), str(command[5]))
        elif valid_command(command[0].lower(), 'area'):
            pic.area(int(command[1]), int(command[2]), int(command[3]), int(command[4]), str(command[5]))
        elif valid_command(command[0].lower(), 'fill'):
            pic.fill(int(command[1]), int(command[2]), str(command[3]))
        elif valid_command(command[0].lower(), 'show'):
            pic.show()
        elif valid_command(command[0].lower(), 'clear'):
            pic.clear()
        elif valid_command(command[0].lower(), 'exit'):
            break
        else:
            print("CHYBNY PRIKAZ")
    except IndexError:
        print("CHYBNE PARAMETRY")
    except ValueError:
        print("CHYBNA HODNOTA PARAMETRU")
    except:
        print("CHYBA")
        raise
