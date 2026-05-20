# PowerTaskDialogRules

Dialog rules for power task creation/editing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_on_create** | **List[str]** | Fields required when creating a new power task | 
**job_type_values** | **List[str]** | Valid job type values | 
**action_values** | **List[str]** | Valid action values | 
**weekday_values** | **List[str]** | Valid weekday abbreviations | 
**job_minutes_step** | **int** | Minute step increment for job time selection | 

## Example

```python
from ha_sdk_python.models.power_task_dialog_rules import PowerTaskDialogRules

# TODO update the JSON string below
json = "{}"
# create an instance of PowerTaskDialogRules from a JSON string
power_task_dialog_rules_instance = PowerTaskDialogRules.from_json(json)
# print the JSON string representation of the object
print(PowerTaskDialogRules.to_json())

# convert the object into a dict
power_task_dialog_rules_dict = power_task_dialog_rules_instance.to_dict()
# create an instance of PowerTaskDialogRules from a dict
power_task_dialog_rules_from_dict = PowerTaskDialogRules.from_dict(power_task_dialog_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


