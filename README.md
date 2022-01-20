<p align="center">
    <em>한국 통신사 rcs 를 위한 pydantic 구조체</em>
</p>
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

- [Installation](#installation)
- [Quick start](#quick-start)
- [Features](#features)
- [Contribution](#contribution)

## Installation

```sh
pip install rcs-pydantic
```

## Quick start

```py
import httpx
from fastapi import Body, FastAPI
from rcs_pydantic import scheme

app = FastAPI()


def get_card(message_info):
    rcs_message = RcsMessage(
        message_info,
        agency_id="ktbizrcs",
        message_base_id="STANDALONE_1",
        service_type="RCSSMS",
        expiry_option=2,
        header="0",
        footer="080-0000-0000",
        cdr_id="ktrcs02",
        copy_allowed=True,
        body=scheme.RcsSMSBody(
            description=textwrap.dedent(
                """\
                안녕하세요.
                메세지입니다.
                """
            )
        ),
        buttons=[
            scheme.ButtonInfo(
                suggestions=[
                    scheme.SuggestionInfo(
                        action=scheme.ActionInfo(
                            urlAction=scheme.UrlActionInfo(
                                openUrl=scheme.OpenUrlInfo(url="https://www.kt.com")
                            ),
                            displayText="kt 홈페이지 들어가기",
                            postback=scheme.PostbackInfo(data="postback_kt"),
                        )
                    )
                ]
            )
        ],
    )
    return rcs_message

@app.post("/corp/{version}/momsg")
async def recieve_message(version: str, message_info: scheme.MessageInfo = Body(...)):
    """
    메세지 받는 웹훅
    """
    body = get_card(message_info)
    response = httpx.post(url=f"{config.RCS_URL}/message", json=body.json())
    return {"status": response.status_code, "content": response.json()}

```

## Features

TODO

## Contribution

TODO
