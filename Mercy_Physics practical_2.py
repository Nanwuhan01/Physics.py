"""
Five Common Physics Formulas (Interactive Console App)
"""

def kinetic_energy(mass, velocity):
    """KE = 1/2 * m * v^2  (Joules)"""
    return 0.5 * mass * velocity ** 2


def work_done(force, distance):
    """W = F * d  (Joules)"""
    return force * distance


def momentum(mass, velocity):
    """p = m * v  (kg·m/s)"""
    return mass * velocity


def ohms_law(voltage=None, current=None, resistance=None):
    """V = I * R  -- pass any two values, get the third."""
    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current
    else:
        raise ValueError("Provide exactly two known values, leave one as None.")


def wave_speed(frequency, wavelength):
    """v = f * λ  (m/s)"""
    return frequency * wavelength


def main():
    while True:
        print("\n" + "=" * 40)
        print("    PHYSICS FORMULA CALCULATOR")
        print("=" * 40)
        print("1. Kinetic Energy (KE = 1/2 * m * v^2)")
        print("2. Work Done (W = F * d)")
        print("3. Momentum (p = m * v)")
        print("4. Ohm's Law (V = I * R)")
        print("5. Wave Speed (v = f * λ)")
        print("6. Exit")
        
        choice = input("\nSelect a formula (1-6): ").strip()

        if choice == "1":
            print("\n--- Kinetic Energy ---")
            m = float(input("Enter mass (kg): "))
            v = float(input("Enter velocity (m/s): "))
            result = kinetic_energy(m, v)
            print(f"Kinetic Energy = {result} J")

        elif choice == "2":
            print("\n--- Work Done ---")
            f = float(input("Enter force (N): "))
            d = float(input("Enter distance (m): "))
            result = work_done(f, d)
            print(f"Work Done = {result} J")

        elif choice == "3":
            print("\n--- Momentum ---")
            m = float(input("Enter mass (kg): "))
            v = float(input("Enter velocity (m/s): "))
            result = momentum(m, v)
            print(f"Momentum = {result} kg·m/s")

        elif choice == "4":
            print("\n--- Ohm's Law ---")
            print("Select what you want to calculate:")
            print("  a. Voltage (V = I * R)")
            print("  b. Current (I = V / R)")
            print("  c. Resistance (R = V / I)")
            sub_choice = input("Choice (a/b/c): ").strip().lower()

            if sub_choice == "a":
                i = float(input("Enter current (A): "))
                r = float(input("Enter resistance (ohms): "))
                print(f"Voltage = {ohms_law(current=i, resistance=r)} V")
            elif sub_choice == "b":
                v = float(input("Enter voltage (V): "))
                r = float(input("Enter resistance (ohms): "))
                print(f"Current = {ohms_law(voltage=v, resistance=r)} A")
            elif sub_choice == "c":
                v = float(input("Enter voltage (V): "))
                i = float(input("Enter current (A): "))
                print(f"Resistance = {ohms_law(voltage=v, current=i)} ohms")
            else:
                print("Invalid Ohm's law choice!")

        elif choice == "5":
            print("\n--- Wave Speed ---")
            f = float(input("Enter frequency (Hz): "))
            l = float(input("Enter wavelength (m): "))
            result = wave_speed(f, l)
            print(f"Wave Speed = {result} m/s")

        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()