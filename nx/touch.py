from .controllers import Button
from .players import p1
import _nx


class Touch:
    def __init__(self, x, y, dx, dy, angle):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.angle = angle

    def __repr__(self):
        return "Touch(x={0.x}, y={0.y}, dx={0.dx}, dy={0.dy}, angle={0.angle})".format(self)


class TouchScreen(Button):
    def __init__(self):
        self._button = Button(p1, 26)

    @property
    def is_pressed(self):
        return self._button.is_pressed

    @property
    def touches(self):
        _touches = _nx.hid_get_touches()
        touch_list = []
        for touch in _touches:
            touch_list.append(Touch(*touch))
        return touch_list


screen = TouchScreen()