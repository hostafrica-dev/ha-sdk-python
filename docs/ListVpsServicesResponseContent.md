# ListVpsServicesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListVpsServicesData**](ListVpsServicesData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_vps_services_response_content import ListVpsServicesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListVpsServicesResponseContent from a JSON string
list_vps_services_response_content_instance = ListVpsServicesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListVpsServicesResponseContent.to_json())

# convert the object into a dict
list_vps_services_response_content_dict = list_vps_services_response_content_instance.to_dict()
# create an instance of ListVpsServicesResponseContent from a dict
list_vps_services_response_content_from_dict = ListVpsServicesResponseContent.from_dict(list_vps_services_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


