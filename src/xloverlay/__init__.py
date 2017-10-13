# xloverlay/__init__.py

""" Overlay library for python XLattice packages. """

__version__ = '0.0.6'
__version_date__ = '2017-10-13'

__all__ = ['__version__', '__version_date__', 'XLOverlayError', ]


class XLOverlayError(RuntimeError):
    """ General purpose exception for the package. """
