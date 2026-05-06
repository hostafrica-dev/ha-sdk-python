# NotificationCreateResponseData

Response data for notification creation operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**notification** | [**Notification**](Notification.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.notification_create_response_data import NotificationCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCreateResponseData from a JSON string
notification_create_response_data_instance = NotificationCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(NotificationCreateResponseData.to_json())

# convert the object into a dict
notification_create_response_data_dict = notification_create_response_data_instance.to_dict()
# create an instance of NotificationCreateResponseData from a dict
notification_create_response_data_from_dict = NotificationCreateResponseData.from_dict(notification_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


