# DnsRecordInfo

A DNS record within a zone.  Record values are normalized to a flat `content` string. Structured record types use additional top-level fields; the proxy maps these to upstream `data` / `rdata_raw` shapes:  - **A / AAAA**: `content` is the IP address (`data.address`). - **CNAME**: `content` is the target hostname (`data.cname`). - **TXT**: `content` is the text value (`data.txtdata`). - **NS**: `content` is the nameserver hostname (`data.nsdname`). - **MX**: `content` is the mail exchange hostname; `priority` is the MX preference   (`data.exchange`, `data.preference`). - **SRV**: `content` is the target hostname; `priority`, `weight`, and `port` are the   SRV parameters (`data.target`, `data.priority`, `data.weight`, `data.port`).  When upstream returns structured `rdata_raw` without a string `rdata` value, `content` and the type-specific fields are derived from `rdata_raw`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record identifier | [optional] 
**name** | **str** | Record host/name (e.g. @, www, mail) | [optional] 
**type** | **str** | Record type (e.g. A, AAAA, CNAME, MX, TXT, NS, SRV) | [optional] 
**content** | **str** | Primary record value: IP address (A/AAAA), hostname (CNAME/NS/MX/SRV), or text (TXT) | [optional] 
**ttl** | **int** | Time-to-live in seconds | [optional] 
**priority** | **int** | MX preference when type is MX; SRV priority when type is SRV | [optional] 
**weight** | **int** | SRV weight when type is SRV | [optional] 
**port** | **int** | SRV port when type is SRV | [optional] 

## Example

```python
from ha_sdk_python.models.dns_record_info import DnsRecordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordInfo from a JSON string
dns_record_info_instance = DnsRecordInfo.from_json(json)
# print the JSON string representation of the object
print(DnsRecordInfo.to_json())

# convert the object into a dict
dns_record_info_dict = dns_record_info_instance.to_dict()
# create an instance of DnsRecordInfo from a dict
dns_record_info_from_dict = DnsRecordInfo.from_dict(dns_record_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


