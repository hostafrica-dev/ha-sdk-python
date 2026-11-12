# DeleteDnsZoneRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **str** | DNS Manager zone id from list-dns-zones. Required by upstream deletezone. | 
**domain_id** | **str** | Optional domain id from list-dns-zones when available. | [optional] 
**service_id** | **int** | Optional hosting service id (list-dns-zones hosting_id) when available. | [optional] 

## Example

```python
from ha_sdk_python.models.delete_dns_zone_request_content import DeleteDnsZoneRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDnsZoneRequestContent from a JSON string
delete_dns_zone_request_content_instance = DeleteDnsZoneRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDnsZoneRequestContent.to_json())

# convert the object into a dict
delete_dns_zone_request_content_dict = delete_dns_zone_request_content_instance.to_dict()
# create an instance of DeleteDnsZoneRequestContent from a dict
delete_dns_zone_request_content_from_dict = DeleteDnsZoneRequestContent.from_dict(delete_dns_zone_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


