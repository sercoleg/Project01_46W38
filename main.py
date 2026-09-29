def wind_turbine_power_output(wind_speed, interpolation_method):
    """
    Calculates the power output in kW of a public 15 MW wind turbine

    Parameters
    ----------
    wind_speed : float          # Wind speed [m/s]
    interpolation_method : str  # 'linear' or 'cubic'

    Returns
    -------
    Power output : float        # [kW]
    """

    # Variables' definition:
    wind_speed = float(wind_speed)
    rated_power = 15 # [MW]
    rated_power_kw = rated_power * 1000 # [kW]
    cut_in_wind_speed = 3 # [m/s]
    rated_wind_speed = 11 # [m/s]
    cut_out_wind_speed = 25 # [m/s]
    power_output = None
    g = None

    # If interpolation method is not defined, then, linear method is selected
    if not interpolation_method:
        interpolation_method = 'linear'

    # Defining weighting function g according to interpolation method selected
    if interpolation_method == 'linear':
        g = (wind_speed - cut_in_wind_speed) / (rated_wind_speed - cut_in_wind_speed)
    elif interpolation_method == 'cubic':
        g = (wind_speed ** 3) / (rated_wind_speed ** 3)

    # Calculating power output according wind speeds cases:
    # 1) below cut-in or above cut-out --> no power
    # 2) above cut-in and below rated --> according to g(wind_speed) weighting function and rated power
    # 3) above rated and below cut-out --> rated power
    if wind_speed < cut_in_wind_speed or wind_speed >= cut_out_wind_speed:
        power_output = 0
    elif cut_in_wind_speed <= wind_speed < rated_wind_speed:
        power_output = g * rated_power_kw
    elif wind_speed >= rated_wind_speed and wind_speed < cut_out_wind_speed:
        power_output = rated_power_kw

    return power_output
