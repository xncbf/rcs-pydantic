# RCS-PYDANTIC

<p align="center">
<a href="https://github.com/xncbf/rcs-pydantic/actions?query=workflow%3ATests+event%3Apush+branch%3Amain" target="_blank">
    <img src="https://github.com/xncbf/rcs-pydantic/workflows/Tests/badge.svg?event=push&branch=main" alt="Test">
</a>
<a href="https://codecov.io/gh/xncbf/rcs-pydantic" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/xncbf/rcs-pydantic?color=%2334D058" alt="Coverage">
</a>
<a href="https://pypi.org/project/rcs-pydantic" target="_blank">
    <img src="https://img.shields.io/pypi/v/rcs-pydantic?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/rcs-pydantic" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/rcs-pydantic.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

- [RCS-PYDANTIC](#rcs-pydantic)
  - [Introduce](#introduce)
  - [Installation](#installation)
  - [Dependency](#dependency)
  - [Quick start](#quick-start)
  - [제공되는 항목](#제공되는-항목)
    - [제공되는 데이터 pydantic 모델](#제공되는-데이터-pydantic-모델)
    - [제공되는 데이터 관련 Enum](#제공되는-데이터-관련-enum)
    - [제공되는 에러 코드 Enum](#제공되는-에러-코드-enum)
  - [Features](#features)
    - [RcsMessage](#rcsmessage)
    - [MessageException](#messageexception)
  - [Contribution](#contribution)

## Introduce

한국 통신사 rcs 를 위한 pydantic 모델

[fastapi](https://github.com/tiangolo/fastapi) 또는 [django-ninja](https://github.com/vitalik/django-ninja) 와 함께 사용할 때 유용합니다.

## Installation

```sh
pip install rcs-pydantic
```

## Dependency

- python3.x (3.7 이상)
- pydantic

## Quick start

```py
from rcs_pydantic import MessageInfo, RcsMessage

message_info = {
    "replyId": "B01RDSFR.KcNNLk67ui.FDSAF432153214",
    "eventType":"newUser",
    "displayText": "안녕",
    "userContact":"01012341234",
    "chatbotId":"0212351235",
    "timeStamp": "2020-03-03T04:43:55.867+09"
}

rcs = {
    "message_base_id": "SS000000",
    "service_type": "RCSSMS",
    "agency_id": "<str: agency_id>",
    "body": {
        "title": "타이틀",
        "description": "일반 RCSSMS 테스트 메시지 입니다."
    }
}


rcs_message = RcsMessage(message_info=MessageInfo(**message_info), **rcs)
```

```sh
>>> print(rcs_message.send_info)
common=CommonInfo(
    msgId='4be0072f-0f05-4b3a-adc8-90d7ef309c53',
    userContact='01012341234',
    scheduleType=<ScheduleTypeEnum.IMMEDIATE: 0>,
    msgServiceType=<MessageServiceTypeEnum.RCS: 'rcs'>
)
rcs=RcsInfo(
    chatbotId='0212351235',
    agencyId='<str: agency_id>',
    messagebaseId='SS000000',
    serviceType=<ServiceTypeEnum.SMS: 'RCSSMS'>,
    expiryOption=<ExpiryOptionEnum.AFTER_SETTING_TIMES: 2>,
    header=<HeaderEnum.NOT_ADVERTISE: '0'>,
    copyAllowed=True,
    body=RcsSMSBody(title='타이틀', description='일반 RCSSMS 테스트 메시지 입니다.'),
)
>>>
```

## 제공되는 항목

국내 통신사 RCS 문서에서 제공되는 모든 데이터를 pydandic 모델로써 지원합니다.

### 제공되는 데이터 pydantic 모델

```python
RcsSMSBody
RcsLMSBody
RcsMMSBody
RcsCHATBody
RcsTMPLBody
RcsSMSCarouselBody
RcsLMSCarouselBody
RcsMMSCarouselBody
RcsCHATCarouselBody
LocationInfo
ShowLocationInfo
OpenUrlInfo
CreateCalendarEventInfo
CopyToClipboardInfo
ComposeTextMessageInfo
DialPhoneNumberInfo
UrlActionInfo
LocalBrowserActionInfo
MapActionInfo
CalendarActionInfo
ClipboardActionInfo
ComposeActionInfo
DialActionInfo
PostbackInfo
ActionInfo
SuggestionInfo
ButtonInfo
CommonInfo
RcsInfo
LegacyInfo
StatusInfo
QuerystatusInfo
ErrorInfo
ResponseErrorInfo
ResponseInfo
TextMessageInfo
FileMessageInfo
GeolocationPushMessage
UserLocationInfo
MessageInfo
SendInfo
TokenInfo
```

### 제공되는 데이터 관련 Enum

```python
EventTypeEnum
RCSMessageEnum
MessageEnum
MessageStatusEnum
MnoInfoEnum
BillEnum
MessageServiceTypeEnum
ServiceTypeEnum
LegacyServiceTypeEnum
ScheduleTypeEnum
ExpiryOptionEnum
HeaderEnum
ActionEnum
```

### 제공되는 에러 코드 Enum

```python
ErrorCodeEnum
MaaPErrorCodeEnum
RcsBizCenterErrorCodeEnum
KTErrorCodeEnum
LegacyErrorCodeEnum
```

## Features

### RcsMessage

`RcsMessage` 클래스는 서버로 수신된 `MessageInfo` 메세지 모델을 기반으로 메세지 전송을 위한 `SendInfo` 모델을 만듭니다.

```py
from rcs_pydantic import MessageInfo, RcsMessage

message_info = {
    "replyId": "B01RDSFR.KcNNLk67ui.FDSAF432153214",
    "eventType":"newUser",
    "displayText": "안녕",
    "userContact":"01012341234",
    "chatbotId":"0212351235",
    "timeStamp": "2020-03-03T04:43:55.867+09"
}

rcs = {
    "message_base_id": "SS000000",
    "service_type": "RCSSMS",
    "agency_id": "<str: agency_id>",
    "body": {
        "title": "타이틀",
        "description": "일반 RCSSMS 테스트 메시지 입니다."
    }
}


rcs_message = RcsMessage(message_info=MessageInfo(**message_info), **rcs)
```

### MessageException

`MessageException` 예외 클래스는 제공되는 모든 에러 코드 Enum 을 포함하는 예외 클래스입니다.

다음과 같이 여러 Enum 코드중 한가지를 메세지로 반환합니다.

```python
from rcs_pydantic.errors import ErrorCodeEnum
from rcs_pydantic.exceptions import MessageException
try:
    raise MessageException(ErrorCodeEnum.MISSING_AUTHORIZATION_HEADER.value[0])
except MessageException as e:
    print(f"ERROR MESSAGE: {e}")

ERROR MESSAGE: Valid access token in Authorization header is required for RESTful API calls.
>>>
```

다음과 같이 `has_value` 를 통해 특정 `Enum` 에 포함된 에러인지 확인할 수 있습니다.

```python
>>> from rcs_pydantic.errors import ErrorCodeEnum
... ErrorCodeEnum.has_value(40003)
True
>>> ErrorCodeEnum.has_value(11111)
False
```

## Contribution

이 프로젝트는 기여를 환영합니다!

패치를 제출하기 전에 issue 티켓을 먼저 제출해주세요.

Pull request 는 `main` 브랜치로 머지되며 항상 사용 가능한 상태로 유지해야 합니다.

모든 테스트 코드를 통과한 뒤 리뷰한 후 머지됩니다.
