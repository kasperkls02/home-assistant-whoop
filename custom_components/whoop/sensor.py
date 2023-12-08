"""Platform for Whoop integration."""

from __future__ import annotations

import logging

import datetime
from tzlocal import get_localzone


from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)