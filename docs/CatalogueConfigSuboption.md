# CatalogueConfigSuboption

A suboption (selectable value) within a config option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Suboption identifier | 
**name** | **str** | Suboption display name | 
**prices** | **object** | Per-cycle prices for this suboption | 

## Example

```python
from ha_sdk_python.models.catalogue_config_suboption import CatalogueConfigSuboption

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueConfigSuboption from a JSON string
catalogue_config_suboption_instance = CatalogueConfigSuboption.from_json(json)
# print the JSON string representation of the object
print(CatalogueConfigSuboption.to_json())

# convert the object into a dict
catalogue_config_suboption_dict = catalogue_config_suboption_instance.to_dict()
# create an instance of CatalogueConfigSuboption from a dict
catalogue_config_suboption_from_dict = CatalogueConfigSuboption.from_dict(catalogue_config_suboption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


