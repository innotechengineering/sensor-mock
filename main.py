from fastapi import FastAPI, HTTPException
from models import SensorUpdateEvent

app = FastAPI()


@app.post('/api/sensor/update', tags=['Sensors'], status_code=204)
async def update_sensor(*, event: SensorUpdateEvent) -> None:

    if event.SensorType == 'placement':
        if event.Location not in ['test1', 'test2']:
            raise HTTPException(status_code=404, detail="location not found")



