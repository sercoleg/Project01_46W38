def wind_turbine_power_output(
        wind_speed,
        rated_power = 15,
        cut_in_wind_speed = 3,
        rated_wind_speed = 11,
        cut_out_wind_speed = 25,
        interpolation_method = 'linear'):
    """
    Calculates the power output in MW of a public 15 MW wind turbine

    Parameters
    ----------
    wind_speed : float
        Wind speed [m/s]

    rated_power : float, default = 15
        Rated power [MW]

    cut_in_wind_speed : float, default = 3
        Cut-in wind speed [m/s]

    rated_wind_speed : float, default = 11
        Rated wind speed [m/s]

    cut_out_wind_speed : float, default = 25
        Cut-out wind speed [m/s]

    interpolation_method : str, default = 'linear'
        'linear' or 'cubic'

    Returns
    -------
    power_output : float
        Power output [MW]
    """

    # Defining weighting function g according to interpolation method selected
    if interpolation_method == 'linear':
        g = (wind_speed - cut_in_wind_speed) / (rated_wind_speed - cut_in_wind_speed)
    elif interpolation_method == 'cubic':
        g = (wind_speed ** 3) / (rated_wind_speed ** 3)
    # If interpolation method is not 'linear' nor 'cubic', then, raise an error
    else:
        raise ValueError("interpolation_method should be 'linear' or 'cubic'")

    # Calculating power output according wind speeds cases:
    # 1) below cut-in or above cut-out --> no power
    # 2) above cut-in and below rated --> according to g(wind_speed) weighting function and rated power
    # 3) above rated and below cut-out --> rated power
    if wind_speed < cut_in_wind_speed or wind_speed >= cut_out_wind_speed:
        power_output = 0
    elif cut_in_wind_speed <= wind_speed < rated_wind_speed:
        power_output = g * rated_power
    elif wind_speed >= rated_wind_speed and wind_speed < cut_out_wind_speed:
        power_output = rated_power

    return power_output
