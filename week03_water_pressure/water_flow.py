

# CSE 111 W03 Project: Water Pressure
# Enhancement:
# 1. Uses constants for water density, gravity, and viscosity.
# 2. Converts pressure from kilopascals (kPa) to psi.
# 3. Displays the final pressure in both kPa and psi.

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column."""
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    """Calculate pressure gained from water height in kPa."""
    return (
        WATER_DENSITY
        * EARTH_ACCELERATION_OF_GRAVITY
        * height / 1000
    )


def pressure_loss_from_pipe(
        pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate pressure loss from a pipe in kPa."""
    return (
        -friction_factor
        * pipe_length
        * WATER_DENSITY
        * fluid_velocity**2
        / (2000 * pipe_diameter)
    )


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate pressure loss from fittings in kPa."""
    return (
        -0.04
        * WATER_DENSITY
        * fluid_velocity**2
        * quantity_fittings
        / 2000
    )


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number."""
    return (
        WATER_DENSITY
        * hydraulic_diameter
        * fluid_velocity
        / WATER_DYNAMIC_VISCOSITY
    )


def pressure_loss_from_pipe_reduction(
        larger_diameter, fluid_velocity,
        reynolds_number, smaller_diameter):
    """Calculate pressure loss from pipe reduction."""
    k = (
        0.1 + 50 / reynolds_number
    ) * (
        (larger_diameter / smaller_diameter)**4 - 1
    )

    return (
        -k
        * WATER_DENSITY
        * fluid_velocity**2
        / 2000
    )


def kpa_to_psi(kpa):
    """Convert kilopascals to pounds per square inch."""
    return kpa * 0.1450377377


def main():
    """Calculate the water pressure at a house."""

    tower_height = float(
        input("Height of water tower (meters): ")
    )

    tank_height = float(
        input("Height of water tank walls (meters): ")
    )

    length1 = float(
        input("Length of supply pipe from tank to lot (meters): ")
    )

    quantity_fittings = int(
        input("Number of 90° angles in supply pipe: ")
    )

    length2 = float(
        input("Length of pipe from supply to house (meters): ")
    )

    # Pipe properties
    diameter1 = 0.28687
    diameter2 = 0.048692

    friction_factor1 = 0.013
    friction_factor2 = 0.018

    # Water velocity in the supply pipe
    velocity = 1.65

    # Calculate pressure gained from the water column.
    height = water_column_height(tower_height, tank_height)

    pressure = pressure_gain_from_water_height(height)

    # Calculate pressure loss in the first pipe.
    pressure += pressure_loss_from_pipe(
        diameter1, length1, friction_factor1, velocity
    )

    # Calculate pressure loss from fittings.
    pressure += pressure_loss_from_fittings(
        velocity, quantity_fittings
    )

    # Calculate Reynolds number.
    reynolds = reynolds_number(diameter1, velocity)

    # Calculate pressure loss from pipe reduction.
    pressure += pressure_loss_from_pipe_reduction(
        diameter1, velocity, reynolds, diameter2
    )

    # IMPORTANT CORRECTION:
    # Change velocity to 1.75 m/s for the pipe leading to the house.
    velocity = 1.75

    # Calculate pressure loss in the smaller pipe.
    pressure += pressure_loss_from_pipe(
        diameter2, length2, friction_factor2, velocity
    )

    # Display pressure in kilopascals and psi.
    print(f"Pressure at house: {pressure:.1f} kilopascals")

    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")


if __name__ == "__main__":
    main()
