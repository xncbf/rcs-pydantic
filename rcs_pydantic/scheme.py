from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field, validator

from . import enums
from .errors import LegacyErrorCodeEnum


class EmptyDict:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, dict):
            raise TypeError("dict required")
        if len(v.keys()) > 0:
            raise ValueError("dict must be empty")
        return {}


class RcsSMSBody(BaseModel):
    title: Optional[str] = Field(max_length=30)
    description: str = Field(max_length=100)
    media: Optional[str]


class RcsLMSBody(BaseModel):
    title: Optional[str] = Field(max_length=30)
    description: str = Field(max_length=1300)
    media: Optional[str]


class RcsMMSBody(BaseModel):
    title: Optional[str] = Field(max_length=30)
    description: str = Field(max_length=1300)
    media: Optional[str]


class RcsCHATBody(BaseModel):
    title: Optional[str] = Field(max_length=30)
    description: str = Field(max_length=1300)
    media: Optional[str]


class RcsSMSCarouselBody(BaseModel):
    title1: Optional[str] = Field(max_length=30)
    description1: str = Field(max_length=100)
    media1: Optional[str]
    title2: Optional[str] = Field(max_length=30)
    description2: Optional[str] = Field(max_length=100)
    media2: Optional[str]
    title3: Optional[str] = Field(max_length=30)
    description3: Optional[str] = Field(max_length=100)
    media3: Optional[str]
    title4: Optional[str] = Field(max_length=30)
    description4: Optional[str] = Field(max_length=100)
    media4: Optional[str]
    title5: Optional[str] = Field(max_length=30)
    description5: Optional[str] = Field(max_length=100)
    media5: Optional[str]
    title6: Optional[str] = Field(max_length=30)
    description6: Optional[str] = Field(max_length=100)
    media6: Optional[str]


class RcsLMSCarouselBody(BaseModel):
    title1: Optional[str] = Field(max_length=30)
    description1: str = Field(max_length=100)
    media1: Optional[str]
    title2: Optional[str] = Field(max_length=30)
    description2: Optional[str] = Field(max_length=100)
    media2: Optional[str]
    title3: Optional[str] = Field(max_length=30)
    description3: Optional[str] = Field(max_length=100)
    media3: Optional[str]
    title4: Optional[str] = Field(max_length=30)
    description4: Optional[str] = Field(max_length=100)
    media4: Optional[str]
    title5: Optional[str] = Field(max_length=30)
    description5: Optional[str] = Field(max_length=100)
    media5: Optional[str]
    title6: Optional[str] = Field(max_length=30)
    description6: Optional[str] = Field(max_length=100)
    media6: Optional[str]


class RcsMMSCarouselBody(BaseModel):
    title1: Optional[str] = Field(max_length=30)
    description1: str = Field(max_length=100)
    media1: Optional[str]
    title2: Optional[str] = Field(max_length=30)
    description2: Optional[str] = Field(max_length=100)
    media2: Optional[str]
    title3: Optional[str] = Field(max_length=30)
    description3: Optional[str] = Field(max_length=100)
    media3: Optional[str]
    title4: Optional[str] = Field(max_length=30)
    description4: Optional[str] = Field(max_length=100)
    media4: Optional[str]
    title5: Optional[str] = Field(max_length=30)
    description5: Optional[str] = Field(max_length=100)
    media5: Optional[str]
    title6: Optional[str] = Field(max_length=30)
    description6: Optional[str] = Field(max_length=100)
    media6: Optional[str]


class RcsCHATCarouselBody(BaseModel):
    title1: Optional[str] = Field(max_length=30)
    description1: str = Field(max_length=100)
    media1: Optional[str]
    title2: Optional[str] = Field(max_length=30)
    description2: Optional[str] = Field(max_length=100)
    media2: Optional[str]
    title3: Optional[str] = Field(max_length=30)
    description3: Optional[str] = Field(max_length=100)
    media3: Optional[str]
    title4: Optional[str] = Field(max_length=30)
    description4: Optional[str] = Field(max_length=100)
    media4: Optional[str]
    title5: Optional[str] = Field(max_length=30)
    description5: Optional[str] = Field(max_length=100)
    media5: Optional[str]
    title6: Optional[str] = Field(max_length=30)
    description6: Optional[str] = Field(max_length=100)
    media6: Optional[str]


