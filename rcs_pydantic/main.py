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
            scheme.RcsTMPLBody,
        ],
        agency_id: Optional[str] = None,
        message_base_id: Union[enums.MessageEnum, enums.RCSMessageEnum] = enums.MessageEnum.STANDALONE_1,
        service_type: enums.ServiceTypeEnum = enums.ServiceTypeEnum.SMS,
        expiry_option: Optional[enums.ExpiryOptionEnum] = None,
        header: enums.HeaderEnum = enums.HeaderEnum.NOT_ADVERTISE,
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
            msgId=uuid.uuid4(),
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
