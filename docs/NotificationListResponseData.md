# NotificationListResponseData

Response data for listing notifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**notifications** | [**List[Notification]**](Notification.md) | List of notifications | 
**dialog_rules** | [**NotificationDialogRules**](NotificationDialogRules.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.notification_list_response_data import NotificationListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationListResponseData from a JSON string
notification_list_response_data_instance = NotificationListResponseData.from_json(json)
# print the JSON string representation of the object
print(NotificationListResponseData.to_json())

# convert the object into a dict
notification_list_response_data_dict = notification_list_response_data_instance.to_dict()
# create an instance of NotificationListResponseData from a dict
notification_list_response_data_from_dict = NotificationListResponseData.from_dict(notification_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


