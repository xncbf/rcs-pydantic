import pytest
from faker import Faker

from rcs_pydantic import enums
from rcs_pydantic.errors import ErrorCodeEnum, KTErrorCodeEnum, MaaPErrorCodeEnum, RcsBizCenterErrorCodeEnum
from rcs_pydantic.exceptions import MessageException
from rcs_pydantic.main import RcsMessage

from . import factory

fake = Faker()


def test_rcs_message():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsSMSBodyFactory(),
        buttons=[factory.ButtonInfoFactory()],
        agency_id="abc",
        agency_key="abc",
        brand_key="abc",
        expiry_option=enums.ExpiryOptionEnum.AFTER_SETTING_TIMES,
        header=enums.HeaderEnum.ADVERTISE,
        footer="010-0000-0000",
        cdr_id="abc",
        copy_allowed=True,
        message_group_id="abc",
    )
    assert rcs_message.send_info


def test_rcs_chat_message():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsCHATBodyFactory(),
        buttons=[factory.ButtonInfoFactory()],
        agency_id="abc",
        agency_key="abc",
        brand_key="abc",
        expiry_option=enums.ExpiryOptionEnum.AFTER_SETTING_TIMES,
        header=enums.HeaderEnum.ADVERTISE,
        footer="010-0000-0000",
        cdr_id="abc",
        copy_allowed=True,
        service_type=enums.ServiceTypeEnum.CHAT,
        chips=[factory.SuggestionInfoFactory()],
    )
    assert rcs_message.send_info


def test_rcs_message_with_empty_button():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsSMSBodyFactory(),
        buttons=[{}],
        agency_id="abc",
        agency_key="abc",
        brand_key="abc",
        expiry_option=enums.ExpiryOptionEnum.AFTER_SETTING_TIMES,
        header=enums.HeaderEnum.ADVERTISE,
        footer="010-0000-0000",
        cdr_id="abc",
        copy_allowed=True,
    )
    assert rcs_message.send_info


def test_tuple_enum_has_value():
    assert ErrorCodeEnum.has_value(ErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])


def test_exception_error_message():
    try:
        raise MessageException(ErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])
    except MessageException as e:
        assert e.message == "Valid access token in Authorization header is required for RESTful API calls."
        assert str(e) == "Valid access token in Authorization header is required for RESTful API calls."


def test_error_code_message_exception():
    with pytest.raises(MessageException):
        raise MessageException(ErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])


def test_maap_error_code_message_exception():
    with pytest.raises(MessageException):
        raise MessageException(MaaPErrorCodeEnum.ACTION_BUTTON_PERMISSION_ERROR.value[0])


def test_rcsbiz_error_code_message_exception():
    with pytest.raises(MessageException):
        raise MessageException(RcsBizCenterErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])


def test_kt_error_code_message_exception():
    with pytest.raises(MessageException):
        raise MessageException(KTErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])


def test_unknown_error_code_message_exception():
    with pytest.raises(MessageException):
        raise MessageException(123)


def test_rcs_legacy_message():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsSMSBodyFactory(),
        buttons=[factory.ButtonInfoFactory()],
        agency_id="abc",
        agency_key="abc",
        brand_key="abc",
        expiry_option=enums.ExpiryOptionEnum.AFTER_SETTING_TIMES,
        header=enums.HeaderEnum.ADVERTISE,
        footer="010-0000-0000",
        cdr_id="abc",
        copy_allowed=True,
        legacy=factory.LegacyInfoFactory(),
    )
    assert rcs_message.send_info
