# ListVpsServicesData

List VPS response data - matches upstream API format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[VpsServiceInfo]**](VpsServiceInfo.md) | Array of VPS services | 

## Example

```python
from ha_sdk_python.models.list_vps_services_data import ListVpsServicesData

# TODO update the JSON string below
json = "{}"
# create an instance of ListVpsServicesData from a JSON string
list_vps_services_data_instance = ListVpsServicesData.from_json(json)
# print the JSON string representation of the object
print(ListVpsServicesData.to_json())

# convert the object into a dict
list_vps_services_data_dict = list_vps_services_data_instance.to_dict()
# create an instance of ListVpsServicesData from a dict
list_vps_services_data_from_dict = ListVpsServicesData.from_dict(list_vps_services_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


