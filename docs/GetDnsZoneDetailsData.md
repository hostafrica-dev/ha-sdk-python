# GetDnsZoneDetailsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**domain_id** | **str** | Domain service id | [optional] 
**zone_id** | **str** | DNS zone identifier | [optional] 
**zone_exists** | **bool** | True when a DNS zone exists for this domain | [optional] 
**management_available** | **bool** | True when DNS management is available for this domain | [optional] 
**domain_nameservers** | **List[str]** | Configured domain nameservers | [optional] 
**ns_changing** | **str** | Nameserver change state (e.g. own, pending) | [optional] 
**package_settings** | **object** | Package quotas and allowed record types from upstream | [optional] 
**records** | [**List[DnsRecordInfo]**](DnsRecordInfo.md) | DNS records in the zone | [optional] 

## Example

```python
from ha_sdk_python.models.get_dns_zone_details_data import GetDnsZoneDetailsData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDnsZoneDetailsData from a JSON string
get_dns_zone_details_data_instance = GetDnsZoneDetailsData.from_json(json)
# print the JSON string representation of the object
print(GetDnsZoneDetailsData.to_json())

# convert the object into a dict
get_dns_zone_details_data_dict = get_dns_zone_details_data_instance.to_dict()
# create an instance of GetDnsZoneDetailsData from a dict
get_dns_zone_details_data_from_dict = GetDnsZoneDetailsData.from_dict(get_dns_zone_details_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


