# -*- coding: utf-8 -*-
# Time       : 2022/1/17 15:20
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from typing import Optional, Sequence


class AwesomeException(Exception):
    def __init__(self, msg: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
        self.msg = msg
        self.stacktrace = stacktrace

    def __str__(self) -> str:
        exception_msg = "Message: {}\n".format(self.msg)
        if self.stacktrace:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n{}".format(stacktrace)
        return exception_msg


class CookieExpired(AwesomeException):
    """身份令牌或饼干过期时抛出"""
    pass


class AssertTimeout(AwesomeException):
    """断言超时"""
    pass


class UnableToGet(AwesomeException):
    """不可抗力因素，游戏无法获取"""
    pass


class SurpriseExit(AwesomeException):
    """脑洞大开的作者想挑战一下 Python 自带的垃圾回收机制，决定以一种极其垂直的方式结束系统任务。"""
    pass