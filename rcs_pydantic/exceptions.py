from . import errors


class MessageException(Exception):
    def __init__(self, message: int):
        if errors.ErrorCodeEnum.has_value(message):
            self.message = errors.ErrorCodeEnum(message).name.lower()
        elif errors.MaaPErrorCodeEnum.has_value(message):
            self.message = errors.MaaPErrorCodeEnum(message).name.lower()
        elif errors.RcsBizCenterErrorCodeEnum.has_value(message):
            self.message = errors.RcsBizCenterErrorCodeEnum(message).name.lower()
        elif errors.KTErrorCodeEnum.has_value(message):
            self.message = errors.KTErrorCodeEnum(message).name.lower()
        else:
            self.message = "unknown"
