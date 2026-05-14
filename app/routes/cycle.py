
from fastapi import APIRouter, Request
from rankine.rankine import Rankine, State
from rankine.improvements import Overheating, Overpressure, Underpressure
from rankine.specials import RankineReheating
from rankine.conversions import *

router = APIRouter(prefix='/rankine', tags=['rankine'])

@router.post('/ideal')
async def rankine(request: Request):
    data = await request.json()

    cycle = Rankine.from_diagram(data)
    cycle.resolve()

    return cycle.diagram

@router.post('/improvement/{nature}')
async def rankine_improvements(request: Request, nature: str):
    data = await request.json()
    cycle = Rankine.from_diagram(data)

    print(data['targets'])

    match nature:
        case "overheating":
            cycle_improved = Overheating.overheating(cycle, data['targets']['T'])
        case "overpressure":
            cycle_improved = Overpressure.overpressure(cycle, data['targets']['P'])
        case "underpressure":
            cycle_improved = Underpressure.underpressure(cycle, data['targets']['P'])

    return cycle_improved.diagram

@router.post('/special/{nature}')
async def rankine_special(request: Request, nature: str):
    data = await request.json()

    match nature:
        case "reheating":
            cycle = RankineReheating.from_diagram(data)
            cycle.resolve()
    
    return cycle.diagram
