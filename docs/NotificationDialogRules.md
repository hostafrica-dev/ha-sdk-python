# NotificationDialogRules

Dialog rules for notification creation/editing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_on_create** | **List[str]** | Fields required when creating a new notification | 
**condition_keys** | **List[str]** | Valid condition key values | 
**threshold_range** | **List[int]** | Threshold value range [min, max] | 
**period_min** | **int** | Minimum period value in minutes | 
**timeframe_min** | **int** | Minimum timeframe value in minutes | 

## Example

```python
from ha_sdk_python.models.notification_dialog_rules import NotificationDialogRules

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDialogRules from a JSON string
notification_dialog_rules_instance = NotificationDialogRules.from_json(json)
# print the JSON string representation of the object
print(NotificationDialogRules.to_json())

# convert the object into a dict
notification_dialog_rules_dict = notification_dialog_rules_instance.to_dict()
# create an instance of NotificationDialogRules from a dict
notification_dialog_rules_from_dict = NotificationDialogRules.from_dict(notification_dialog_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


