import pytest
from faker import Faker

from rcs_pydantic import enums

from . import factory

fake = Faker()


def test_rcs_sms_body_factory():
    factory.RcsSMSBodyFactory()


def test_rcs_lms_body_factory():
    factory.RcsLMSBodyFactory()


def test_rcs_mms_body_factory():
    factory.RcsMMSBodyFactory()


def test_rcs_chat_body_factory():
    factory.RcsCHATBodyFactory()


def test_rcs_tmpl_body_factory():
    factory.RcsTMPLBodyFactory()


def test_location_info_factory():
    factory.LocationInfoFactory()


def test_show_location_info_factory():
    factory.ShowLocationInfoFactory()


def test_open_url_info_factory():
    factory.OpenUrlInfoFactory()


def test_create_calendar_event_info_factory():
    factory.CreateCalendarEventInfoFactory()


def test_copy_to_clipboard_info_factory():
    factory.CopyToClipboardInfoFactory()


def test_compose_text_message_info_factory():
    factory.ComposeTextMessageInfoFactory()


def test_dial_phone_number_info_factory():
    factory.DialPhoneNumberInfoFactory()


def test_url_action_info_factory():
    factory.UrlActionInfoFactory()


def test_local_browser_action_info_factory():
    factory.LocalBrowserActionInfoFactory()


def test_map_action_info_factory():
    factory.MapActionInfoFactory()


def test_calendar_action_info_factory():
    factory.CalendarActionInfoFactory()


def test_clipboard_action_info_factory():
    factory.ClipboardActionInfoFactory()


def test_compose_action_info_factory():
    factory.ComposeActionInfoFactory()


def test_dialer_action_info_factory():
    factory.DialerActionInfoFactory()


def test_postback_info_factory():
    factory.PostbackInfoFactory()


def test_action_info_factory():
    factory.ActionInfoFactory()


def test_suggestion_info_factory():
    factory.SuggestionInfoFactory()


def test_button_info_factory():
    factory.ButtonInfoFactory()


def test_common_info_factory():
    factory.CommonInfoFactory()


def test_rcs_info_factory():
    with pytest.raises(ValueError):
        factory.RcsInfoFactory(header=enums.HeaderEnum.NOT_ADVERTISE, footer="080-000-0000")
    with pytest.raises(ValueError):
        factory.RcsInfoFactory(header=enums.HeaderEnum.ADVERTISE, footer=None)

    factory.RcsInfoFactory(header=enums.HeaderEnum.ADVERTISE, footer="080-000-0000")


def test_legacy_info_factory():
    factory.LegacyInfoFactory()


def test_status_info_factory():
    factory.StatusInfoFactory()


def test_error_info_factory():
    factory.ErrorInfoFactory()


def test_response_error_info_factory():
    factory.ResponseErrorInfoFactory()


def test_token_info_factory():
    factory.TokenInfoFactory()


def test_response_info_factory():
    factory.ResponseInfoFactory()


def test_message_info_factory():
    with pytest.raises(ValueError):
        factory.MessageInfoFactory(eventType=enums.EventTypeEnum.RESPONSE, messageBody={"textMessage": "안녕하세요?"})

    factory.MessageInfoFactory(eventType=enums.EventTypeEnum.MESSAGE, messageBody={"textMessage": "안녕하세요?"})
    factory.MessageInfoFactory(eventType=enums.EventTypeEnum.MESSAGE, messageBody=None)


def test_send_info_factory():
    factory.SendInfoFactory()


def test_file_info_factory():
    factory.FileInfoFactory()


def test_file_regist_info_factory():
    factory.FileRegistInfoFactory()
