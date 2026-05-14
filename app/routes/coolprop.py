
from fastapi import APIRouter, Request
import CoolProp.CoolProp as CP

router = APIRouter(prefix='/coolprop', tags=['coolprop'])

def get_unit(paramter):
    return {
        'H': 'J/kg',
        'S': 'J/kg·K',
        'V': 'm3/kg',
        'Q': '',
        'P': 'Pa',
        'T': 'K',
        'D': 'kg/m3'
    }[paramter]

@router.post('/')
async def rankine(request: Request):
    data = await request.json()

    fluid = data['fluid']
    parameters = data['parameters']
    targets = data['targets']

    data = []
    for target in targets:
        data.append({
            'parameter': target,
            'value': CP.PropsSI(
                target, parameters[0][0], parameters[0][1], 
                parameters[1][0], parameters[1][1], fluid
            ),
            'unit': get_unit(target)
        })

    return {
        "data": data
    }
