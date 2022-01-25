from typing import Optional, Union

from rcs_pydantic import enums

from . import scheme


class RcsMessage:
    STANDALONE_1 = "SCS00000"  # 기본 말풍선
    STANDALONE_2 = "SCL00000"  # 텍스트 카드
    CAROUSEL_MEDIUM_1 = "CCwMhM0200"  # 슬라이드형(Medium, 2장)
    CAROUSEL_MEDIUM_2 = "CCwMhM0300"  # 슬라이드형(Medium, 3장)
    CAROUSEL_MEDIUM_3 = "CCwMhM0400"  # 슬라이드형(Medium, 4장)
    CAROUSEL_MEDIUM_4 = "CCwMhM0500"  # 슬라이드형(Medium, 5장)
    CAROUSEL_MEDIUM_5 = "CCwMhM0600"  # 슬라이드형(Medium, 6장)
    CAROUSEL_SMALL_1 = "CCwShS0200"  # 슬라이드형(Small, 2장)
    CAROUSEL_SMALL_2 = "CCwShS0300"  # 슬라이드형(Small, 3장)
    CAROUSEL_SMALL_3 = "CCwShS0400"  # 슬라이드형(Small, 4장)
    CAROUSEL_SMALL_4 = "CCwShS0500"  # 슬라이드형(Small, 5장)
    CAROUSEL_SMALL_5 = "CCwShS0600"  # 슬라이드형(Small, 6장)
    STANDALONE_MEDIA_TOP = "SCwThT00"  # 세로형(Tall)
    STANDALONE_MEDIA_TOP = "SCwThM00"  # 세로형(Medium)

    def __init__(
        self,
        message_info: scheme.MessageInfo,
        body: Union[
            scheme.RcsSMSBody,
            scheme.RcsLMSBody,
            scheme.RcsMMSBody,
            scheme.RcsCHATBody,
            scheme.RcsTMPLBody,
        ],
        agency_id: Optional[str] = None,
        message_base_id: str = STANDALONE_1,
        service_type: str = "RCSSMS",
        expiry_option: Optional[int] = None,
        header: str = "0",
        footer: Optional[str] = None,
        cdr_id: Optional[str] = None,
        copy_allowed: Optional[bool] = None,
        buttons: Optional[list] = None,
    ):
        self.message_info = message_info
        self.agency_id = agency_id
        self.message_base_id = message_base_id
        self.service_type = service_type
        self.expiry_option = expiry_option
        self.header = header
        self.footer = footer
        self.cdr_id = cdr_id
        self.copy_allowed = copy_allowed
        self.body = body
        self.buttons = buttons
        self.send_info = scheme.SendInfo(
            common=self.make_common_info(message_info), rcs=self.make_rcs_info(message_info)
        )

    def make_common_info(self, message_info: scheme.MessageInfo) -> scheme.CommonInfo:
        return scheme.CommonInfo(
            msgId=message_info.replyId,
            userContact=message_info.userContact,
            scheduleType=0,
            msgServiceType=enums.MessageServiceTypeEnum.RCS,
        )

    def make_rcs_info(self, message_info: scheme.MessageInfo) -> scheme.RcsInfo:
        rcs_info = scheme.RcsInfo(
            chatbotId=message_info.chatbotId,
            messagebaseId=self.message_base_id,
            serviceType=self.service_type,
            header=self.header,
            body=self.body,
        )
        if self.agency_id:
            rcs_info.agencyId = self.agency_id
        if self.expiry_option:
            rcs_info.expiryOption = self.expiry_option
        if self.footer:
            rcs_info.footer = self.footer
        if self.cdr_id:
            rcs_info.cdrId = self.cdr_id
        if self.copy_allowed:
            rcs_info.copyAllowed = self.copy_allowed
        if self.buttons:
            rcs_info.buttons = self.buttons
        return rcs_info

    def send(self):
        self.send_info
