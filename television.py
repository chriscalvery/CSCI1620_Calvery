class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL) -> None:
        """
        Init class and variables
        :param status:
        :param muted:
        :param volume:
        :param channel:
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        self.__prev_volume = None

    def power(self) -> None:
        """
        Method to turn TV on or off
        """
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self) -> None:
        """
        Method to mute or unmute TV
        """
        if not self.__muted and self.__status:
            self.__muted = True
            self.__prev_volume = self.__volume
            self.__volume = 0

    def volume_up(self) -> None:
        """
        Method to turn volume up
        """
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume + 1
        elif self.__status and Television.MAX_VOLUME > self.__volume >= Television.MIN_VOLUME:
          self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to turn volume down
        """
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume - 1
        elif self.__status and Television.MIN_VOLUME < self.__volume <= Television.MAX_VOLUME:
            self.__volume -= 1

    def channel_up(self) -> None:
        """
        Method to move channel up
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to move channel down
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def __str__(self) -> str:
        """
        Method to return status, channel, and volume of TV
        :return:
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
