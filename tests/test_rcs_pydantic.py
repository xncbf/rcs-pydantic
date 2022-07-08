import pytest
from faker import Faker
from pydantic import BaseModel

from rcs_pydantic import enums
from rcs_pydantic.errors import ErrorCodeEnum, KTErrorCodeEnum, MaaPErrorCodeEnum, RcsBizCenterErrorCodeEnum
from rcs_pydantic.exceptions import MessageException
from rcs_pydantic.main import RcsMessage
from rcs_pydantic.scheme import EmptyDict

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


def test_rcs_chat_message():
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
        service_type=enums.ServiceTypeEnum.CHAT,
    )
    rcs_message.send()


def test_rcs_message_with_empty_button():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsSMSBodyFactory(),
        buttons=[{}],
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


def test_empty_dict():
    class C(BaseModel):
        item: EmptyDict

    C(item={})

    with pytest.raises(ValueError):
        C(item=None)

    with pytest.raises(ValueError):
        C(item=[])

    with pytest.raises(ValueError):
        C(item={"a": 1})
