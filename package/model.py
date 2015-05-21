"""Model module.
"""


class Model(object):

    """The model class.

    Attributes
    ----------
    a : str
        A string.
    b : int
        An integer.

    Parameters
    ----------
    a : str
        A string.
    """

    def __init__(self, a):

        """Model Constructor.
        """

        self._a = a
        self._b = None

    def set_b(self, b):

        """Sets b.

        Parameters
        ----------
        b : int
        """

        self._b = b

    def get_a(self):

        """Returns a.

        Returns
        -------
        str
        """

        return self._a

    def get_b(self):

        """Returns b.

        Returns
        -------
        int
        """

        return self._b
