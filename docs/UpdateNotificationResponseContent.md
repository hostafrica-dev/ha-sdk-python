# UpdateNotificationResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NotificationCreateResponseData**](NotificationCreateResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.update_notification_response_content import UpdateNotificationResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationResponseContent from a JSON string
update_notification_response_content_instance = UpdateNotificationResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationResponseContent.to_json())

# convert the object into a dict
update_notification_response_content_dict = update_notification_response_content_instance.to_dict()
# create an instance of UpdateNotificationResponseContent from a dict
update_notification_response_content_from_dict = UpdateNotificationResponseContent.from_dict(update_notification_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


