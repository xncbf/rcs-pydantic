from faker import Faker

from rcs_pydantic import __version__

fake = Faker()


def test_version():
    assert __version__ == "0.1.7"


# def test_rcs_message():
#     body = RcsSMSBody(title=fake.name(max_length=30), description=fake.text())
#     RcsMessage(body=body)
