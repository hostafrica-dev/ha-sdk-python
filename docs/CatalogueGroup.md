# CatalogueGroup

A product group in the catalogue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Group identifier | 
**name** | **str** | Group display name (e.g. Linux Cloud Servers) | 
**products** | [**List[CatalogueProduct]**](CatalogueProduct.md) | Products within this group | 

## Example

```python
from ha_sdk_python.models.catalogue_group import CatalogueGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueGroup from a JSON string
catalogue_group_instance = CatalogueGroup.from_json(json)
# print the JSON string representation of the object
print(CatalogueGroup.to_json())

# convert the object into a dict
catalogue_group_dict = catalogue_group_instance.to_dict()
# create an instance of CatalogueGroup from a dict
catalogue_group_from_dict = CatalogueGroup.from_dict(catalogue_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


