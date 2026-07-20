"""
Misc may contain stuff that seems useless but may be useful for people who do not know how to do this
in their own program
"""



def pcombo(pstate, ndigits):
    return pstate ** ndigits

def mil_hr(hr: int, pm = bool, minu: None | int = None,):
    """
    :param minu: the 12 hour clock minute. just slightly changes the output
    :param hr: the 12 hour clock hour
    :param pm: if its pm or am. true if PM false if AM
    :return: a int 0 - 23 on what the military hour is
    """
    minute = "00"
    if minu is not None:
        minute = str(minu)

    if pm:
        a = hr + 12
        if a == 24:
            a = 0
        return int(f"{a}{minute}"), (a, minute)
    else:
        return int(f"{hr}{minute}"), (hr, minute)

def twlv_hr(mil: int, minu: int | None = None):
    """
    :param minu: Optional Minute. will output as 0 if none is provided
    :param mil: Military time hour
    :return: int, int, bool. (hour, minute, PM?) 12 hour clocktime and weather or not it is pm.
    """
    minute = 0
    if minu is not None:
        minute = minu
    if mil > 12:
        return mil - 12,minute, True
    else:
        return mil,minute, False