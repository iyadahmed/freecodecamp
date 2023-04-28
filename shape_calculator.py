class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def set_width(self, width: int):
        self._width = width

    def set_height(self, height: int):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * self._width + 2 * self._height

    def get_diagonal(self):
        return (self._width**2 + self._height**2) ** 0.5

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        return ("*" * self._width + "\n") * self._height

    def get_amount_inside(self, other: "Rectangle"):
        nw = self._width // other._width
        nh = self._height // other._height
        return nw * nh

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def set_width(self, width: int):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height: int):
        super().set_width(height)
        super().set_height(height)

    def set_side(self, side: int):
        self._width = side
        self._height = side

    def __str__(self):
        return f"Square(side={self._width})"
