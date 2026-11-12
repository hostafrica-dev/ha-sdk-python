# CreateDnsZoneRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**zone_ip** | **str** | Apex A record IPv4 for the new zone. Required by DNS Manager create. | 
**domain_name** | **str** | Zone domain name (FQDN). Optional; upstream resolves from domain_id when omitted. | [optional] 
**service_id** | **int** | WHMCS hosting service id — pass list-dns-zones / create-candidates hosting_id (or relid for HOSTING) as service_id. Helps DirectAdmin create routing when hosting is linked. | [optional] 
**type** | **int** | Zone type from list-dns-create-candidates: 0&#x3D;OTHER, 1&#x3D;DOMAIN, 2&#x3D;HOSTING, 3&#x3D;ADDON. Optional; upstream defaults from eligible packages. | [optional] 
**relid** | **int** | Related service id matching the zone type (from list-dns-create-candidates relid). Optional with type; for HOSTING/ADDON often the same value sent as service_id. | [optional] 
**template_id** | **int** | Optional DNS template id to apply after zone creation | [optional] 

## Example

```python
from ha_sdk_python.models.create_dns_zone_request_content import CreateDnsZoneRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDnsZoneRequestContent from a JSON string
create_dns_zone_request_content_instance = CreateDnsZoneRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateDnsZoneRequestContent.to_json())

# convert the object into a dict
create_dns_zone_request_content_dict = create_dns_zone_request_content_instance.to_dict()
# create an instance of CreateDnsZoneRequestContent from a dict
create_dns_zone_request_content_from_dict = CreateDnsZoneRequestContent.from_dict(create_dns_zone_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


