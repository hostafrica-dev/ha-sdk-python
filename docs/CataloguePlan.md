# CataloguePlan

A plan (size tier) available for a product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Plan identifier | 
**name** | **str** | Plan display name (e.g. C1, C2) | 
**cpu** | **int** | Number of vCPUs | 
**ram** | **int** | RAM in GB | 
**disk** | **int** | Disk size in GB | 
**bandwidth** | **int** | Bandwidth allowance in GB | 
**backups** | **int** | Number of included backup slots | 
**snapshots** | **int** | Number of included snapshot slots | 
**pricing** | **object** | Per-cycle pricing for this plan | 

## Example

```python
from ha_sdk_python.models.catalogue_plan import CataloguePlan

# TODO update the JSON string below
json = "{}"
# create an instance of CataloguePlan from a JSON string
catalogue_plan_instance = CataloguePlan.from_json(json)
# print the JSON string representation of the object
print(CataloguePlan.to_json())

# convert the object into a dict
catalogue_plan_dict = catalogue_plan_instance.to_dict()
# create an instance of CataloguePlan from a dict
catalogue_plan_from_dict = CataloguePlan.from_dict(catalogue_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


