import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Waveshare3in7(DisplayImpl):
    def __init__(self, config):
        super(Waveshare3in7, self).__init__(config, 'waveshare3in7')

    def layout(self):
        fonts.setup(10, 8, 10, 18, 25, 9)
        self._layout['width'] = 280
        self._layout['height'] = 480
        self._layout['face'] = (0, 43)
        self._layout['name'] = (0, 14)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (0, 71)
        self._layout['uptime'] = (0, 25)
        self._layout['line1'] = [0, 12, 280, 12]
        self._layout['line2'] = [0, 116, 280, 116]
        self._layout['friend_face'] = (12, 88)
        self._layout['friend_name'] = (1, 103)
        self._layout['shakes'] = (26, 117)
        self._layout['mode'] = (0, 117)
        self._layout['status'] = {
            'pos': (65, 26),
            'font': fonts.status_font(fonts.Small),
            'max': 12
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare 3.7 inch lcd display")
        from pwnagotchi.ui.hw.libs.waveshare.v3in7.epd3in7 import EPD
        self._display = EPD()
        self._display.init(0)
        self._display.Clear(0)

    def render(self, canvas):
        self._display.display_4Gray(canvas)

    def clear(self):
        self._display.Clear(0)
