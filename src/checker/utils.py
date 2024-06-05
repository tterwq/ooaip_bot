from typing import Dict, Any

def check_similary(metrics1: Dict[str, Any], metrics2: Dict[str, Any]) -> Dict[str, Any]:
    result = {}
    for key in metrics1:
        if key in metrics2 and metrics1[key] == metrics2[key]:
            result[key] = metrics1[key]
    
    return result