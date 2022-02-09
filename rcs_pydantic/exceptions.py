from . import errors


class MessageException(Exception):
    def __init__(self, message: int):
        if errors.ErrorCodeEnum.has_value(message):
            self.message = errors.ErrorCodeEnum(message).value[1]
        elif errors.MaaPErrorCodeEnum.has_value(message):
            self.message = errors.MaaPErrorCodeEnum(message).value[1]
        elif errors.RcsBizCenterErrorCodeEnum.has_value(message):
            self.message = errors.RcsBizCenterErrorCodeEnum(message).value[1]
        elif errors.KTErrorCodeEnum.has_value(message):
            self.message = errors.KTErrorCodeEnum(message).value[1]
        else:
            self.message = "unknown"

    def __str__(self):
        return self.message
