# ListNotificationsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NotificationListResponseData**](NotificationListResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_notifications_output import ListNotificationsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationsOutput from a JSON string
list_notifications_output_instance = ListNotificationsOutput.from_json(json)
# print the JSON string representation of the object
print(ListNotificationsOutput.to_json())

# convert the object into a dict
list_notifications_output_dict = list_notifications_output_instance.to_dict()
# create an instance of ListNotificationsOutput from a dict
list_notifications_output_from_dict = ListNotificationsOutput.from_dict(list_notifications_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