class LocationInfo(BaseModel):
    query: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    label: Optional[str]


class ShowLocationInfo(BaseModel):
    fallbackUrl: str = Field(max_length=1000)
    location: LocationInfo


class PostParameterInfo(BaseModel):
    P_NAME: str
    P_MID: str


class OpenUrlInfo(BaseModel):
    url: str
    isHalfView: Optional[str] = Field(default="false")
    postParameter: Optional[PostParameterInfo]


class CreateCalendarEventInfo(BaseModel):
    title: str
    description: str
    startTime: str
    endTime: str


class CopyToClipboardInfo(BaseModel):
    text: str


class ComposeTextMessageInfo(BaseModel):
    phoneNumber: str
    text: str


class DialPhoneNumberInfo(BaseModel):
    phoneNumber: str


class UrlActionInfo(BaseModel):
    """
    단말기에 기본 웹 브라우저로 설정된 앱을 통해서, 웹페이지로 이동할 수있습니다
    """

    openUrl: OpenUrlInfo


class LocalBrowserActionInfo(BaseModel):
    """
    단말기의 메시지 앱 내부 브라우저를 통해 웹페이지로 이동할 수 있습니다
    """

    openUrl: OpenUrlInfo


class MapActionInfo(BaseModel):
    """
    미리 지정된 위치를 보여주거나 사용자의 현재 위치를 서버로 전송 할 수 있습니다.
    """

    showLocation: Optional[ShowLocationInfo]
    requestLocationPush: Optional[Dict]


class CalendarActionInfo(BaseModel):
    """
    사용자의 캘린더에 특정 일정을 등록 할 수 있습니다.
    """

    createCalendarEvent: CreateCalendarEventInfo


class ClipboardActionInfo(BaseModel):
    """
    특정 문구를 사용자 단말이 자동으로 복사 할 수 있게 합니다
    """

    copyToClipboard: CopyToClipboardInfo


class ComposeActionInfo(BaseModel):
    """
    다른 번호로 메시지를 보낼 수 있도록 대화방을 엽니다.
    """

    composeTextMessage: ComposeTextMessageInfo


class DialerActionInfo(BaseModel):
    """
    특정 전화번호로 전화를 걸 수 있습니다.
    """

    dialPhoneNumber: DialPhoneNumberInfo


class PostbackInfo(BaseModel):
    data: str = Field(max_length=2048)


class ReplyActionInfo(BaseModel):
    """
    버튼을 눌러서 답장할수있습니다.
    """

    displayText: str = Field(max_length=200)
    postback: PostbackInfo


class ActionInfo(BaseModel):
    urlAction: Optional[UrlActionInfo]
    localBrowserAction: Optional[LocalBrowserActionInfo]
    mapAction: Optional[MapActionInfo]
    calendarAction: Optional[CalendarActionInfo]
    clipboardAction: Optional[ClipboardActionInfo]
    composeAction: Optional[ComposeActionInfo]
    dialerAction: Optional[DialerActionInfo]
    displayText: str = Field(max_length=200)
    postback: PostbackInfo


class SuggestionInfo(BaseModel):
    action: Optional[ActionInfo]
    reply: Optional[ReplyActionInfo]


class ButtonInfo(BaseModel):
    suggestions: List[SuggestionInfo]


class CommonInfo(BaseModel):
    """
    msgServiceType enum: [rcs, legacy]
    rcs : rcs 부달시 실패코드 회신
    rcs, legcy : rcs 부달시, xMS로fallback전송
    * legacy만 보낼 수는 없음
    """

    msgId: str = Field(max_length=40)
    userContact: str = Field(max_length=40)
    scheduleType: Optional[enums.ScheduleTypeEnum]
    msgGroupId: Optional[str] = Field(max_length=20)
    msgServiceType: enums.MessageServiceTypeEnum


