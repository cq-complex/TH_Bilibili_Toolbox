"""Decode Bilibili API envelopes and distinguish HTTP and business errors."""


class APIError(ValueError):
    pass


def api_code(payload):
    code = payload.get("code", payload.get("status_code"))
    if type(code) is not int:
        raise APIError("接口响应缺少有效返回码 / Invalid API response code")
    return code


def api_message(payload):
    return str(payload.get("message") or payload.get("msg") or "Bilibili API")


def read_api_response(response):
    response.raise_for_status()
    try:
        payload = response.json()
    except ValueError as error:
        raise APIError("接口未返回 JSON / API did not return JSON") from error
    if not isinstance(payload, dict):
        raise APIError("接口返回格式异常 / Invalid API response")
    api_code(payload)
    return payload


def require_api_success(payload):
    code = api_code(payload)
    if code != 0:
        raise APIError(f"{api_message(payload)} ({code})")
    return payload


def api_data(response):
    data = require_api_success(read_api_response(response)).get("data")
    if not isinstance(data, dict):
        raise APIError("接口未返回数据对象 / API response has no data object")
    return data
