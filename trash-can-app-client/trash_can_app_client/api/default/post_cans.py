from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.post_cans_response_400 import PostCansResponse400
from ...models.trash_can import TrashCan
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: TrashCan,
) -> Dict[str, Any]:
    url = "{}/cans".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "verify": client.verify_ssl,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PostCansResponse400, TrashCan]]:
    if response.status_code == 201:
        response_201 = TrashCan.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = PostCansResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PostCansResponse400, TrashCan]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: TrashCan,
) -> Response[Union[PostCansResponse400, TrashCan]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: TrashCan,
) -> Optional[Union[PostCansResponse400, TrashCan]]:
    """Add a new TrashCan"""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: TrashCan,
) -> Response[Union[PostCansResponse400, TrashCan]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: TrashCan,
) -> Optional[Union[PostCansResponse400, TrashCan]]:
    """Add a new TrashCan"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
