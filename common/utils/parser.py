import re


def mobile(mobile_str):
    '''检验手机号'''
    if re.match(r'1[3-9]\d{9}$',mobile_str):
        return mobile_str
    else:
        raise ValueError('{} is not a valid mobile'.format(mobile_str))


