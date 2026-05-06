# GetVpsDetailsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsDetailsResponse**](VpsDetailsResponse.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_vps_details_response_content import GetVpsDetailsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpsDetailsResponseContent from a JSON string
get_vps_details_response_content_instance = GetVpsDetailsResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetVpsDetailsResponseContent.to_json())

# convert the object into a dict
get_vps_details_response_content_dict = get_vps_details_response_content_instance.to_dict()
# create an instance of GetVpsDetailsResponseContent from a dict
get_vps_details_response_content_from_dict = GetVpsDetailsResponseContent.from_dict(get_vps_details_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


