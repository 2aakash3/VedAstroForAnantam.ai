from fastapi import FastAPI, Query
from vedastro import GeoLocation, Time, Calculate, PlanetName

app = FastAPI()

@app.get("/planet")
def get_planet_data(
    planet: str = Query(...),
    datetime: str = Query(...),
    location: str = Query(default="Delhi")
):
    try:
        geo = GeoLocation(location, 77.21, 28.61)  # For simplicity, using Delhi coords
        time = Time(datetime, geo)
        result = Calculate.AllPlanetData(PlanetName[planet], time)
        return {"result": str(result)}
    except Exception as e:
        return {"error": str(e)}