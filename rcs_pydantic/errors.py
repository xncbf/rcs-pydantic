from enum import Enum


class TupleEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for item in cls:
            if item.value[0] == value:
                return item
        return super()._missing_(value)


class LegacyErrorCodeEnum(str, TupleEnum):
    pass


class ErrorCodeEnum(TupleEnum):
    """
    삼성 MaaP Core Enum of error codes.
    """

    # General errors
    MISSING_AUTHORIZATION_HEADER = (
        40001,
        "Valid access token in Authorization header is required for RESTful API calls.",
    )
    MISSING_TOKEN = (40002, "Authorization header does not contain a token. Note that token type is required.")
    INVALID_TOKEN = (40003, "Token has been tampered.")
    TOKEN_HAS_EXPIRED = (40004, "Token Has Expired")
    MALFORMED_TOKEN_PAYLOAD = (40005, "Token payload has insufficient information.")
    INVALID_CLIENT_ID = (40006, "Token is not issued to the client.")
    INSUFFICIENT_SCOPE = (40007, "Token is not authorized to use the scope.")
    INTERNAL_SERVER_ERROR = (41000, "Internal Server Error")
    RCS_REQUEST_TIMEOUT = (41001, "RCS Request Timeout")
    REVOCATION_FAILED = (41002, "Revocation Failed")
    THROTTLED_BY_MESSAGE_RATE = (41003, "Throttled by message rate")
    RCS_SERVER_BUSY = (41004, "RCS Server Busy")
    RCS_SERVER_TEMPORARILY_UNAVAILABLE = (41005, "RCS Server Temporarily unavailable")
    SESSION_DOES_NOT_EXIST = (41006, "Session does not exist")
    EXPIRED_BEFORE_SESSION_ESTABLISHMENT = (41007, "RCS 세션 연결 전 만료되어 발송 실패 ")
    SESSION_ALREADY_EXPIRED = (41008, "Session already expired")
    DEVICE_NOT_SUPPORT_REVOCATION = (41009, "aa")
    IMDN_RECEIVED_EVEN_ALREADY_REVOKED = (41010, "IMDN received even already revoked")
    MESSAGE_WAS_ALREADY_REVOKED = (41011, "aa")
    CONNECTING_RCS_ALLOCATOR_FAILED = (41100, "Message Status on Response of Sending Message API")
    CONNECTING_RCS_ALLOCATOR_TIMEOUT = (41101, "Message Status on Response of Sending Message API")
    RCS_ALLOCATION_FAILED = (41102, "Message Status on Response of Sending Message API")
    RCS_ALLOCATION_TIMEOUT = (41103, "Message Status on Response of Sending Message API")
    CONNECTING_RCS_FAILED = (41104, "Message Status on Response of Sending Message API")
    CONNECTING_RCS_TIMEOUT = (41105, "Message Status on Response of Sending Message API")
    SENDING_MESSAGE_TO_RCS_FAILED = (41106, "Message Status on Response of Sending Message API")
    SENDING_MESSAGE_TO_RCS_TIMEOUT = (41107, "Message Status on Response of Sending Message API")
    RCS_HANDLE_REQUEST_FAILED = (41108, "Message Status Webhook ")
    RCS_INTERNAL_SERVER_ERROR = (41109, "Message Status Webhook ")
    RCS_USER_NOT_FOUND = (41110, "Message Status Webhook ")
    PROCESS_REVOCATION_REQUEST_FAILED = (41117, "Message Status Webhook ")
    USER_FOR_MESSAGE_RECEIVING_NOT_FOUND = (41200, "aa")
    MESSAGE_NOT_ACCEPTABLE = (41201, "Message Session형성과정 중 단말의 SDP에 message송신에 필요한 feature tag가 없는 경우 발생")
    USER_IS_NOT_CAPABLE_FOR_TEXT = (41210, "Bot이 Text message를 보낼 때 user의 capability에 chat이 없는 경우 발생.")
    USER_IS_NOT_CAPABLE_FOR_FT = (41211, "Bot이 File message를 보낼 때 user의 capability에 fthttp가 없는 경우 발생")
    USER_IS_NOT_CAPABLE_FOR_RICHCARD = (
        41212,
        "Bot이 Richcard message를 보낼 때 user의 capability에 bot 또는 chatbot.sa가 없는 경우 발생",
    )
    USER_IS_NOT_CAPABLE_FOR_XBOTMESSAGE_1_0 = (
        41220,
        "clipboardAction, messageHeader, messageFooter, openrichcard, geolocationPushMessage, copyAllowed",
    )
    USER_IS_NOT_CAPABLE_FOR_XBOTMESSAGE_1_1 = (
        41221,
        "clipboardAction, localBrowserAction, messageHeader, messageFooter, openrichcard, geolocationPushMessage,"
        "copyAllowed Bot이 v1.1에 해당하는 Extended message를 보낼 때 user의 capability에 bot, chatbot.sa, xbotmessage "
        "1.1이 없는 경우 발생. 이 때 xbotmessage는 상위 version이 하위 version을 포함한다. (1.2 version이 있다면 1.1에 해당하는 "
        "capability를 가진 것으로 간주함)",
    )
    USER_IS_NOT_CAPABLE_FOR_XBOTMESSAGE_1_2 = (
        41222,
        "clipboardAction, localBrowserAction, messageHeader, messageFooter, openrichcard, geolocationPushMessage,"
        " copyAllowed, shareAction, streamingPlay",
    )
    USER_IS_NOT_CAPABLE_FOR_OPENRICHARD_1_0 = (
        41230,
        "Bot이 v1.0에 해당하는 Openrichcard를 보낼 때 user의 capability에 bot, chatbot.sa, xbotmessage 1.0이 없는 경우 발생",
    )
    USER_IS_NOT_CAPABLE_FOR_OPENRICHARD_1_1 = (41231, "v1.1에 해당하는 Openrichcard가 현재 정의 및 사용되지 않으므로, 실제 발생하지 않는 code")
    USER_IS_NOT_CAPABLE_FOR_OPENRICHARD_1_2 = (41232, "v1.2에 해당하는 Openrichcard가 현재 정의 및 사용되지 않으므로, 실제 발생하지 않는 code")
    USER_IS_NOT_CAPABLE_FOR_GEOLOCATION_PUSH_REQUEST = (41240, "User is not capable for GEOLOCATION PUSH REQUEST")
    FAILED_TO_GET_MESSAGE_CONTENT_TYPE = (41250, "Failed to get message content type")
    FILE_DOWNLOAD_FAILED = (41300, "aa")
    INVALID_STATE = (42001, "Bot is in an invalid state to call the API.")
    INVALID_MESSAGE = (42002, "Message is missing required fields or has malformed format.")
    INVALID_DATE_TIME_FORMAT = (42003, "Date and time format does not comply with ISO 8601.")
    MISSING_CONTACT = (42004, "Missing recipient information.")
    INVALID_CONTACT = (42005, "Incorrect contact format (e.g., phone number is not start with '+')")
    EMULATOR_ACCESS_ONLY = (42006, "Bot is in a state which allows access via Emulator only.")
    CONTACT_NOT_IN_WHITELIST = (42007, "Bot is accessible only to authorized users via MaaP client.")
    MISSING_MESSAGE_CONTENT = (42008, "Token Has Expired")
    INVALID_MESSAGE_CONTENT = (
        42009,
        "Message is not any of textMessage, fileMessage, audioMessage, geolocationPushMessage, richcardMessage,"
        " or isTyping.",
    )
    AMBIGUOUS_MESSAGE = (
        42010,
        "One and only one of textMessage, fileMessage, audioMessage, geolocationPushMessage, richcardMessage, "
        "or isTyping should be provided if sending a message to the user.",
    )
    INVALID_MESSAGE_STATUS = (42011, "Invalid MessageStatus")
    INVALID_ISTYPING_STATUS = (42012, "Invalid IsTyping Status")
    INVALID_TRAFFIC_TYPE = (42013, "Invalid TrafficType")
    INVALID_SUGGESTED_CHIPLIST_ASSOCIATION = (
        42014,
        "suggestedChipList can be used together with one and only one of textMessage, fileMessage, audioMessage, "
        "geolocationPushMessage, or richcardMessage.",
    )
    EMPTY_TEXT_MESSAGE = (42015, "Empty TextMessage")
    MISSING_RICHCARD = (
        42031,
        "richcardMessage should contain a message, which should contain either generalPurposeCard or"
        " generalPurposeCardCarousel.",
    )
    AMBIGUOUS_RICHCARD = (42032, "A message should contain either richcard or richcard carousel.")
    TOO_MANY_RICHCARDS = (42033, "Richcard carousel exceeds the maximum allowed richcards.")
    MISSING_RICHCARD_LAYOUT = (42034, "generalPurposeCard or generalPurposeCardCarousel should contain layout.")
    MISSING_RICHCARD_CONTENT = (42035, "generalPurposeCard or generalPurposeCardCarousel should contain content.")
    INVALID_CARDORIENTATION = (42036, "cardOrientation should be either HORIZONTAL or VERTICAL.")
    MISSING_IMAGE_ALIGNMENT = (42037, "Richcard HORIZONAL orientation should contain image alignment.")
    INVALID_IMAGE_ALIGNMENT = (42038, "imageAlignment should be either LEFT or RIGHT.")
    REDUNDANT_IMAGE_ALIGNMENT = (42039, "Richcard VERTICAL orientation should not contain image alignment.")
    INVALID_RICHCARD_CAROUSEL_CARDWIDTH = (
        42040,
        "Richcard carousel cardWidth should be either SMALL_WIDTH or MEDIUM_WIDTH.",
    )
    MISMATCHED_MEDIA_HEIGHT = (42041, "Media height cannot be TALL_HEIGHT for SMALL_WIDTH carousel.")
    INVALID_RICHCARD_CONTENT = (
        42042,
        "generalPurposeCard or generalPurposeCardCarousel content should have at least one of media, title, "
        "or description.",
    )
    INVALID_SUGGESTIONS = (42043, "Suggestion list should contain at least one suggested reply or action.")
    TOO_MANY_SUGGESTIONS_IN_CHIPLIST_MAX_11 = (42044, "Suggestion list exceeds the maximum allowed items.")
    INVALID_SUGGESTION = (42045, "Suggestion should be either reply or action.")
    AMBIGUOUS_SUGGESTION = (42046, "Suggestion should be one and only one reply or action.")
    AMBIGUOUS_SUGGESTED_ACTION = (42047, "Suggested action should be one and only one type of action.")
    TOO_MANY_SUGGESTIONS_IN_RICHCARD_MAX_4 = (42048, "Richcard suggestion list exceeds the maximun allowed items (4).")
    TOO_MANY_SUGGESTION_DATA_MAX_2048 = (42049, "Suggestion data exceeds the maxmun data size (2048).")
    INVALID_ACTION = (42050, "Either latitude and longitude or query are required in location.")
    INVALID_LOCATION = (42051, "Either latitude and longitude or query are required in location.")
    AMBIGUOUS_LOCATION = (42052, "Location should contain either query or latitude and longitude.")
    INVALID_MAPACTION = (42053, "One of showLocation or requestLocationPush is required in mapAction.")
    AMBIGUOUS_MAPACTION = (42054, "mapAction should contain either showLocation or requestLocationPush.")
    INVALID_DIALERACTION = (
        42055,
        "One of dialPhoneNumber, dialEnrichedCall, or dialVideoCall is required in dialerAction.",
    )
    AMBIGUOUS_DIALERACTION = (42056, "dialerAction should contain only one type of dialer action.")
    INVALID_COMPOSEACTION = (
        42057,
        "Either composeTextMessage or composeRecordingMessage is required in composeAction.",
    )
    AMBIGUOUS_COMPOSEACTION = (42058, "composeAction should contain only one type of compose action.")
    INVALID_SETTINGSACTION = (
        42059,
        "Either enableDisplayedNotifications or disableAnonymization is required in settingsAction.",
    )
    AMBIGUOUS_SETTINGSACTION = (42060, "settingsAction should contain only one type of settings action.")
    INVALID_CLIPBOARDACTION = (42061, "ClipboardAciton should contain copy text.")
    MISSING_LOCALBROWSERACTION = (42062, "LocalBrowserAction should contain url.")
    INVALID_SHAREACTION = (42063, "ShareAction should contain url.")
    AMBIGUOUS_SHAREACTION = (42064, "Sharetext of ShareAction should contain text.")
    INVALID_THUMBNAIL = (
        42100,
        "thumbnailFileSize and thumbnailContentType should be provided together with thumbnailUrl.",
    )
    MISSING_FILEURL = (42101, "Missing FileUrl")
    MISSING_AUDIO_FILEURL = (42102, "Missing AudioFile Url")
    MISSING_POS = (42103, "Missing Pos")
    MISSING_MEDIA_INFORMATION = (42104, "Missing Media Information")
    MISSING_MEDIA_CONTENT_TYPE = (42105, "Missing Media Information")
    MISSING_MEDIA_FILESIZE = (42106, "Missing Media Information")
    MISSING_MEDIA_HEIGHT = (42107, "Missing Media Information")
    MISSING_POSTBACK_DATA_INFORMATION = (42108, "Missing postback data information")
    INVALID_LOCATION_LABEL = (42201, "geolocationPushMessage should not contain label length > 200 Characters.")
    INVALID_MEDIA_CONTENT_DESCRIPTION = (
        42202,
        "Content Description of media is not in limit <1 Character or >200 Character.",
    )
    INVALID_MEDIA_TITLE = (42203, "Media title is not in limit <1 Character or >200 Character.")
    INVALID_MEDIA_DESCRIPTION = (42204, "Media card description is not in limit <1 Character or >2000 Character.")
    TOO_MANY_CONTENTS_IN_RICHARD_CAROUSEL = (42205, "Richcard carousel list exceeds the maximum allowed items (10).")
    INVALID_MEDIA_FILE_SIZE = (42206, "Minimum Value for file size is 0.")
    INVALID_EXPIRY_TIME_FORMAT = (42207, "Invalid expiry time")
    INVALID_EXPIRY_TIME = (42208, "Invalid expiry time")
    AMBIGUOUS_OPENRICHCARD = (
        42301,
        "OpenrichcardMessage should contain a message, which should contain either generalPurposeCard or "
        "generalPurposeCardCarousel.",
    )
    MISSING_OPENRICHCARD = (42302, "A OpenrichcardMessage should contain open_rich_card.")
    MISSING_OPENRICHCARD_LAYOUT_WIDGET = (42303, "Openrichcard should contain widget.")
    MISSING_OPENRICHCARD_VIEW_CONTENT = (42304, "View layout of Openrichcard do not have mandatory parameters.")
    MISSING_OPENRICHCARD_LINEARLAYOUT_CONTENT = (42305, "Parameters in LinearLayout have invalid value.")
    MISSING_OPENRICHCARD_TEXTVIEW_CONTENT = (42306, "TextView layout of Openrichcard do not have mandatory parameters.")
    INVALID_CONTENTS_IN_OPENRICHCARD_TEXTVIEW = (42307, "Parameters in TextView have invalid value.")
    INVALID_TEXT_LENGTH_IN_OPENRICHCARD_TEXTVIEW = (42308, "text is not limit in [0 < text < 2000].")
    MISSING_OPENRICHCARD_IMAGEVIEW_CONTENT = (
        42309,
        "ImageView layout of Openrichcard do not have mandatory parameters.",
    )
    TOO_SMALL_MEDIA_IN_OPENRICHCARD_IMAGEVIEW = (42310, "MediaFileSize is under 0.")
    INVALID_OPENRICHCARD_IMAGEVIEW_SCALETYPE = (
        42311,
        "ScaleType value of ImageView should be center or centerCrop or centerInside or fitCenter or fitEnd or "
        "fitStart or fitXY or matrix.",
    )
    MISSING_OPENRICHCARD_WIDTH_OR_HEIGHT = (42312, "width or height is not in Openrichcard.")
    INVALID_OPENRICHCARD_WIDTH_OR_HEIGHT = (42313, "width or height in Openrichcard has invalid value.")
    INVALID_OPENRICHCARD_COMMON_CONTENTS = (42314, "Common Contents in Openrichcard has invalid value.")
    TOO_MANY_CHILD_IN_OPEN_RICH_CARD = (42315, "aa")
    INVALID_FILE_TYPE = (42401, "Invalid file type")
    DOWNLOAD_FAILURE = (42402, "Download failure")
    MISSING_CONTACT_1 = (42501, "Missing contact")
    MISSING_CONTENT_2 = (42502, "Missing content")
    MISSING_TITLE = (42503, "Missing title")
    MISSING_DESCRIPTION = (42504, "Missing description")
    MISSING_IMAGE_URL = (42505, "Missing image url")
    MISSING_IMAGE_TYPE = (42506, "Missing image type")
    MISSING_BUTTON_LINK = (42507, "Missing button link")
    MISSING_BUTTON_TEXT = (42508, "Missing button text")
    INVALID_TITLE = (42509, "Invalid title")
    INVALID_DESCRIPTION = (42510, "Invalid description")
    INVALID_IMAGE_URL_ADDRESS = (42511, "Invalid image url address")
    INVALID_BUTTON_URL_ADDRESS = (42512, "Invalid button url address")
    INVALID_BUTTON_TEXT = (42513, "Invalid button text")
    DUPLICATED_MESSAGE_ID = (42514, "Duplicated message ID")
    TOO_MANY_REQUEST = (42601, "Too Many Request")


