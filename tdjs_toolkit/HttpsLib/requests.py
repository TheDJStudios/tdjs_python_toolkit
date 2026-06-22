import json
import urllib.request
import urllib.parse
import urllib.error


class Response:
    def __init__(self, status_code, headers, content, url):
        self.status_code = status_code
        self.headers = dict(headers)
        self.content = content
        self.url = url

    @property
    def text(self):
        return self.content.decode("utf-8", errors="replace")

    def json(self):
        return json.loads(self.text)

    @property
    def ok(self):
        return 200 <= self.status_code < 300

    def raise_for_status(self):
        if not self.ok:
            raise HTTPError(self.status_code, self.text, self.url)


class HTTPError(Exception):
    def __init__(self, status_code, body, url):
        super().__init__(f"HTTP {status_code} for {url}: {body}")
        self.status_code = status_code
        self.body = body
        self.url = url


def request(method, url, params=None, headers=None, data=None, json_data=None, timeout=30):
    headers = dict(headers or {})

    if params:
        query = urllib.parse.urlencode(params)
        separator = "&" if "?" in url else "?"
        url = f"{url}{separator}{query}"

    body = None

    if json_data is not None:
        body = json.dumps(json_data).encode("utf-8")
        headers.setdefault("Content-Type", "application/json")
    elif data is not None:
        if isinstance(data, dict):
            body = urllib.parse.urlencode(data).encode("utf-8")
            headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        elif isinstance(data, str):
            body = data.encode("utf-8")
        else:
            body = data

    headers.setdefault("User-Agent", "toolkit-http/1.0")

    req = urllib.request.Request(
        url=url,
        data=body,
        headers=headers,
        method=method.upper()
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            content = res.read()
            return Response(
                status_code=res.status,
                headers=res.headers,
                content=content,
                url=res.url
            )
    except urllib.error.HTTPError as e:
        content = e.read()
        return Response(
            status_code=e.code,
            headers=e.headers,
            content=content,
            url=url
        )


def get(url, params=None, headers=None, timeout=30):
    return request("GET", url, params=params, headers=headers, timeout=timeout)


def post(url, params=None, headers=None, data=None, json=None, timeout=30):
    return request("POST", url, params=params, headers=headers, data=data, json_data=json, timeout=timeout)


def put(url, params=None, headers=None, data=None, json=None, timeout=30):
    return request("PUT", url, params=params, headers=headers, data=data, json_data=json, timeout=timeout)


def patch(url, params=None, headers=None, data=None, json=None, timeout=30):
    return request("PATCH", url, params=params, headers=headers, data=data, json_data=json, timeout=timeout)


def delete(url, params=None, headers=None, timeout=30):
    return request("DELETE", url, params=params, headers=headers, timeout=timeout)