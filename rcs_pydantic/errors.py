from enum import Enum


class LegacyErrorCodeEnum(str, Enum):
    pass


class ErrorCodeEnum(Enum):
    """
    Enum of error codes.
    """

    # General errors

    MISSING_AUTHORIZATION_HEADER = 40001
    MISSING_TOKEN = 40002
    INVALID_TOKEN = 40003
    TOKEN_HAS_EXPIRED = 40004
    MALFORMED_TOKEN_PAYLOAD = 40005
    INVALID_CLIENT_ID = 40006
    INSUFFICIENT_SCOPE = 40007
    INTERNAL_SERVER_ERROR = 41000
    RCS_REQUEST_TIMEOUT = 41001
    REVOCATION_FAILED = 41002
    THROTTLED_BY_MESSAGE_RATE = 41003
    RCS_SERVER_BUSY = 41004
    RCS_SERVER_TEMPORARILY_UNAVAILABLE = 41005
    SESSION_DOES_NOT_EXIST = 41006
    EXPIRED_BEFORE_SESSION_ESTABLISHMENT = 41007
    SESSION_ALREADY_EXPIRED = 41008
    IMDN_RECEIVED_EVEN_ALREADY_REVOKED = 41010
    SUBSCRIBE_TIMEOUT = 41100
    USER_NOT_FOUND = 41101
    USER_NOT_FOUND_ = 41200
    MESSAGE_NOT_ACCEPTABLE = 41201
    USER_IS_NOT_CAPABLE_FOR_TEXT = 41210
    USER_IS_NOT_CAPABLE_FOR_FT = 41211
    USER_IS_NOT_CAPABLE_FOR_RICHCARD = 41212
    USER_IS_NOT_CAPABLE_FOR_XBOTMESSAGE_1_0 = 41220
    USER_IS_NOT_CAPABLE_FOR_XBOTMESSAGE_1_1 = 41221
    USER_IS_NOT_CAPABLE_FOR_XBOTMESSAGE_1_2 = 41222
    USER_IS_NOT_CAPABLE_FOR_OPENRICHARD_1_0 = 41230
    USER_IS_NOT_CAPABLE_FOR_OPENRICHARD_1_1 = 41231
    USER_IS_NOT_CAPABLE_FOR_OPENRICHARD_1_2 = 41232
    USER_IS_NOT_CAPABLE_FOR_GEOLOCATION_PUSH_REQUEST = 41240
    FAILED_TO_GET_MESSAGE_CONTENT_TYPE = 41250
    INVALID_STATE = 42001
    INVALID_MESSAGE = 42002
    INVALID_DATE_TIME_FORMAT = 42003
    MISSING_CONTACT = 42004
    INVALID_CONTACT = 42005
    EMULATOR_ACCESS_ONLY = 42006
    CONTACT_NOT_IN_WHITELIST = 42007
    MISSING_MESSAGE_CONTENT = 42008
    INVALID_MESSAGE_CONTENT = 42009
    AMBIGUOUS_MESSAGE = 42010
    INVALID_MESSAGE_STATUS = 42011
    INVALID_ISTYPING_STATUS = 42012
    INVALID_TRAFFIC_TYPE = 42013
    INVALID_SUGGESTED_CHIPLIST_ASSOCIATION = 42014
    EMPTY_TEXT_MESSAGE = 42015
    MISSING_RICHCARD = 42031
    AMBIGUOUS_RICHCARD = 42032
    TOO_MANY_RICHCARDS = 42033
    MISSING_RICHCARD_LAYOUT = 42034
    MISSING_RICHCARD_CONTENT = 42035
    INVALID_CARDORIENTATION = 42036
    MISSING_IMAGE_ALIGNMENT = 42037
    INVALID_IMAGE_ALIGNMENT = 42038
    REDUNDANT_IMAGE_ALIGNMENT = 42039
    INVALID_RICHCARD_CAROUSEL_CARDWIDTH = 42040
    MISMATCHED_MEDIA_HEIGHT = 42041
    INVALID_RICHCARD_CONTENT = 42042
    INVALID_SUGGESTIONS = 42043
    TOO_MANY_SUGGESTIONS = 42044
    INVALID_SUGGESTION = 42045
    AMBIGUOUS_SUGGESTION = 42046
    AMBIGUOUS_SUGGESTED_ACTION = 42047
    TOO_MANY_SUGGESTIONS_IN_RICHCARD_MAX_4 = 42048
    TOO_MANY_SUGGESTION_DATA_MAX_2048 = 42049
    INVALID_ACTION = 42050
    INVALID_LOCATION_A = 42051  # Either latitude and longitude or query are required in location.
    AMBIGUOUS_LOCATION = 42052
    INVALID_MAPACTION = 42053
    AMBIGUOUS_MAPACTION = 42054
    INVALID_DIALERACTION = 42055
    AMBIGUOUS_DIALERACTION = 42056
    INVALID_COMPOSEACTION = 42057
    AMBIGUOUS_COMPOSEACTION = 42058
    INVALID_SETTINGSACTION = 42059
    AMBIGUOUS_SETTINGSACTION = 42060
    INVALID_CLIPBOARDACTION = 42061
    MISSING_LOCALBROWSERACTION = 42062
    INVALID_SHAREACTION = 42063
    AMBIGUOUS_SHAREACTION = 42064
    INVALID_THUMBNAIL = 42100
    MISSING_FILEURL = 42101
    MISSING_AUDIO_FILEURL = 42102
    MISSING_POS = 42103
    MISSING_MEDIA_INFORMATION_A = 42104
    MISSING_MEDIA_INFORMATION_B = 42105
    MISSING_MEDIA_INFORMATION_C = 42106
    MISSING_MEDIA_INFORMATION_D = 42107
    INVALID_LOCATION_B = 42201  # geolocationPushMessage should not contain label length > 200 Characters.
    INVALID_MEDIA_CONTENT_DESCRIPTION = 42202
    INVALID_MEDIA_TITLE = 42203
    INVALID_MEDIA_DESCRIPTION = 42204
    TOO_MANY_CONTENTS_IN_RICHARD_CAROUSEL = 42205
    INVALID_MEDIA_FILE_SIZE = 42206
    INVALID_EXPIRY_TIME_FORMAT = 42207
    INVALID_EXPIRY_TIME = 42208
    AMBIGUOUS_OPENRICHCARD = 42301
    MISSING_OPENRICHCARD = 42302
    MISSING_OPENRICHCARD_LAYOUT_WIDGET = 42303
    MISSING_OPENRICHCARD_VIEW_CONTENT = 42304
    MISSING_OPENRICHCARD_LINEARLAYOUT_CONTENT = 42305
    MISSING_OPENRICHCARD_TEXTVIEW_CONTENT = 42306
    INVALID_CONTENTS_IN_OPENRICHCARD_TEXTVIEW = 42307
    INVALID_TEXT_LENGTH_IN_OPENRICHCARD_TEXTVIEW = 42308
    MISSING_OPENRICHCARD_IMAGEVIEW_CONTENT = 42309
    TOO_SMALL_MEDIA_IN_OPENRICHCARD_IMAGEVIEW = 42310
    INVALID_OPENRICHCARD_IMAGEVIEW_SCALETYPE = 42311
    MISSING_OPENRICHCARD_WIDTH_OR_HEIGHT = 42312
    INVALID_OPENRICHCARD_WIDTH_OR_HEIGHT = 42313
    INVALID_OPENRICHCARD_COMMON_CONTENTS = 42314
    TOO_MANY_CHILD_IN_OPEN_RICH_CARD = 42315
    INVALID_FILE_TYPE = 42401
    DOWNLOAD_FAILURE = 42402
    MISSING_CONTACT_A = 42501
    MISSING_CONTENT_B = 42502
    MISSING_TITLE = 42503
    MISSING_DESCRIPTION = 42504
    MISSING_IMAGE_URL = 42505
    MISSING_IMAGE_TYPE = 42506
    MISSING_BUTTON_LINK = 42507
    MISSING_BUTTON_TEXT = 42508
    INVALID_TITLE = 42509
    INVALID_DESCRIPTION = 42510
    INVALID_IMAGE_URL_ADDRESS = 42511
    INVALID_BUTTON_URL_ADDRESS = 42512
    INVALID_BUTTON_TEXT = 42513
    DUPLICATED_MESSAGE_ID = 42514
    TOO_MANY_REQUEST = 42601


# class RcsException(Exception):
#     """
#     Base class for all RCSErrorCode exceptions.
#     """

#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)

#     def __str__(self):
#         return self.message