class RcsInfo(BaseModel):
    chatbotId: str = Field(max_length=40)
    agencyId: Optional[str] = Field(max_length=20)
    """
    # agencyId
    대행사 ID
    ktbizrcs (Default: KT 중계가 브랜드 대행사인 경우)
    Maximum : 20Byte
    * Agency ID는 "Rcs Biz Center - 브랜드 운영관리" 에서 기업의 브랜드가 대행사 권한을 부여한 대행사의 ID
    Agency ID가 "ktbizrcs" 가 아닌 경우 필수 입력 필요.
    """
    messagebaseId: Union[enums.MessageEnum, enums.RCSMessageEnum, str]
    serviceType: enums.ServiceTypeEnum
    expiryOption: Optional[enums.ExpiryOptionEnum]
    """
    # expiryOption
    메시지 처리 옵션 enum: [1, 2]
    - 1: 최대3일 까지 결과 webhook 전송 (default)
    - 2: ‘설정시간’ 까지 결과 webhook 전송
    * ‘설정시간’ 은 통신사 정책에 따라 변경 가능,
    현재 ‘설정시간’ 은 별도 안내 (ex. 10초~3분)

    * 양방향 메시지 발송 시에는2로 설정해서 발송해야 한다
    """
    header: enums.HeaderEnum

    footer: Optional[str] = Field(max_length=20, regex=r"^[\d-]*$")
    """
    # footer
    수신거부 전화번호 (숫자, - 만 가능, Max: 20 자리)
    - header가0인 경우, footer 입력 불가
    - header가1인 경우, footer 필수
    """

    @validator("footer")
    def footer_validator(cls, v, values, **kwargs):
        if values["header"] == enums.HeaderEnum.NOT_ADVERTISE and v:
            raise ValueError("If header is 0 then footer can not be provided.")
        elif values["header"] == enums.HeaderEnum.ADVERTISE and not v:
            raise ValueError("If header is 1 then footer should be provided.")
        return v

    cdrId: Optional[str]
    """
    # cdrId
    청약 ID 기록시 기록한 ID로 과금 처리 된다.
    Ex)
    RCS ID: A, B, C청약을 한 기업이 토큰 인증을A로 받고,
    메시지 발송은 cdrId에B로 기록하여 발송하면A로 과금 되던 것이B로 과금 수행한다.
    - 청약 ID만 기록 가능
    - 해당 기업의 청약인지 Value 체크 수행
    """
    copyAllowed: Optional[bool] = True
    """
    # copyAllowed
    단말의 메시지 복사 기능 허용 여부.
    - true: 복사 허용 (default)
    - false: 복사 허용 하지 않음
    """

    body: Union[
        RcsSMSBody,
        RcsLMSBody,
        RcsMMSBody,
        RcsCHATBody,
        RcsSMSCarouselBody,
        RcsLMSCarouselBody,
        RcsMMSCarouselBody,
        RcsCHATCarouselBody,
        dict,
    ]
    """
    # body
    메시지베이스에서 치환할 파라미터의 정보를 담은 json object.
    Maximum : 10240Byte
    - RCSSMS, RCSLMS, RCSMMS인 경우
      - "title": max 30자
      - "description" :
        RCSSMS max 100자
        RCSLMS max 1300자
        RCSMMS 카드별 총합max 1300자.
      - "media" :"maapfile://{fileId}"
    - RCSTMPL인 경우
      (RCS Biz Center에 미리 등록된 메시지베이스의 변수부에 데이터 수록)
      변수부 가변 값의 총 합이 90자 이내여야 한다.

    * [별첨1] 엑셀파일 참조(A2P+양방향 메시지양식으로 업데이트 필요)
    - RCSCHAT인 경우
      - "title": max 30자
      - "description" : 1300자
      - "media" :"maapfile://{fileId}"
    """

    buttons: Optional[List[Union[ButtonInfo, EmptyDict]]]
    """
    # buttons
    GSMA RCC.07의3.6.10.4의 ‘suggestions’ 규격에 준하여 버튼을 구성
    ㅇRCSSMS, RCSLMS, RCSMMS, RCSCHAT인 경우에만 사용.
    suggestions의 리스트이며 리스트의 각 항목은 carousel의 카드 순서에 맞도록 삽입된다.
    - RCSSMS 최대 버튼 수: 1개
    - RCSLMS 최대 버튼 수: 3개
    - RCSMMS card당 최대 버튼 수: 2개
    (carousel에서 버튼이 없는 카드는 {}로 표시, 예제 참조)
    ㅇRCSTMPL인 경우
    버튼의 변수부를 등록 하여 사용하며, 해당 필드 허용하지 않음.
    """

    chipList: Optional[List[SuggestionInfo]]
    """
    # chipList
    GSMA RCC.07의3.6.10.4의 ‘suggestion’ 규격에 따라 chiplist를 구성(RCC.07의 기준 버전 확인 필요)
    ㅇRCSCHAT인 경우에만 사용.
    * Chiplist는 최대 11개까지 사용 가능하다
    """

    replyId: Optional[str] = Field(max_length=40)
    """
    # replyId
    양기업의 양방향 momsg를 수신할 때 포함된 replyID를 그대로 넣어서 전송한다
    Maximum : 40Byte
    ㅇRCSCHAT인 경우에 반드시 포함되어야 하며, RCSCHAT이 아닌 경우에는 포함되면 발송이 실패된다
    *양방향서비스에서 양방향 대화의 세션을 관리하는 기준으로, 고객이 양방향 MO를 수행할 때마다 새롭게 할당되며, 유효시간은 24시간임. 유효시간이 만료된 replyId포함되어 발송되면 실패처리된다
    """

    class Config:
        smart_union = True


