from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrashCan")


@attr.s(auto_attribs=True)
class TrashCan:
    """ """

    id: int
    deployed: Union[Unset, bool] = UNSET
    power: Union[Unset, str] = UNSET
    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    capacity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        deployed = self.deployed
        power = self.power
        lat = self.lat
        lon = self.lon
        capacity = self.capacity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if deployed is not UNSET:
            field_dict["deployed"] = deployed
        if power is not UNSET:
            field_dict["power"] = power
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        deployed = d.pop("deployed", UNSET)

        power = d.pop("power", UNSET)

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        capacity = d.pop("capacity", UNSET)

        trash_can = cls(
            id=id,
            deployed=deployed,
            power=power,
            lat=lat,
            lon=lon,
            capacity=capacity,
        )

        trash_can.additional_properties = d
        return trash_can

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
