# VpsCancelDetails

Nested details within a VPS cancellation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **int** | ID of the service being cancelled | 
**cancellation_type** | **str** | The cancellation type that was applied - &#39;Immediate&#39; or &#39;End of Billing Period&#39; | 
**status** | **str** | Current status of the cancellation request | 

## Example

```python
from hostafrica_sdk_python.models.vps_cancel_details import VpsCancelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VpsCancelDetails from a JSON string
vps_cancel_details_instance = VpsCancelDetails.from_json(json)
# print the JSON string representation of the object
print(VpsCancelDetails.to_json())

# convert the object into a dict
vps_cancel_details_dict = vps_cancel_details_instance.to_dict()
# create an instance of VpsCancelDetails from a dict
vps_cancel_details_from_dict = VpsCancelDetails.from_dict(vps_cancel_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


