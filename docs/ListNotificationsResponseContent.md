# ListNotificationsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NotificationListResponseData**](NotificationListResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_notifications_response_content import ListNotificationsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationsResponseContent from a JSON string
list_notifications_response_content_instance = ListNotificationsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListNotificationsResponseContent.to_json())

# convert the object into a dict
list_notifications_response_content_dict = list_notifications_response_content_instance.to_dict()
# create an instance of ListNotificationsResponseContent from a dict
list_notifications_response_content_from_dict = ListNotificationsResponseContent.from_dict(list_notifications_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


