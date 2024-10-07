from enum import StrEnum
from dataclasses import dataclass
from datetime import datetime

class EnergyType(StrEnum):
	ELECTRICITY = "Electricity"
	WATER = "Water"
	HEAT = "Heat"
	DISTRICT_COOLING = "DistrictCooling"

class TimeSplit(StrEnum):
	MONTHLY = "Monthly"
	DAILY = "Daily"
	HOURLY = "Hourly"

@dataclass
class EnergySlice:
	__start_date : datetime
	__end_date : datetime
	energy_type : EnergyType

	@property
	def start_date(self):
		return self.__start_date.strftime("%Y-%m-%d")

	@property
	def end_date(self):
		return self.__end_date.strftime("%Y-%m-%d")