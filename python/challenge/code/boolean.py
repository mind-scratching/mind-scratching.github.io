__all__ = [
    'boolean',
    'array',

    'true',
    'false',
]


class boolean:
    __slots__ = ['value']

    ### ----- Initialization Methods ----- ###
    def __init__(self, value=False):
        self.value = value

    ### ----- Output Methods ----- ###
    def __repr__(self):  # repr(x)
        return 'true' if self else 'false'

    __str__ = __repr__  # str(x)

    ### ----- Comparison Methods ----- ###
    def __lt__(self, other):  # x < y
        if isinstance(other, (bool, boolean)):
            if self:
                return false
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __le__(self, other):  # x <= y
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

    def __eq__(self, other):  # x == y
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

    def __ne__(self, other):  # x != y
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

    def __gt__(self, other):  # x > y
        if isinstance(other, (bool, boolean)):
            if other:
                return false
            elif self:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __ge__(self, other):  # x >= y
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
    def __hash__(self):
        return 1 if self.value else 0

    def __bool__(self):
        return True if self.value else False

    ### ----- Calculation Methods ----- ###
    def __and__(self, other):
        if isinstance(other, (bool, boolean)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented
    __rand__ = __and__

    def __xor__(self, other):
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
    __rxor__ = __xor__

    def __or__(self, other):
        if isinstance(other, (bool, boolean)):
            if self:
                return true
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented
    __ror__ = __or__


true = boolean(True)
false = boolean(False)


class array:
    pass
