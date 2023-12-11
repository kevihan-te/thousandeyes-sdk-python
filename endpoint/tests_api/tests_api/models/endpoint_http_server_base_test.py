# coding: utf-8

"""
    Endpoint Tests API

     ## Overview Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from tests_api.models.endpoint_test_auth_type import EndpointTestAuthType
from tests_api.models.endpoint_test_protocol import EndpointTestProtocol
from tests_api.models.test_probe_mode import TestProbeMode
from tests_api.models.test_ssl_version_id import TestSslVersionId
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EndpointHttpServerBaseTest(BaseModel):
    """
    EndpointHttpServerBaseTest
    """ # noqa: E501
    auth_type: Optional[EndpointTestAuthType] = Field(default=None, alias="authType")
    has_path_trace_in_session: Optional[StrictBool] = Field(default=None, description="Enables \"in session\" path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session.", alias="hasPathTraceInSession")
    http_time_limit: Optional[StrictInt] = Field(default=None, description="Maximum amount of time in milliseconds the agents wait before a request times out.", alias="httpTimeLimit")
    protocol: Optional[EndpointTestProtocol] = None
    url: Optional[StrictStr] = Field(default=None, description="Test target URL. Optionally, you can specify a protocol (http or https). If no protocol is provided, the default `https` protocol is used.")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    tcp_probe_mode: Optional[TestProbeMode] = Field(default=None, alias="tcpProbeMode")
    verify_certificate: Optional[StrictBool] = Field(default=None, description="Flag indicating if a certificate should be verified.", alias="verifyCertificate")
    __properties: ClassVar[List[str]] = ["authType", "hasPathTraceInSession", "httpTimeLimit", "protocol", "url", "username", "sslVersionId", "tcpProbeMode", "verifyCertificate"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EndpointHttpServerBaseTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EndpointHttpServerBaseTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authType": obj.get("authType"),
            "hasPathTraceInSession": obj.get("hasPathTraceInSession"),
            "httpTimeLimit": obj.get("httpTimeLimit"),
            "protocol": obj.get("protocol"),
            "url": obj.get("url"),
            "username": obj.get("username"),
            "sslVersionId": obj.get("sslVersionId"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "verifyCertificate": obj.get("verifyCertificate")
        })
        return _obj


