class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        self.__prev_volume = None

    def power(self):
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self):
        if not self.__muted and self.__status:
            self.__muted = True
            self.__prev_volume = self.__volume
            self.__volume = 0

    def volume_up(self):
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume + 1
        elif self.__status and Television.MAX_VOLUME > self.__volume >= Television.MIN_VOLUME:
          self.__volume += 1

    def volume_down(self):
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume - 1
        elif self.__status and Television.MIN_VOLUME < self.__volume <= Television.MAX_VOLUME:
            self.__volume -= 1

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
