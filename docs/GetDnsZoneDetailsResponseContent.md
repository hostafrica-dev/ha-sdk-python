# GetDnsZoneDetailsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**GetDnsZoneDetailsData**](GetDnsZoneDetailsData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_dns_zone_details_response_content import GetDnsZoneDetailsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetDnsZoneDetailsResponseContent from a JSON string
get_dns_zone_details_response_content_instance = GetDnsZoneDetailsResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetDnsZoneDetailsResponseContent.to_json())

# convert the object into a dict
get_dns_zone_details_response_content_dict = get_dns_zone_details_response_content_instance.to_dict()
# create an instance of GetDnsZoneDetailsResponseContent from a dict
get_dns_zone_details_response_content_from_dict = GetDnsZoneDetailsResponseContent.from_dict(get_dns_zone_details_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


