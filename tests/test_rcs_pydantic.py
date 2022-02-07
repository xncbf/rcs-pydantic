import pytest
from faker import Faker

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
        expiry_option=2,
        header="1",
        footer="010-0000-0000",
        cdr_id="abc",
        copy_allowed=True,
    )
    rcs_message.send()


def test_tuple_enum_has_value():
    assert ErrorCodeEnum.has_value(ErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])


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
