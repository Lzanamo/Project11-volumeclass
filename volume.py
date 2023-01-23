###########################################################
#  Computer Project #11
#
#  Volume Class Build
#    Takes two parameters: the magnitude and the unit of the volume
#    check if the unit is either ml or oz and if the magnitude is a number greater than zero
#    has defined __str__ and __repr__ that display the volume
#    an is_valid() method to check if the volume is valid
#    get_unit or get_magnitude that returns the magnitude or the unit
#    Methods to convert to either oz or ml
#    __eq__ method to check if they are equal
#    add() and sub() method to add or subtract two volumes of a number to a volume
###########################################################

UNITS = ["ml", "oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001


class Volume(object):
    def __init__(self, mag=0, unit="ml"):  # this line is incomplete: parameters needed
        ''' Checks if the unit and magnitude are valid and initializes them'''
        self.__mag = mag
        self.__unit = unit

        if unit not in UNITS:  # checks if the unit is in the UNITS list
            self.__mag = None
            self.__unit = None

        if (type(mag) != int and type(mag) != float) or mag < 0:  # checks if the magnitude is a non-zero number
            self.__mag = 0
            self.__unit = None

    def __str__(self):
        '''Displays the volume is it's valid'''
        result = self.is_valid()  # calls is_valid method before moving on
        if result == True:
            return "{:.3f} {}".format(self.__mag, self.__unit)
        else:
            return "Not a Volume"

    def __repr__(self):
        '''Displays the volume is it's valid'''
        result = self.is_valid()
        if result == True:
            return "{:.6f} {}".format(self.__mag, self.__unit)
        else:
            str = "Not a Volume"
            return str

    def is_valid(self):
        '''Checks the unit and returns True if its valid'''
        if self.__unit == None:  # check if the unit of the volume is None
            return False
        else:
            return True

    def get_units(self):
        '''Returns the unit of the Volume is the volume is valid'''
        if self.is_valid() == True:
            return self.__unit
        else:
            return None

    def get_magnitude(self):
        '''Return the magnitude of the Volumr'''
        return self.__mag

    def metric(self):
        '''Converts volumes from oc to ml'''
        # check if the volume is valid and does the conversion based on the units of the volume
        if self.is_valid() == True and self.__unit == "oz":
            return Volume(self.__mag * MLperOZ, "ml")
        elif self.is_valid() == True and self.__unit == "ml":
            return Volume(self.__mag, self.__unit)
        else:
            return Volume(None, None)

    def customary(self):
        '''Converts volumes from ml to oz'''
        # check if the volume is valid and does the conversion based on the units of the volume
        if self.is_valid() == True and self.__unit == "ml":
            return Volume(self.__mag / MLperOZ, "oz")
        elif self.is_valid() == True and self.__unit == "oz":
            return Volume(self.__mag, self.__unit)
        else:
            return Volume(None, None)

    def __eq__(self, other):
        '''Checks if two volumes are euqal to each other in the same unit'''
        # checks if the volumes are valid
        if self.is_valid() == True and other.is_valid() == True:
            if self.__unit == other.__unit:  # if the units are the same returns true if the absolut value of the volums difference is less than Delta
                if abs(self.__mag - other.__mag) < DELTA:
                    return True
                else:
                    return False
            else:
                # if the units are different changes the second volume to the unit of the first volume and compare the absolut value of the volumes difference to Delta
                if self.__unit == "ml" and other.__unit == "oz":
                    other2 = other.metric()
                    if abs(self.__mag - other2.__mag) < DELTA:
                        return True
                    else:
                        return False
                elif self.__unit == "oz" and other.__unit == "ml":
                    other2 = other.customary()
                    if abs(self.__mag - other2.__mag) < DELTA:
                        return True
                    else:
                        return False
        else:
            return False

    def add(self, other):
        '''Adds two volumes togther or a volume and a number'''
        # checks if the second parameter is of type Volume or not
        if type(other) == Volume:
            if self.is_valid() == True and other.is_valid() == True:  # checks if both volumes are valid
                v1_unit = self.__unit
                v2_unit = other.__unit
                if v1_unit == v2_unit:  # if the units are the same just add and return
                    mag = self.__mag + other.__mag
                    return Volume(mag, self.__unit)
                else:
                    # if the units are different, convert the second volume to the unit of the first volume and add together
                    if v1_unit == "ml" and v2_unit == "oz":
                        other2 = other.metric()
                        return Volume(self.__mag + other2.__mag, self.__unit)
                    elif v1_unit == "oz" and v2_unit == "ml":
                        other2 = other.customary()
                        return Volume(self.__mag + other2.__mag, self.__unit)
            else:
                return Volume(None, None)
        elif type(other) == int or type(other) == float:  # checks if the second parameter is an int or float
            mag = self.__mag + other
            return Volume(mag, self.__unit)

    def sub(self, other):
        '''Subtracts one volume from another or a number from a volume'''
        # checks if the second parameter is of type Volume or not
        if type(other) == Volume:
            if self.is_valid() == True and other.is_valid() == True:  # checks if both volumes are valid
                v1_unit = self.__unit
                v2_unit = other.__unit
                if v1_unit == v2_unit:  # if the units are the same just subtract and return
                    mag = self.__mag - other.__mag
                    return Volume(mag, self.__unit)
                else:
                    # if the units are different, convert the second volume to the unit of the first volume and subtract
                    if v1_unit == "ml" and v2_unit == "oz":
                        other2 = other.metric()
                        return Volume(self.__mag - other2.__mag, self.__unit)
                    elif v1_unit == "oz" and v2_unit == "ml":
                        other2 = other.customary()
                        return Volume(self.__mag - other2.__mag, self.__unit)
            else:
                return Volume(None, None)
        elif type(other) == int or type(other) == float:  # checks if the second parameter is an int or float
            mag = self.__mag - other
            return Volume(mag, self.__unit)