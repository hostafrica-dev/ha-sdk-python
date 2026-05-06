# CatalogueConfigOption

A configurable option available for a product (e.g. Backup Quota, OS Template)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Config option identifier | 
**name** | **str** | Config option display name | 
**type** | **str** | Control type (e.g. selection, quantity) | 
**qty_min** | **int** | Minimum quantity (null for selection types) | [optional] 
**qty_max** | **int** | Maximum quantity (null for selection types) | [optional] 
**suboptions** | [**List[CatalogueConfigSuboption]**](CatalogueConfigSuboption.md) | Available suboptions for this config option | 

## Example

```python
from hostafrica_sdk_python.models.catalogue_config_option import CatalogueConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueConfigOption from a JSON string
catalogue_config_option_instance = CatalogueConfigOption.from_json(json)
# print the JSON string representation of the object
print(CatalogueConfigOption.to_json())

# convert the object into a dict
catalogue_config_option_dict = catalogue_config_option_instance.to_dict()
# create an instance of CatalogueConfigOption from a dict
catalogue_config_option_from_dict = CatalogueConfigOption.from_dict(catalogue_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


