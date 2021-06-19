class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, num):
    self.width = num

  def set_height(self, num):
    self.height = num

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = "Too big for picture."
    if self.width < 50 and self.height < 50:
      draw_width = "*" * self.width
      picture = (draw_width + "\n") * self.height

    return picture

  def get_amount_inside(self, rectangle):
    if self.width < rectangle.width or self.height < rectangle.height:
      return 0
    width_multiple = int(self.width / rectangle.width)
    height_mutliple = int(self.height / rectangle.height)

    return width_multiple * height_mutliple

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __repr__(self):
    return f"Square(side={self.width})"

  def set_side(self, num):
    self.width = num
    self.height = num

  def set_width(self, num):
    self.set_side(num)

  def set_height(self, num):
    self.set_side(num)
