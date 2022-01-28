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
  - [Quick start](#quick-start)
  - [Features](#features)
  - [Contribution](#contribution)

## Introduce

한국 통신사 rcs 를 위한 pydantic 구조체

## Installation

```sh
pip install rcs-pydantic
```

## Quick start

```py
from rcs_pydantic import MessageInfo, RcsMessage

message_info = {
    "replyId": "B01RDSFR.KcNNLk67ui.FDSAF432153214",
    "eventType":"message",
    "messageBody": {"textMessage": "안녕하세요?"},
    "userContact":"01012341234",
    "chatbotId":"0212351235",
    "timestamp": "2020-03-03T04:43:55.867+09"
}

rcs = {
    "message_base_id": "SCS00000",
    "service_type": "RCSSMS",
    "header": "0",
    "cdr_id": "KT_rcsid",
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
    msgId='B01RDSFR.KcNNLk67ui.FDSAF432153214',
    userContact='01012341234',
    scheduleType=<ScheduleTypeEnum.IMMEDIATE: 0>,
    msgGroupId=None,
    msgServiceType=<MessageServiceTypeEnum.RCS: 'rcs'>
)
rcs=RcsInfo(
    chatbotId='0212351235',
    agencyId='ktbizrcs',
    messagebaseId='SCS00000',
    serviceType=<ServiceTypeEnum.SMS: 'RCSSMS'>,
    expiryOption=<ExpiryOptionEnum.AFTER_SETTING_TIMES: 2>,
    header=<HeaderEnum.NOT_ADVERTISE: '0'>,
    footer=None,
    cdrId='KT_rcsid',
    copyAllowed=True,
    body=RcsSMSBody(title='타이틀', description='일반 RCSSMS 테스트 메시지 입니다.'),
    buttons=None,
    chipLists=None,
    replyId=None
)
>>>
```

## Features

TODO

## Contribution

TODO
