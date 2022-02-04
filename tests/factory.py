from datetime import datetime
from typing import List

import factory
from faker import Faker

from rcs_pydantic import enums, errors, scheme

fake = Faker()


class RcsSMSBodyFactory(factory.Factory):
    class Meta:
        model = scheme.RcsSMSBody

    title: str = factory.Faker("name")
    description: str = factory.Faker("name")


class RcsLMSBodyFactory(factory.Factory):
    class Meta:
        model = scheme.RcsLMSBody

    title: str = factory.Faker("name")
    description: str = factory.Faker("name")


class RcsMMSBodyFactory(factory.Factory):
    class Meta:
        model = scheme.RcsMMSBody

    title: str = factory.Faker("name")
    description: str = factory.Faker("name")


class RcsCHATBodyFactory(factory.Factory):
    class Meta:
        model = scheme.RcsCHATBody

    title: str = factory.Faker("name")
    description: str = factory.Faker("name")


class RcsTMPLBodyFactory(factory.Factory):
    class Meta:
        model = scheme.RcsTMPLBody


class LocationInfoFactory(factory.Factory):
    class Meta:
        model = scheme.LocationInfo

    latitude: float = factory.Faker("latitude")
    longitude: float = factory.Faker("longitude")
    label: str = factory.Faker("name")
    # query: str = factory.Faker("name")


class ShowLocationInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ShowLocationInfo

    fallbackUrl: str = factory.Faker("url")
    location: scheme.LocationInfo = factory.SubFactory(LocationInfoFactory)


class OpenUrlInfoFactory(factory.Factory):
    class Meta:
        model = scheme.OpenUrlInfo

    url: str = factory.Faker("url")


class CreateCalendarEventInfoFactory(factory.Factory):
    class Meta:
        model = scheme.CreateCalendarEventInfo

    title: str = factory.Faker("name")
    description: str = factory.Faker("name")
    startTime: str = factory.Faker("iso8601")
    endTime: str = factory.Faker("iso8601")


class CopyToClipboardInfoFactory(factory.Factory):
    class Meta:
        model = scheme.CopyToClipboardInfo

    text: str = factory.Faker("text")


class ComposeTextMessageInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ComposeTextMessageInfo

    phoneNumber: str = factory.Faker("phone_number")
    text: str = factory.Faker("text")


class DialPhoneNumberInfoFactory(factory.Factory):
    class Meta:
        model = scheme.DialPhoneNumberInfo

    phoneNumber: str = factory.Faker("phone_number")


class UrlActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.UrlActionInfo

    openUrl: scheme.OpenUrlInfo = factory.SubFactory(OpenUrlInfoFactory)


class LocalBrowserActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.LocalBrowserActionInfo

    openUrl: scheme.OpenUrlInfo = factory.SubFactory(OpenUrlInfoFactory)


class MapActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.MapActionInfo

    showLocation: scheme.ShowLocationInfo = factory.SubFactory(ShowLocationInfoFactory)


class CalendarActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.CalendarActionInfo

    createCalendarEvent: scheme.CreateCalendarEventInfo = factory.SubFactory(CreateCalendarEventInfoFactory)


class ClipboardActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ClipboardActionInfo

    copyToClipboard: scheme.CopyToClipboardInfo = factory.SubFactory(CopyToClipboardInfoFactory)


class ComposeActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ComposeActionInfo

    composeTextMessage: scheme.ComposeTextMessageInfo = factory.SubFactory(ComposeTextMessageInfoFactory)


class DialerActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.DialerActionInfo

    dialPhoneNumber: scheme.DialPhoneNumberInfo = factory.SubFactory(DialPhoneNumberInfoFactory)


class PostbackInfoFactory(factory.Factory):
    class Meta:
        model = scheme.PostbackInfo

    data: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=200)[:2048])


class ActionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ActionInfo

    urlAction: scheme.UrlActionInfo = factory.SubFactory(UrlActionInfoFactory)
    displayText: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=20)[:200])
    postback: scheme.PostbackInfo = factory.SubFactory(PostbackInfoFactory)


