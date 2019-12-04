# import time
#
#
# class TimeTest(object):
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod
#     def showTime():
#         return time.strftime("%H:%M:%S", time.localtime())
#
#
# print(TimeTest.showTime())
# t = TimeTest(2, 10, 10)
# nowTime = t.showTime()
# print(nowTime)

class ColorTest(object):
    color = "color"

    @classmethod
    def value(self):
        return self.color


class Red(ColorTest):
    color = "red"


class Green(ColorTest):
    color = "green"


g = Green()
print(g.value())
print(Green.value())