from faker import Faker

from rcs_pydantic.errors import ErrorCodeEnum
from rcs_pydantic.main import RcsMessage

from . import factory

fake = Faker()


def test_rcs_message():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsSMSBodyFactory(),
        footer=None,
        buttons=[factory.ButtonInfoFactory()],
    )
    rcs_message.send()


def test_tuple_enum_has_value():
    assert ErrorCodeEnum.has_value(ErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])
