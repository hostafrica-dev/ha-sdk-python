# DnsZoneInfo

A DNS zone owned by the authenticated client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **str** | DNS Manager zone id (or DirectAdmin index id). Required for dns_manager record mutations and delete-zone. Often null on DirectAdmin — use domain_id (+ service_id from hosting_id) instead. | [optional] 
**domain_id** | **str** | Domain id. Preferred identity when present; required for DirectAdmin get-zone/record/delete-zone when the row is a registered domain. | [optional] 
**domain_name** | **str** | Zone domain name (FQDN). Send as domain_name on manage POSTs. | [optional] 
**hosting_id** | **int** | Hosting service id. Pass as service_id on create-zone/delete-zone (and record mutations when needed) when domain_id is null, or to help DirectAdmin routing. | [optional] 
**type** | **int** | Zone type: 0&#x3D;OTHER, 1&#x3D;DOMAIN, 2&#x3D;HOSTING, 3&#x3D;ADDON | [optional] 
**type_key** | **str** | Zone type key (e.g. other, domain, hosting, addon). Indicates which id fields are populated; does not change URLs. | [optional] 
**package_name** | **str** | Product or package name for the zone | [optional] 
**has_hosting** | [**DomainHostingLink**](DomainHostingLink.md) |  | [optional] 
**has_dns_manager_zone** | **bool** | Whether a DNS Manager zone exists for this domain name | 
**backend** | [**DnsBackend**](DnsBackend.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.dns_zone_info import DnsZoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DnsZoneInfo from a JSON string
dns_zone_info_instance = DnsZoneInfo.from_json(json)
# print the JSON string representation of the object
print(DnsZoneInfo.to_json())

# convert the object into a dict
dns_zone_info_dict = dns_zone_info_instance.to_dict()
# create an instance of DnsZoneInfo from a dict
dns_zone_info_from_dict = DnsZoneInfo.from_dict(dns_zone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