class MaaPErrorCodeEnum(Enum):
    """
    이동통신사 MaaP Core Enum of error codes.
    """

    MISSING_AUTHORIZATION_HEADER = (50001, "Authorization 헤더 파라미터 누락")
    MISSING_TOKEN = (50002, "Authorization 헤더 값 누락")
    INVAILD_TOKEN = (50003, "토큰이 일치하지 않습니다.")
    TOKEN_HAS_EXPIRED = (50004, "토큰이 만료되었습니다.")
    AUTHORIZATION_ERROR = (50005, "인증 토큰 에러")
    INVALID_CLIENT_ID = (50006, "요청된 계정 정보를 찾을 수 없습니다(BP ID)")
    INVALID_SENDER_ID = (50007, "요청된 중계사 전송 계정을 찾을 수 없습니다(RCS ID)")
    INVALID_PASSWORD = (50008, "잘못된 패스워드")
    NON_ALLOWED_IP = (50009, "접근 허용된 IP가 아닙니다")
    INVALID_STATE = (50100, "메시지 전송을 할 수 없는 상태입니다. (서버의 요청 거부)")
    MESSAGE_TPS_EXCEEDED = (50201, "RCS 메시지 TPS가 초과되었습니다.")
    MESSAGE_QUOTA_EXCEEDED = (50202, "RCS 메시지 Quota가 초과되었습니다.")
    SYSTEM_ERROR = (59001, "시스템 에러")
    IO_ERROR_IO = (59002, "에러 발생")
    DUPLICATION_ERROR = (51003, "중복 Key 오류")
    PARAMETER_ERROR = (51004, "요청 파라미터 형식 오류")
    JSON_PARSING_ERROR = (51005, "요청 Body JSON 파싱 에러")
    DATA_NOT_FOUND = (51006, "데이터를 찾을 수 없음")
    DUPLICATED_AUTO_REPLY_MSG_ID = (51007, "이미 사용 중인 자동응답 메시지 ID입니다.")
    DUPLICATED_POSTBACK_ID = (51008, "이미 사용 중인 Postback ID입니다.")
    INVALID_PHONE_NUMBER_FORMAT = (52001, "전화번호 형식이 일치하지 않습니다")
    INVALID_MESSAGE_STATUS = (52002, "요청을 처리할 수 없는 상태입니다.")
    BOT_ALEADY_EXISTS = (52003, "이미 사용 중인 챗봇 ID입니다.")
    BOT_CREATION_FAILED = (52004, "챗봇을 생성할 수 없습니다.")
    BOT_UPDATE_FAILED = (52005, "챗봇 정보를 변경할 수 없습니다.")
    BRAND_DELETE_FAILED = (52006, "챗봇이 있는 브랜드는 삭제 할수 없습니다.")
    INVALID_CHATBOT_SERVICE_TYPE = (52007, "챗봇 Type은 a2p, chatbot 로 설정해야 함")
    MISMATCHED_CHATBOT_ID = (52008, "요청 URL Parameter의 챗봇 Id와 Body Parameter 불일치")
    PERSISTENT_MENU_PERMISSION_ERROR = (52009, "Persistent Menu 등록이 허용되지 않습니다.")
    INVALID_PERSISTENT_MENU_DATA = (52010, "Persistent menu JSON 데이터 오류")
    MESSAGE_TRANSMISSION_TIME_EXCEEDING = (52016, "실시간 메시지 인입 후 10초안에 삼성으로 전달되지 못함")
    MESSAGEBASE_ID_STOPPED_TEMPORARILY = (52023, "메시지 베이스의 상태가 'pause'인 메시지 베이스 메시지로 전문 구성하여 전송 시도 시")
    INVALID_WEBHOOK_REQUEST_PARAMETER = (52101, "잘못된 Webhook 중계사 요청 파라미터 입니다.")
    WEBHOOK_HOST_CONNECT_ERROR = (52102, "Webhook 중계 시스템 연결 오류")
    WEBHOOK_HOST_SERVER_REQUEST_FAILURE = (52103, "중계사 Webhook 전송 요청을 실패 했습니다.")
    WEBHOOK_RESPONSE_RECEIVE_FAILURE = (52104, "중계사 Webhook 처리 응답 수신 오류가 발생 했습니다.")
    WEBHOOK_MESSAGE_NON_RECEIVE_FAILURE = (52105, "Webhook 메시지 미 수신 오류가 발생 했습니다.")
    WEBHOOK_MESSAGE_PROCESS_FAILURE = (52106, "Webhook 메시지 처리 오류가 발생 했습니다.")
    INVALID_AUTO_REPLY_MESSAGE_ID = (52201, "자동응답 메시지 ID가 존재하지 않습니다.")
    AUTO_REPLY_MESSAGE_CONTENTS_ERROR = (52202, "자동응답 메시지 내용 중 누락된 필수 항목이 있습니다.")
    INVALID_FILE_TYPE = (53001, "요청을 처리할 수 없는 파일 유형입니다.")
    FILE_ATTRIBUTE_ERROR = (53002, "파일 속성 오류")
    FILE_ID_FORMAT_ERROR = (53003, "fileID가 없거나 ID형식에 맞지 않음")
    FILE_UPLOAD_ERROR = (53004, "File 저장 오류")
    INVALID_MULTI_PART_REQUEST = (53005, "Multipart 데이터 전송 오류")
    ATTACHED_FILE_SIZE_ERROR = (53006, "업로드 파일 크기 초과")
    INVAILD_CONTACT_NUMBER_USER = (54001, "자사 고객이 아닙니다.")
    NO_RCS_CAPABILITY = (54002, "자사 고객이지만, RCS메시지를 수신할 수 있는 가입자가 아닙니다.")
    UNABLE_SENDING_TO_RECIPIENT = (54003, "단말기기로 RCS 메시지를 전송할 수 없습니다.")
    MAA_P_INTERNAL_ERROR = (54004, "MaaP 시스템 혹은 RCS 프로토콜 상의 이슈로 발송 실패되었음 (삼성 에러 40001 ~ 41100, 42601)")
    CORP_CONTENT_ERROR = (55001, "기업 정보 내용이 누락된 필수항목이 있습니다.")
    INVALID_PROPERTY = (55002, "필수 파라미터 검증 오류")
    AGENCY_CONTENT_ERROR = (55101, "대행사 정보 내용이 누락된 필수 항목이 있습니다.")
    INVALID_AGENCY_ID = (55102, "AgencyID가 존재하지 않습니다.")
    AGENCY_ID_PERMISSION_ERROR = (55103, "BrandID에 대행 권한이 없는 AgencyID")
    CONTRACT_CONTENT_ERROR = (55104, "계약 정보 내용이 부정확하거나 누락된 필수 항목이 있습니다.")
    BRAND_CONTENT_ERROR = (55201, "브랜드 정보 내용이 누락된 필수항목이 있습니다.")
    BRAND_NAME_ERROR = (55202, "브랜드 명이 누락되어 있습니다.")
    BRAND_PROFILE_IMAGE_ERROR = (55203, "브랜드 프로필 이미지가 누락되어 있습니다.")
    BRAND_CS_NUMBER_ERROR = (55204, "브랜드 CS번호가 누락되어 있습니다.")
    BRAND_MENU_ERROR = (55205, "브랜드 메뉴 최대 개수를 초과하였거나 부정확합니다. ")
    BRAND_CATEGORY_ERROR = (55206, "브랜드 카테고리 설정이 잘못되어 있습니다. ")
    BRAND_HOMEPAGE_ERROR = (55207, "브랜드 홈페이지 설정이 잘못되어 있습니다.")
    BRAND_EMAIL_ERROR = (55208, "브랜드 이메일 설정이 잘못되어 있습니다.")
    BRAND_ADDRESS_ERROR = (55209, "브랜드 주소가 잘못되어 있습니다.")
    INVALID_BRAND_ID = (55210, "브랜드ID가 존재하지 않음")
    BOT_CONTENT_ERROR = (55301, "챗봇 정보 내용이 부정확하거나 누락된 필수항목이 있습니다.")
    INVALID_BOT_ID = (55302, "BotID(발신번호)가 전화번호 형식에 맞지 않음")
    BOT_ID_PERMISSION_ERROR = (55303, "BrandID에 존재하지 않는 BotID")
    MESSAGEBASE_CONTENT_ERROR = (55501, "메시지베이스 내용이 부정확하거나 누락된 필수항목이 있습니다.")
    INVALID_MESSAGEBASE_ID = (55502, "MessagebaseID가 존재하지 않음")
    MESSAGEBASE_ID_PERMISSION_ERROR = (55503, "BrandID에 존재하지 않는 MessagebaseID입니다.")
    INVALID_FORMATSTRING = (55504, "messagebase의 formatstring 누락된 필수 항목이 있습니다.")
    INVALID_MESSAGEBASE_POLICY_INFO = (55505, "messagebase의 policy Info가 부정확하거나 누락된 필수 항목이 있습니다.")
    INVALID_MESSAGEBASE_PARAM = (55506, "messagebase의 param 부정확하거나 누락된 필수 항목이 있습니다.")
    INVALID_MESSAGEBASE_ATTRIBUTE = (55507, "messagebase의 attribute 부정확하거나 누락된 필수 항목이 있습니다.")
    INVALID_MESSAGEBASE_TYPE = (55508, "messagebase의 type 부정확하거나 누락된 필수 항목이 있습니다.")
    MISMATCHING_PRODUCT_TYPE = (55509, "messagebaseID의 product type과 일치하지 않음")
    MESSAGEBASE_FORM_CONTENT_ERROR = (55601, "MessagebaseForm 내용이 부정확하거나 누락된 필수항목이 있습니다.")
    INVALID_MESSAGEBASEFORM_ID = (55602, "messagebaseformID가 존재하지 않습니다.")
    INVALID_MESSAGE_BASE_PRODUCT_CODE = (55603, "messaegBase의 상품코드 에러")
    PROHIBITED_TEXT_CONTENT = (55701, "(광고) 를 사용할 수 없음")
    ACTION_BUTTON_PERMISSION_ERROR = (55702, "Action button이 허용되지 않는 messagebaseID에서 Action button을 사용하였음")
    PROHIBITED_HEADER_VALUE = (55703, "허용되지 않은 header 값 사용")
    PROHIBITED_FOOTER_FIELD = (55704, "header 값과 일치 하지 않은 footer 사용 (ex. header가 0 인데, footer 가 있음)")
    MISSING_FOOTER_CONTENT = (55705, "footer값이 누락되어 있습니다 (ex. header가 1 인데, footer 가 없음)")
    FOOTER_CONTENT_SYNTAX_ERROR = (55706, "footer validation 오류 (ex. 숫자, 하이픈만 가능. 20자리)")
    CONTENT_PATTERN_ERROR = (55707, "등록한 패턴과 일치 하지 않음")
    EXCEEDED_MAX_CHARACTER_OF_TITLE = (55708, "title 최대글자수를 초과했습니다.")
    EXCEEDED_MAX_CHARACTER_OF_DESCRIPTION = (55709, "description 최대글자수를 초과했습니다.")
    EXCEEDED_MAX_NUMBER_OF_BUTTONS = (55710, "최대 버튼수를 초과했습니다.")
    MISMATCHING_NUMBER_OF_CAROUSEL_CARD = (55711, "messagebaseID의 number of card 와 입력이 일치하지 않음")
    EXCEEDED_MAX_SIZE_OF_MEDIA = (55712, "최대 미디어 용량을 초과했습니다.")
    EXCEEDED_REPLY_ID_USAGE_COUNT = (55713, "Reply ID의 사용횟수 초과했습니다.")
    EXPIRED_REPLY_ID = (55714, "Reply ID의 유효시간이 만료되었습니다.")
    NOT_FOUND_REPLY_ID = (55715, "Reply ID가 존재하지 않음")
    GW_VENDOR_CONTENT_ERROR = (55801, "중계사 정보가 부정확하거나 누락된 필수 항목이 있습니다.")
    INVALID_MESSAGE = (55802, "메시지 형식이 부정확하거나 누락된 필수항목이 있습니다.")
    MESSAGE_SYNTAX_ERROR = (55803, "메시지 기술방법이 잘못되었습니다.")
    MISSING_MESSAGE_CONTENT = (55804, "메시지 내용이 누락되었거나 부정확합니다.")
    INVALID_MESSAGE_CONTENT = (55805, "요청을 처리할 수 없는 메시지 유형입니다.")
    DUPLICATED_MESSAGE_ID = (55806, "같은 메시지 ID로 두번 이상 메시지 발송이 요청됨")
    INVALID_CHATBOT_PERMISSION = (55807, "챗봇 권한 오류")
    INVALID_CHATBOT_STATUS = (55808, "발신 가능한 챗봇 상태가 아님")
    INVALID_AGENCY_PERMISSION = (55809, "대행사 권한 오류")
    INVALID_EXPIRY_FIELD = (55810, "메시지 유효기간 입력값 오류")
    EXCEEDED_MAX_CHARACTER_OF_PARAM = (55811, "메시지베이스 파라미터의 길이가 한계값 이상")
    BUTTONS_NOT_ALLOWED = (55812, "버튼 필드를 받을 수 없는 메시지베이스 입니다.")
    EXCEED_BUTTON_TEXT_LENGTH = (55813, "최대 버튼 글자수 초과")
    INVALID_MESSAGE_BASE_BUTTONS = (55814, "버튼 형식 오류")
    MESSAGE_BODY_FILE_NOT_FOUND = (55815, "존재하지 않는 File이거나 usageType 오류")
    MISMATCHED_SUGGESTIONS_COUNT = (55816, "Empty suggestions array 허용 안함")
    INVALID_DEST_PHONE_NUMBER = (55817, "수신 번호 형식 오류")
    INVALID_MESSAGE_BASE_ID = (55818, "메세지베이스 ID가 존재하지 않음")
    INVALID_CHATBOT_ID = (55819, "챗봇ID가 존재하지 않음")
    REVOKED_MESSAGE = (55820, "Webhook Revoked 메시지")
    ETC_TIME_OUT = (55821, "전송 성공 불확실함 (revocation fail 등)")
    CANCELED_MESSAGE = (55822, "메시지 취소되어, 전송안됨")
    INVALID_CHATBOT_YN = (55822, "양방향 서비스 사용불가")
    MISMATCHED_SUGGESTED_CHIP_LIST_COUNT = (55823, "Empty suggestedChipList array 허용 안함")
    CHIPLIST_NOT_ALLOWED = (55824, "칩리스트 필드를 사용할 수 없습니다.")
    BUTTONS_REPLY_NOT_ALLOWED = (55825, "버튼 필드에 Reply를 사용할 수 없습니다.")
    MISMATCHED_CAROUSEL_BUTTON_COUNT = (55880, "메시지카드 버튼 갯수 상이")
    MISMATCHED_CHIP_LIST_COUNT = (55881, "칩리스트 개수 초과")
    CHIP_LIST_NOT_ALLOWED = (55882, "ChipList 발송 가능하지 않음")
    INVALID_REPLY_ID = (55883, "유효한 replyId 아님")
    MISSING_REPLY_ID = (55884, "replyId 값 누락 됨")
    INVALID_USER_CONTACT_FOR_SESSION_MESSAGE = (55885, "replyId 와 일치하는 수신번호가 아님")
    INVALID_CHATBOT_ID_FOR_SESSION_MESSAGE = (55886, "replyId 와 일치하는 Chatbot ID 아님")
    INVALID_MESSAGE_BASE_PRODUCT_CODE_FOR_SESSION_MESSAGE = (55887, "messagebase 상품 코드가 세션 메시지 가능하지 않음")
    NOT_ALLOWED_CHATBOT_FOR_SESSION_MESSAGE = (55888, "Chatbot 이 세션 메시지 가능하지 않음")
    NON_RETRYABLE_ERROR_CAUSED_BY_INVALID_MESSAGE = (
        55900,
        "잘못된 메시지 형식으로 인해 발송 실패되었고 재시도 가능하지 않음 (삼성 에러 42001 ~ 42514)",
    )
    REVOCATION_FAILED = (56002, "메시지 회수 실패 (삼성 에러 41002)")
    EXPIRED_BEFORE_SESSION_ESTABLISHMENT = (56007, "RCS 세션 연결 전 만료되어 발송 실패 (삼성 에러 41007)")
    BACKEND_ERROR = (59002, "Backend(삼성 MaaP G/W) 서버 내부 에러")
    BACKEND_TIMEOUT = (59003, "Backend(삼성 MaaP G/W) 서버 타임 아웃 발생")
    ETC_ERROR = (59999, "기타 정의되지 않은 Error (Webhook Cancelled 메시지 등)")
    NOT_FOUND_HANDLER = (51900, "잘못된 요청입니다.")
    SAMSUNG_MAA_P_CONNECT_IF_ERROR = (51901, "삼성 MaaP Gateway NB API 연동 에러")
    SAMSUNG_MAA_P_SERVICE_IF_ERROR = (51902, "삼성 MaaP Registry Chatbot API 연동 에러")
    CAPRI_IF_ERROR = (51903, "Capri 연동 에러")
    WEBHOOK_EXECUTE_IMPOSIBLE_STATUS_FAILURE = (51904, "Webhook 처리 불가 상태 오류가 발생했습니다.")
    WEBHOOK_CDR_LOG_WRITING_FAILURE = (51905, "Webhook 메시지 전송 과금 이력 작성을 실패했습니다.")
    INVALID_WEBHOOK_URL = (51906, "잘못된 Webhook Url 입니다.")
    EXPIRED_WEBHOOK_MESSAGE = (51907, "만료된 메시지 입니다.")
    EXCEED_RETRY_COUNT_TO_SEND_MESSAGE = (51908, "재시도 횟수 초과로 인해 메시지 전송을 실패했습니다.")
    NON_EXISTING_WEBHOOK_MESSAGE = (51909, "Webhook 발송 메시지가 존재하지 않습니다.")
    NON_EXISTING_WEBHOOK_GW_VENDOR = (51910, "Webhook 발송 중계사 정보가 존재하지 않습니다.")
    NO_SUBSCRIPTION = (51911, "계약관계가 없습니다.")
    MAAP_SIMULATER_FAIL = (51912, "삼성 시뮬레이터 연동 오류")
    FAILURE_IN_PREPERATION_FOR_SENDING_WEBHOOK = (51912, "Webhook 발송 준비 수행 중 오류가 발생 했습니다.")
    FAILURE_IN_UPDATING_WEBHOOK_SENDING_RESULT_STATE = (51913, "Webhook 발송 결과 상태 갱신 중 오류가 발생 했습니다.")
    FAILURE_IN_UPDATING_CDR_RESULT_STATE = (51914, "CDR 생성 결과 상태 갱신 중 오류가 발생 했습니다.")
    FAILURE_IN_UPDATING_COMPLETION_RESULT_STATE = (51915, "완료 처리 결과 상태 갱신 중 오류가 발생했습니다.")
    FAILURE_IN_UPDATING_EXPIRATION_RESULT_STATE = (51916, "만료 처리 결과 상태 갱신 중 오류가 발생했습니다.")
    WEBHOOK_MSG_LOG_CREATION_ERROR = (51917, "메시지 이력 생성 작업중 오류가 발생했습니다.")
    WEBHOOK_MSG_LOG_CREATION_FAILURE = (51918, "메시지 이력 생성 작업을 실패했습니다.")
    INVALID_WEBHOOK_RECEIVE_REQUEST_ERROR = (51919, "잘못된 Webhook 요청 오류 ")
    NON_EXISTING_CHATBOT_FOR_REQUEST = (51920, "요청 양뱡향 챗봇에 대한 정보가 존재하지 않습니다")
    NON_USABLE_CHATBOT_STATE_ERROR = (51921, "사용 불가 챗봇 상태 오류입니다")
    NON_EXISTING_GW_VENDOR_FOR_REQUEST = (51922, "요청 양방향 챗봇에 대한 양방향 중계사 정보가 존재하지 않습니다.")
    NON_DEFINITION_MO_MESSAGE_URL_FOR_CHATBOT = (51923, "챗봇 Mo 발송 Url 정보가 미 정의 상태 입니다.")
    WEBHOOK_GATEWAY_EXECUTION_ERROR = (51924, "Webhook 수신 Gateway 수행 오류")
    NOT_ALLOWED_REQUEST_EVENT_ERROR = (51925, "미 허용 Webhook 이벤트 요청 오류")
    WEBHOOK_RECEIVE_EXECUTION_ERROR = (51926, "Webhook 수신 처리 수행 오류")
    WEBHOOK_RECEIVE_ASYNC_EXECUTION_ERROR = (51927, "Webhook 수신 처리 비동기 수행 오류")
    NON_DEFINITION_WEBHOOK_URL_FOR_GW_VENDOR_CID = (51928, "중계사 CID Webhook 발송 Url 정보가 미 정의 상태 입니다.")
    NON_TARGET_GW_VENDOR_FOR_CDR_LOG = (51929, "과금 미 처리 대상 중계사 입니다.")
    NON_RECEIVED_WEBHOOK_COMMAND_ERROR_LOG = (51930, "수행 명령 객체 미 전달 오류입니다.")
    MO_MESSAGE_REGISTRATION_ERROR = (51931, "Mo 메시지 DB 등록 오류가 발생했습니다.")
    MO_MESSAGE_REGISTRATION_FAILUER = (51932, "Mo 메시지 DB 등록 작업을 실패했습니다.")
    AUTO_REPLY_MESSAGE_SENDING_ERROR = (51933, "자동 응답 메시지 발송 수행 오류가 발생했습니다.")
    NON_SERVICE_SUPPORTED_ERROR = (51934, "처리 미 대상 서비스 입니다.")
    SAMSUNG_MAA_P_CORE_FILE_SERVER_CONNECTION_ERROR = (51935, "삼성 MaaP Core 파일 서버 연결 오류가 발생했습니다.")
    MESSAGE_FILE_MESSAGE_EVENT_FILE_DOWNLOAD_ERROR_1 = (51936, "파일 메시지 이벤트의 파일 메시지 다운로드 수행 오류가 발생했습니다.")
    MESSAGE_FILE_MESSAGE_EVENT_FILE_DOWNLOAD_ERROR_2 = (51937, "파일 메시지 이벤트의 파일 메시지 다운로드 수행 오류가 발생했습니다.")
    MESSAGE_FILE_MESSAGE_REGISTRATION_TO_DB_ERROR = (51938, "파일 메시지 이벤트의 파일 정보 DB 등록 오류가 발생했습니다.")
    MESSAGE_FILE_MESSAGE_REGISTRATION_TO_DB_FAILURE = (51939, "파일 메시지 이벤트의 파일 정보 DB 등록 작업을 실패 했습니다.")
    WEBHOOK_SCHEDULER_ASYNC_EXECUTION_ERROR = (51950, "Webhook 스케줄러 비동기 수행 오류.")
    WEBHOOK_SCHEDULER_DB_EXECUTION_ERROR = (51951, "Webhook 스케줄러 DB 수행 오류.")
    WEBHOOK_SCHEDULER_DB_EXECUTION_FAILUER = (51952, "Webhook 스케줄러 DB 수행 실패.")
    WEBHOOK_SCHEDULER_PROCESS_EXECUTION_ERROR = (51953, "Webhook 스케줄러 프로세스 수행 오류.")
    WEBHOOK_SCHEDULER_PROCESS_EXECUTION_FAILUER = (51954, "Webhook 스케줄러 프로세스 수행 실패.")
    WEBHOOK_SCHEDULER_PROCESSOR_EXECUTION_ERROR = (51955, "Webhook 스케줄러 프로세서 수행 오류.")
    WEBHOOK_SCHEDULER_PROCESSOR_EXECUTION_FAILUER = (51956, "Webhook 스케줄러 프로세서 수행 실패.")
    NON_EXISTING_MO_MESSAGE_ERROR = (51957, "Mo 메시지가 존재하지 않습니다.")


# class RcsException(Exception):
#     """
#     Base class for all RCSErrorCode exceptions.
#     """

#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)

#     def __str__(self):
#         return self.message
