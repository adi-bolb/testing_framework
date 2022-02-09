# Check https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes for reference

from collections.abc import Iterable
from datetime import datetime

BASE_TYPES = [str, int, float, bool, type(None)]


class EntityValueComparator:

    def base_typed(self, obj):
        """Recursive reflection method to convert any object property into a comparable form.
        """
        T = type(obj)
        from_numpy = T.__module__ == 'numpy'

        if T in BASE_TYPES or callable(obj) or (from_numpy and not isinstance(T, Iterable)):
            return obj

        if isinstance(obj, Iterable):
            base_items = [self.base_typed(item) for item in obj]
            return base_items if from_numpy else T(base_items)

        d = obj if T is dict else obj.__dict__ if '__dict__' in dir(obj) else obj.__getstate__()

        return {k: self.base_typed(v) for k, v in d.items()}

    def deep_equals(self, *args):
        return all(self.base_typed(args[0]) == self.base_typed(other) for other in args[1:])
