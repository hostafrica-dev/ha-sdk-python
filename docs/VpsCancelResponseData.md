# VpsCancelResponseData

Response data for VPS cancellation operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result of the operation | 
**service_id** | **int** | ID of the service being cancelled | 
**cancellation_type** | **str** | The cancellation type that was applied - &#39;Immediate&#39; or &#39;End of Billing Period&#39; | 
**status** | **str** | Current status of the cancellation request | 

## Example

```python
from ha_sdk_python.models.vps_cancel_response_data import VpsCancelResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of VpsCancelResponseData from a JSON string
vps_cancel_response_data_instance = VpsCancelResponseData.from_json(json)
# print the JSON string representation of the object
print(VpsCancelResponseData.to_json())

# convert the object into a dict
vps_cancel_response_data_dict = vps_cancel_response_data_instance.to_dict()
# create an instance of VpsCancelResponseData from a dict
vps_cancel_response_data_from_dict = VpsCancelResponseData.from_dict(vps_cancel_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


