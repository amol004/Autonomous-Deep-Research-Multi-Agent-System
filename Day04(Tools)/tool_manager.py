from tools import get_curent_time, roll_dice, generate_password


tools = {   
    "current_time": get_curent_time,
    "roll_dice": roll_dice,
    "generate_password": generate_password
}



def get_tool_by_name(name: str):
    """
    Returns the tool function by name
    """
    return tools.get(name)



def get_available_tools():
    """
    Returns the list of available tools
    """
    return list(tools.keys())       

    