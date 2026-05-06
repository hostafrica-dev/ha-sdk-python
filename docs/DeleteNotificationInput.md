# DeleteNotificationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**notification_id** | **int** | Notification ID to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_notification_input import DeleteNotificationInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNotificationInput from a JSON string
delete_notification_input_instance = DeleteNotificationInput.from_json(json)
# print the JSON string representation of the object
print(DeleteNotificationInput.to_json())

# convert the object into a dict
delete_notification_input_dict = delete_notification_input_instance.to_dict()
# create an instance of DeleteNotificationInput from a dict
delete_notification_input_from_dict = DeleteNotificationInput.from_dict(delete_notification_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


