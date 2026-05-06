# DeleteNotificationRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**notification_id** | **int** | Notification ID to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_notification_request_content import DeleteNotificationRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNotificationRequestContent from a JSON string
delete_notification_request_content_instance = DeleteNotificationRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteNotificationRequestContent.to_json())

# convert the object into a dict
delete_notification_request_content_dict = delete_notification_request_content_instance.to_dict()
# create an instance of DeleteNotificationRequestContent from a dict
delete_notification_request_content_from_dict = DeleteNotificationRequestContent.from_dict(delete_notification_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


