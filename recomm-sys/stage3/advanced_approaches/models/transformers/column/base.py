"""
Base class for all column-orientation transformers classes
with fit/transform functions.
"""
from abc import ABC, abstractmethod
from enum import Enum


class Column(ABC):
    """Base class for all column-orientation transformers classes
    with fit/transform functions.
    """

    @abstractmethod
    def fit(self, x, y=None):
        """Fit this transformers.

        Parameters
        ----------
        x : array-like
            One column of training data.
        y : array-like, default=None
            Training targets.
        """

        raise NotImplementedError

    @abstractmethod
    def transform(self, x):
        """Transform x by this fitted transformers.

        Parameters
        ----------
        x : array-like
            Column data to be transformed.
        """

        raise NotImplementedError


class ColumnType(Enum):
    NUMBER = 1
    CATEGORY = 2
    SEQUENCE = 3


class NumberColumn(Column):
    """Base class for all column-orientation number type transformers classes
    with fit/transform functions.
    """
    column_type = ColumnType.NUMBER


class CategoryColumn(Column):
    """Base class for all column-orientation category type transformers classes
    with fit/transform functions.
    """
    column_type = ColumnType.CATEGORY

    @abstractmethod
    def dimension(self):
        """Number of unique terms.
        """
        raise NotImplementedError


class SequenceColumn(Column):
    """Base class for all column-orientation sequence type transformers classes
    with fit/transform functions.
    """
    column_type = ColumnType.SEQUENCE

    @abstractmethod
    def dimension(self):
        """Number of unique terms.
        """
        raise NotImplementedError

    @abstractmethod
    def max_length(self):
        """Maximum length of one sequence.
        """
        raise NotImplementedError
