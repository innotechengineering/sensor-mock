from datetime import datetime
from typing import List, Optional, Literal

from pydantic import BaseModel
from enum import Enum

class SocketIOEvent(BaseModel):
  pass

class SensorUpdateEvent(SocketIOEvent):
  SensorType: Literal['switch', 'prox', 'placement']
  Location: Optional[str] = None
  StationId: int
  Value: bool
  AutoReset: Optional[bool] = False