class LegacyInfo(BaseModel):
    """
    (RCS부달시 RCS중계플랫폼이 SMS/LMS/MMS를 크로샷으로 fallback 전송.
    legacy만 보낼 수는 없으며, RcsInfo 영역이 반드시 존재 해야 함)
    """

    serviceType: enums.LegacyServiceTypeEnum
    """
    Fallback은SMS/LMS에 대해서만 제공하고, MMS,CHAT에 대해서는 제공하지 않는다
    """
    callback: str = Field(max_length=20)
    subject: Optional[str] = Field(max_length=50)
    msg: str = Field(max_length=4000)
    """
    SMS : 80Byte
    LMS : 4000Byte (한글 2000자 이내)
    MMS : 4000Byte (한글 2000자 이내 + 이미지, 동영상)
    """
    contentCount: int = Field(ge=0, le=3)
    """
    미디어파일의 갯수
    - 0: SMS/LMS인 경우, 미디어파일 없는 경우
    - 1~3 : (TBD) MMS인 경우
    """
    contentData: Optional[str] = Field(max_length=250)
    """
    (TBD) MMS 에서 사용하는 이미지파일의 정보
    - 컨텐츠위치^컨텐츠타입^컨텐츠서브타입
        - 컨텐츠위치: File Upload시 수신받은 URL (‘http’ 로 시작하는 url로 사용)
        - 컨텐츠타입: IMAGE = 1, AUDIO = 2, VIDEO = 3
        - 컨텐츠서브타입:
            - [IMAGE] 0 = JPG
            - [AUDIO] 0 = AAC, 1 = MA3, MMF
            - [VIDEO] 0 = MP4+AAC
    - 여러 개인 경우, "|" 이용
    예) http://10.217.59.209:5084/data/MEDIA/RCS/send/2021/08/09/test004.jpg^1^JPG
    Maximum : 250Byte
    """


class ErrorInfo(BaseModel):
    code: str
    message: str


class ResponseErrorInfo(BaseModel):
    status: str
    error: ErrorInfo


