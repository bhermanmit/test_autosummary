"""Model module.
"""


class Model(object):

    """The model class.
    """

    def __init__(self, a):

        """Model Constructor.
        """

        self._a = a
        self._b = None

    def set_b(self, b):

        """Sets b.
        """

        self._b = b

    def get_a(self):

        """Returns a.
        """

        return self._a

    def get_b(self):

        """Returns b.
        """

        return self._b
