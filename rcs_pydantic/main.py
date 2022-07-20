import uuid
from typing import Optional, Union

from rcs_pydantic import enums

from . import scheme


class RcsMessage:
    def __init__(
        self,
        message_info: scheme.MessageInfo,
        body: Union[
            scheme.RcsSMSBody,
            scheme.RcsLMSBody,
            scheme.RcsMMSBody,
            scheme.RcsCHATBody,
            scheme.RcsSMSCarouselBody,
            scheme.RcsLMSCarouselBody,
            scheme.RcsMMSCarouselBody,
            scheme.RcsCHATCarouselBody,
            dict,
        ],
        agency_id: Optional[str] = None,
        message_base_id: Union[enums.MessageEnum, enums.RCSMessageEnum] = enums.MessageEnum.SMS,
        service_type: enums.ServiceTypeEnum = enums.ServiceTypeEnum.SMS,
        expiry_option: Optional[enums.ExpiryOptionEnum] = None,
        header: enums.HeaderEnum = enums.HeaderEnum.NOT_ADVERTISE,
        footer: Optional[str] = None,
        cdr_id: Optional[str] = None,
        copy_allowed: Optional[bool] = None,
        buttons: Optional[list] = None,
        chips: Optional[list] = None,
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
        self.chips = chips
        self.send_info = scheme.SendInfo(
            common=scheme.CommonInfo(**self.make_common_info(message_info)),
            rcs=scheme.RcsInfo(**self.make_rcs_info(message_info)),
        )

    def make_common_info(self, message_info: scheme.MessageInfo) -> dict:
        return scheme.CommonInfo(
            msgId=str(uuid.uuid4()),
            userContact=message_info.userContact,
            scheduleType=0,
            msgServiceType=enums.MessageServiceTypeEnum.RCS,
        ).dict(exclude_unset=True)

    def make_rcs_info(self, message_info: scheme.MessageInfo) -> dict:
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
        if self.service_type == enums.ServiceTypeEnum.CHAT:
            rcs_info.expiryOption = enums.ExpiryOptionEnum.AFTER_SETTING_TIMES
        if self.footer:
            rcs_info.footer = self.footer
        if self.cdr_id:
            rcs_info.cdrId = self.cdr_id
        if self.copy_allowed:
            rcs_info.copyAllowed = self.copy_allowed
        if self.buttons:
            rcs_info.buttons = self.buttons
        if self.chips:
            rcs_info.chipList = self.chips
        if message_info.replyId:
            rcs_info.replyId = message_info.replyId
        return rcs_info.dict(exclude_unset=True)

    def send(self):
        self.send_info