class StatusInfo(BaseModel):
    """
    메시지 전송 결과
    """

    rcsId: Optional[str] = Field(max_length=20)
    msgId: str = Field(max_length=40)
    userContact: Optional[str] = Field(max_length=40)
    status: enums.MessageStatusEnum
    serviceType: Optional[enums.ServiceTypeEnum]
    mnoInfo: Optional[enums.MnoInfoEnum]
    sentTime: Optional[str] = Field(regex=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{2}$")
    error: Optional[ErrorInfo]
    legacyError: Optional[LegacyErrorCodeEnum]
    timestamp: str = Field(regex=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{2}$")
    autoReplyMsgId: Optional[str] = Field(max_length=40)
    postbackId: Optional[str] = Field(max_length=40)
    chatbotId: Optional[str] = Field(max_length=40)
    bill: Optional[enums.BillEnum]


class QuerystatusInfo(BaseModel):
    queryId: Optional[str] = Field(max_length=40)
    moreToSend: Optional[int] = Field(ge=0, le=1)


class ResponseInfo(BaseModel):
    status: str
    data: dict


class TextMessageInfo(BaseModel):
    textMessage: str


class FileMessage(BaseModel):
    fileName: str
    fileUrl: str
    fileMIMEType: str
    fileSize: int


class FileMessageInfo(BaseModel):
    fileMessage: FileMessage


class GeolocationPushMessage(BaseModel):
    label: Optional[str]
    timestamp: Optional[str]
    timeOffset: Optional[str]
    pos: Optional[str]
    radius: Optional[int]


class UserLocationInfo(BaseModel):
    geolocationPushMessage: GeolocationPushMessage


class MessageInfo(BaseModel):
    replyId: str = Field(max_length=40)
    eventType: enums.EventTypeEnum
    """
    양방향 MO메시지의 종류를 식별하기 위한 값으로, 총3개의 eventType이 사용된다. 각 eventType별로
    postbackId, PostbackData, displayText, messagebody 등의 설정여부가 달라진다
    - message
    고객이 직접 메시지를 입력한 경우에 설정됨
    - response
    고객이 단말 대화방에서 고정메뉴 또는 메시지의 reply 버튼 또는 chiplist의reply를 선택한 경우 설정
    - newuser
    고객이 단말 대화방을 최초 진입 시 설정됨
    Maximum : 10Byte
    """
    postbackId: Optional[str] = Field(max_length=40)
    postbackData: Optional[str] = Field(max_length=2048)
    displayText: Optional[str] = Field(max_length=200)
    messageBody: Union[TextMessageInfo, UserLocationInfo, FileMessageInfo, None]
    """
    eventType이message인 경우에만 설정
    - 텍스트 메시지의 경우 샘플
        `{"textMessage": "hello world"}`
    - 파일 메시지의 경우 샘플.
        ```
        {
            "fileMessage": {
                "fileName": "3686492106936898.jpeg",
                "fileUrl": "https://bd-media- hub.hermes.kt.com/data/chat/message/file/3686492106936898.jpeg",
                "fileMIMEType": "image/jpeg",
                "fileSize": 326130
            }
        }
        ```
    - userLocation 메시지의 경우 샘플
        ```
        {
            "geolocationPushMessage": {
                "label": "meeting location",
                "timestamp": "2021-08-10T09:19:44Z",
                "timeOffset": -540,
                "pos": "37.3587121 127.1151084",
                "radius": 0
            }
        }
        ```
    Maximum : 10240Byte
    """

    @validator("messageBody")
    def check_message_body(cls, v, values, **kwargs):
        if v:
            if values["eventType"] == enums.EventTypeEnum.MESSAGE:
                return v
            raise ValueError("messageBody is not allowed")

    userContact: str = Field(max_length=40)
    chatbotId: str = Field(max_length=40)
    timestamp: str = Field(regex=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{2}$")


class SendInfo(BaseModel):
    common: CommonInfo
    rcs: RcsInfo


class TokenInfo(BaseModel):
    rcsId: str
    rcsSecret: str
    grantType: str


class FileRegistInfo(BaseModel):
    fileId: str
    usageType: enums.FileUsageTypeEnum
    usageService: enums.FileUsageServiceEnum
    mimeType: str
    file: bytes
    description: Optional[str]


class FileInfo(BaseModel):
    fileId: Optional[str]
    usageType: enums.FileUsageTypeEnum
    usageService: enums.FileUsageServiceEnum
    mimeType: str
    status: enums.FileStatusEnum
    size: Optional[int]
    expiryDate: str = Field(regex=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{2}$")
    url: str
