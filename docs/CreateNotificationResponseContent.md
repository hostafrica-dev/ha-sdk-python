# CreateNotificationResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NotificationCreateResponseData**](NotificationCreateResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.create_notification_response_content import CreateNotificationResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationResponseContent from a JSON string
create_notification_response_content_instance = CreateNotificationResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationResponseContent.to_json())

# convert the object into a dict
create_notification_response_content_dict = create_notification_response_content_instance.to_dict()
# create an instance of CreateNotificationResponseContent from a dict
create_notification_response_content_from_dict = CreateNotificationResponseContent.from_dict(create_notification_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


