# ListVpsServicesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListVpsServicesData**](ListVpsServicesData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_vps_services_output import ListVpsServicesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListVpsServicesOutput from a JSON string
list_vps_services_output_instance = ListVpsServicesOutput.from_json(json)
# print the JSON string representation of the object
print(ListVpsServicesOutput.to_json())

# convert the object into a dict
list_vps_services_output_dict = list_vps_services_output_instance.to_dict()
# create an instance of ListVpsServicesOutput from a dict
list_vps_services_output_from_dict = ListVpsServicesOutput.from_dict(list_vps_services_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