class SuggestionInfoFactory(factory.Factory):
    class Meta:
        model = scheme.SuggestionInfo

    action: scheme.ActionInfo = factory.SubFactory(ActionInfoFactory)


class ButtonInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ButtonInfo

    suggestions: List[scheme.SuggestionInfo] = factory.List(
        [factory.SubFactory(SuggestionInfoFactory) for _ in range(2)]
    )


class CommonInfoFactory(factory.Factory):
    class Meta:
        model = scheme.CommonInfo

    msgId: str = factory.Faker("uuid4")
    userContact: str = factory.Faker("phone_number")
    scheduleType: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.ScheduleTypeEnum))
    msgGroupId: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=10)[:20])
    msgServiceType: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.MessageServiceTypeEnum))


class RcsInfoFactory(factory.Factory):
    class Meta:
        model = scheme.RcsInfo

    chatbotId: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=10)[:40])
    agencyId: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=10)[:20])
    messagebaseId: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.MessageEnum))
    serviceType: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.ServiceTypeEnum))
    expiryOption: int = 2
    header: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.HeaderEnum))
    body: scheme.RcsSMSBody = factory.SubFactory(RcsSMSBodyFactory)


class LegacyInfoFactory(factory.Factory):
    class Meta:
        model = scheme.LegacyInfo

    serviceType: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.LegacyServiceTypeEnum))
    callback: str = factory.Faker("name")
    subject: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=20)[:50])
    msg: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=200)[:4000])
    contentCount: int = 0


class StatusInfoFactory(factory.Factory):
    class Meta:
        model = scheme.StatusInfo

    rcsId: str = factory.Faker("name")
    msgId: str = factory.Faker("name")
    userContact: str = factory.Faker("phone_number")
    status: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.MessageStatusEnum))
    serviceType: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.ServiceTypeEnum))
    mnoInfo: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.MnoInfoEnum))

    @factory.lazy_attribute
    def sentTime(self) -> str:
        t = datetime.now()
        s: str = t.strftime("%Y-%m-%dT%H:%M:%S.%f")
        s = s[:-3]
        return s + "+09"

    @factory.lazy_attribute
    def timestamp(self) -> str:
        t = datetime.now()
        s: str = t.strftime("%Y-%m-%dT%H:%M:%S.%f")
        s = s[:-3]
        return s + "+09"


class ErrorInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ErrorInfo

    code: str = factory.LazyAttribute(
        lambda n: fake.random_element(elements=[x.value[0] for x in errors.ErrorCodeEnum])
    )
    message: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=20)[:50])


class ResponseErrorInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ResponseErrorInfo

    status: str = "403"
    error: scheme.ErrorInfo = factory.SubFactory(ErrorInfoFactory)


class TokenInfoFactory(factory.Factory):
    class Meta:
        model = scheme.TokenInfo

    rcsId: str = factory.Faker("uuid4")
    rcsSecret: str = factory.Faker("password")
    grantType: str = "clientCredentials"


class ResponseInfoFactory(factory.Factory):
    class Meta:
        model = scheme.ResponseInfo

    status: str = "200"
    data: dict = factory.SubFactory(TokenInfoFactory)


class MessageInfoFactory(factory.Factory):
    class Meta:
        model = scheme.MessageInfo

    replyId: str = factory.Faker("uuid4")
    eventType: str = factory.LazyAttribute(lambda n: fake.random_element(elements=enums.EventTypeEnum))
    userContact: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=10)[:40])
    chatbotId: str = factory.LazyAttribute(lambda n: fake.sentence(nb_words=10)[:40])

    @factory.lazy_attribute
    def timeStamp(self) -> str:
        t = datetime.now()
        s: str = t.strftime("%Y-%m-%dT%H:%M:%S.%f")
        s = s[:-3]
        return s + "+09"


class SendInfoFactory(factory.Factory):
    class Meta:
        model = scheme.SendInfo

    common: scheme.CommonInfo = factory.SubFactory(CommonInfoFactory)
    rcs: scheme.RcsInfo = factory.SubFactory(RcsInfoFactory)
