"""
HostAfrica API Client
=====================
Hand-written wrapper over the generated API classes.
Provides a pre-configured client with automatic retry on readonly operations.

Usage::

    from hostafrica_sdk_python.client import create_client

    client = create_client(access_token="Bearer <token>")
    result = client.vps.list_vps_services(...)

The set of retryable paths is auto-generated from @readonly annotations in
hostafrica-api.smithy — run ``make sdk-python`` to keep it in sync.
"""

from __future__ import annotations

import inspect
from typing import Optional
from urllib.parse import urlparse

import urllib3

from hostafrica_sdk_python import api as _api_module
from hostafrica_sdk_python.api_client import ApiClient
from hostafrica_sdk_python.configuration import Configuration
from hostafrica_sdk_python.retryable_paths import RETRYABLE_PATHS
from hostafrica_sdk_python import rest


# Status codes that warrant a retry on readonly operations.
_RETRY_STATUSES = frozenset([429, 502, 503, 504])


class _RetryingApiClient(ApiClient):
    """ApiClient that selectively applies urllib3 retry logic on readonly paths."""

    def __init__(self, configuration: Configuration, retries: int, retry_backoff_factor: float) -> None:
        super().__init__(configuration)
        self._retry_policy = urllib3.Retry(
            total=retries,
            backoff_factor=retry_backoff_factor,
            status_forcelist=list(_RETRY_STATUSES),
            allowed_methods=False,  # allow retry on all methods (we gate by path ourselves)
            raise_on_status=False,
        )

    def call_api(self, method, url, header_params=None, body=None, post_params=None, _request_timeout=None):
        path = urlparse(url).path
        if path in RETRYABLE_PATHS:
            original_pool = self.rest_client.pool_manager
            try:
                # Temporarily replace the pool manager with one that has retry enabled.
                # We create it with the same args but add the Retry policy.
                retrying_pool = urllib3.PoolManager(retries=self._retry_policy)
                self.rest_client.pool_manager = retrying_pool
                return super().call_api(
                    method, url,
                    header_params=header_params,
                    body=body,
                    post_params=post_params,
                    _request_timeout=_request_timeout,
                )
            finally:
                self.rest_client.pool_manager = original_pool
        return super().call_api(
            method, url,
            header_params=header_params,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )


def create_client(
    access_token: Optional[str] = None,
    host: Optional[str] = None,
    retries: int = 3,
    retry_backoff_factor: float = 0.5,
    **configuration_kwargs,
):
    """
    Create a fully-configured HostAfrica API client.

    All generated API classes are available as attributes on the returned object.
    Readonly operations (as annotated in the Smithy model) are automatically
    retried up to ``retries`` times on transient HTTP errors (429, 502, 503, 504).

    :param access_token: Bearer token for authentication (e.g. ``"Bearer abc123"``).
    :param host: Override the API base URL. Defaults to ``https://api.hostafrica.com``.
    :param retries: Number of retry attempts for readonly operations. Defaults to 3.
    :param retry_backoff_factor: Multiplier for exponential backoff between retries.
        Sleep time = ``retry_backoff_factor * (2 ** (attempt - 1))`` seconds.
        Defaults to 0.5 (delays: 0.5s, 1s, 2s, …).
    :param configuration_kwargs: Additional kwargs forwarded to ``Configuration``.
    :returns: An object with each generated API class available as an attribute.
    """
    config = Configuration(**configuration_kwargs)
    if access_token is not None:
        config.access_token = access_token
    if host is not None:
        config.host = host

    api_client = _RetryingApiClient(config, retries=retries, retry_backoff_factor=retry_backoff_factor)

    # Dynamically instantiate every API class exported from the api package.
    # This means new API classes added during regeneration are picked up automatically.
    instances = {}
    for name, obj in inspect.getmembers(_api_module, inspect.isclass):
        if name.endswith("Api"):
            attr = _to_snake(name)
            instances[attr] = obj(api_client)

    return type("HostAfricaClient", (), instances)()


def _to_snake(name: str) -> str:
    """Convert CamelCase class name to snake_case attribute (e.g. VPSManagementApi -> vps_management_api)."""
    import re
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    return s.lower()
