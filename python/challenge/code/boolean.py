__all__ = [
    'boolean',
    'array',

    'true',
    'false',
]


class boolean:
    __slots__ = ['value']

    ### ----- Initialization Methods ----- ###
    def __init__(self, value=False, /):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if isinstance(value, bool):
            self.value = value
        elif hasattr(value, '__bool__'):
            self.value = value.__bool__()
        elif hasattr(value, '__len__'):
            self.value = False if len(value) == 0 else true
        else:
            self.value = True

    ### ----- Informal Methods ----- ###
    def __repr__(self, /):
        'Return repr(self).'
        return 'true' if self else 'false'

    def __str__(self, /):
        'Return str(self).'
        return 'true' if self else 'false'

    ### ----- Comparison Methods ----- ###
    def __lt__(self, other, /):
        'Return self<other.'
        if isinstance(other, (bool, boolean)):
            if self:
                return false
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __le__(self, other, /):
        'Return self<=other.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return true
                else:
                    return false
            else:
                return true
        else:
            return NotImplemented

    def __eq__(self, other, /):
        'Return self==other.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return true
                else:
                    return false
            else:
                if other:
                    return false
                else:
                    return true
        else:
            return NotImplemented

    def __ne__(self, other, /):
        'Return self!=other.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return false
                else:
                    return true
            else:
                if other:
                    return true
                else:
                    return false
        else:
            return NotImplemented

    def __gt__(self, other, /):
        'Return self>other.'
        if isinstance(other, (bool, boolean)):
            if other:
                return false
            elif self:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __ge__(self, other, /):
        'Return self>=other.'
        if isinstance(other, (bool, boolean)):
            if other:
                if self:
                    return true
                else:
                    return false
            else:
                return true
        else:
            return NotImplemented

    ### ----- Transformation Methods ----- ###
    def __hash__(self, /):
        'Return hash(self).'
        return 1 if self.value else 0

    def __bool__(self, /):
        'Return bool(self).'
        return True if self.value else False

    ### ----- Calculation Methods ----- ###
    def __and__(self, other, /):
        'Return self&other.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented

    def __rand__(self, other, /):
        'Return other&self.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented

    def __xor__(self, other, /):
        'Return self^other.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return false
                else:
                    return true
            else:
                if other:
                    return true
                else:
                    return false
        else:
            return NotImplemented

    def __rxor__(self, other, /):
        'Return other^self.'
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return false
                else:
                    return true
            else:
                if other:
                    return true
                else:
                    return false
        else:
            return NotImplemented

    def __or__(self, other, /):
        'Return self|other.'
        if isinstance(other, (bool, boolean)):
            if self:
                return true
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __ror__(self, other, /):
        'Return other|self.'
        if isinstance(other, (bool, boolean)):
            if self:
                return true
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented


true = boolean(True)
false = boolean(False)


class array:
    __slots__ = ['value']

    ### ----- Initialization Methods ----- ###
    def __init__(self, iterable=(), /):
        'Initialize self.  See help(type(self)) for accurate signature.'
        self.value = [*iterable]

    ### ----- Informal Methods ----- ###
    def __repr__(self, /):
        'Return repr(self).'
        content = ', '.join(f'{item!r}' for item in self.value)
        return f'[{content}]'

    def __str__(self, /):
        'Return str(self).'
        content = ', '.join(f'{item!r}' for item in self.value)
        return f'[{content}]'

    ### ----- Comparison Methods ----- ###
    def __lt__(self, other, /):
        'Return self<other.'
        if isinstance(other, array):
            return self.value < other.value
        elif isinstance(other, list):
            return self.value < other
        else:
            return NotImplemented

    def __le__(self, other, /):
        'Return self<=other.'
        if isinstance(other, array):
            return self.value <= other.value
        elif isinstance(other, list):
            return self.value <= other
        else:
            return NotImplemented

    def __eq__(self, other, /):
        'Return self==other.'
        if isinstance(other, array):
            return self.value == other.value
        elif isinstance(other, list):
            return self.value == other
        else:
            return NotImplemented

    def __ne__(self, other, /):
        'Return self!=other.'
        if isinstance(other, array):
            return self.value != other.value
        elif isinstance(other, list):
            return self.value != other
        else:
            return NotImplemented

    def __gt__(self, other, /):
        'Return self>other.'
        if isinstance(other, array):
            return self.value > other.value
        elif isinstance(other, list):
            return self.value > other
        else:
            return NotImplemented

    def __ge__(self, other, /):
        'Return self>=other.'
        if isinstance(other, array):
            return self.value > other.value
        elif isinstance(other, list):
            return self.value > other
        else:
            return NotImplemented

    ### ----- Transformation Methods ----- ###
    def __hash__(self, /):
        'Return hash(self).'
        return hash(self.value)

    ### ----- Container Methods ----- ###

    def __len__(self, /):
        'Return len(self).'
        return self.value

    def __getitem__(self, key, /):
        'x.__getitem__(key) <==> x[key]'
        return self.value[key]

    def __setitem__(self, key, value, /):
        'Set self[key] to value.'
        self.value[key] = value

    def __delitem__(self, key, /):
        'Delete self[key].'
        del self.value[key]

    def __iter__(self, /):
        'Implement iter(self).'
        return iter(self.value)

    def __reversed__(self, /):
        'Return a reverse iterator over the list.'
        return reversed(self.value)

    def __contains__(self, key, /):
        'Return key in self.'
        return key in self.value

    ### ----- Calculation Methods ----- ###
    def __add__(self, other, /):
        'Return self+other'
        return self.value + other

    def __iadd__(self, other, /):
        'Implement self+=other.'
        self.value += other

    def __mul__(self, other, /):
        'Return self*other'
        return self.value * other

    def __rmul__(self, other, /):
        'Return other*self'
        return other * self.value

    def __imul__(self, other, /):
        'Implement self*=other.'
        self.value *= other

    ### ----- Array Methods ----- ###
    def append(self, object, /):
        'Append object to the end of the array.'
        self.value.append(object)

    def clear(self, /):
        'Remove all items from array.'
        self.value.clear()

    def copy(self, /):
        'Return a shallow copy of the list.'
        return self.value.copy()

    def count(self, value, /):
        'Return number of occurrences of value.'
        return self.value.count(value)

    def extend(self, iterable, /):
        'Extend list by appending elements from the iterable.'
        self.value.extend(iterable)

    def index(self, value, start=0, stop=9223372036854775807, /):
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        return self.value.index(value, start, stop)

    def insert(self, index, object, /):
        'Insert object before index.'
        self.value.insert(index, object)

    def pop(self, index=-1, /):
        """
        Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        return self.value.pop(index)

    def remove(self, value, /):
        """
        Remove first occurrence of value.

        Raises ValueError if the value is not present.
        """
        self.value.remove(value)

    def reverse(self, /):
        'Reverse *IN PLACE*.'
        self.value.reverse()

    def sort(self, /, *, key=None, reverse=False):
        """
        Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.
        """
        self.sort(key=key, reverse=reverse)
