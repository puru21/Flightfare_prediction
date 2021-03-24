from pydantic import BaseModel

class FlightFare(BaseModel):
    date_of_journey : str
    source : str
    destination : str
    dep_time : str
    arrival_time : str
    stopage : int
    airline : str 
