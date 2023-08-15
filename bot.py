class Bot:
    def __init__(self, lat, long):
        """
        initialize a Bot instance with the home coordinates set to (lat, long)
        """
        self.home_lat = lat
        self.home_long = long
        self.home_set = True
        
    def __init__(self):
        """
        initialize a Bot instance without home coordinates
        """
        self.home_set = False
        self.home_lat = 0
        self.home_long = 0

    def set_home(self, lat, long):
        """
        set the home coordinates for this bot instance
        """
        self.home_lat = lat
        self.home_long = long
        self.home_set = True

    def clear_home(self):
        """
        reset the Bot instance to have no home coordinates
        """
        self.home_set = False

    def get_lat(self):
        """
        Getter method for the home latitude field
        """
        return self.home_lat
    
    def get_long(self):
        """
        Getter method for the home longitude field
        """
        return self.home_long