from faker import Faker

from rcs_pydantic import __version__
from rcs_pydantic.main import RcsMessage

from . import factory

fake = Faker()


def test_version():
    assert __version__ == "0.1.7"


def test_rcs_message():
    rcs_message = RcsMessage(
        factory.MessageInfoFactory(),
        body=factory.RcsSMSBodyFactory(),
        footer=None,
        buttons=[factory.ButtonInfoFactory()],
    )
    rcs_message.send()
