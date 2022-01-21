from enum import Enum, IntEnum


class MessageServiceTypeEnum(str, Enum):
    RCS: str = "rcs"
    LEGACY: str = "rcs, legacy"  # rcs 부달시, xMS로fallback전송


class ServiceTypeEnum(str, Enum):
    SMS: str = "RCSSMS"
    LMS: str = "RCSLMS"
    MMS: str = "RCSMMS"
    TMPL: str = "RCSTMPL"
    CHAT: str = "RCSCHAT"


class LegacyServiceTypeEnum(str, Enum):
    SMS: str = "SMS"
    LMS: str = "LMS"


class ScheduleTypeEnum(IntEnum):
    IMMEDIATE: int = 0


class ExpiryOptionEnum(IntEnum):
    AFTER_THREE_DAYS: int = 1
    AFTER_SETTING_TIMES: int = 2


class HeaderEnum(str, Enum):
    """
    헤더 광고에 대한 정의
    0: 광고 넣지않음
    1: 광고 넣음
    """

    NOT_ADVERTISE: str = "0"
    ADVERTISE: str = "1"


class ActionEnum(str, Enum):
    URL_ACTION: str = "urlAction"  # 단말기에 기본 웹 브라우저로 설정된 앱을 통해서, 웹페이지로 이동할 수있습니다
    LOCAL_BROWSER_ACTION: str = "localBrowserAction"  # 단말기의 메시지 앱 내부 브라우저를 통해 웹페이지로 이동할 수 있습니다
    MAP_ACTION: str = "mapAction"  # 미리 지정된 위치를 보여주거나 사용자의 현재 위치를 서버로 전송 할 수 있습니다.
    CALENDAR_ACTION: str = "calendarAction"  # 사용자의 캘린더에 특정 일정을 등록 할 수 있습니다.
    CLIPBOARD_ACTION: str = "clipboardAction"  # 특정 문구를 사용자 단말이 자동으로 복사 할 수 있게 합니다
    COMPOSE_ACTION: str = "composeAction"  # 다른 번호로 메시지를 보낼 수 있도록 대화방을 엽니다.
    DIALER_ACTION: str = "dialerAction"  # 특정 전화번호로 전화를 걸 수 있습니다.


class MessageStatusEnum(str, Enum):
    SUCCESS: str = "success"
    FAIL: str = "fail"


class MnoInfoEnum(str, Enum):
    KT: str = "KT"
    SKT: str = "SKT"
    LGU: str = "LGU"


class BillEnum(IntEnum):
    FREE: int = 0
    CHARGE: int = 1


class EventTypeEnum(str, Enum):
    MESSAGE: str = "message"
    RESPONSE: str = "response"
    NEW_USER: str = "newuser"
