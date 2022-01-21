from faker import Faker

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
