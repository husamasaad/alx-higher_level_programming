#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of a side of the square
            position (int, int): the position
        Returns: None
        """

        self.size = size
        self.position = position

    def area(self):
        """
        find the Area of the square
        Returns:
            the area of the square
        """

        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    
    @property
    def position(self):
        """getter of __postion
        Returns:
            The position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(num, int) for num in value or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            self.__position = value

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

