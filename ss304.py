import argparse

def calculate_price(form, thickness, weight):
    # Base prices per kg for common forms and thicknesses
    base_prices = {
        "sheet": {2: 200, 3: 210, 4: 220},
        "plate": {2: 210, 3: 220, 4: 230, 8: 240},
        "pipe": {2: 220, 3: 230, 4: 240},
        "bar": {2: 230, 3: 240, 4: 250},
    }

    # Apply adjustments for different thicknesses
    thickness_factors = {
        1: 1.2,
        5: 0.98,
        6: 0.95,
        7: 0.92,
        8: 0.90,
        9: 0.88,
        10: 0.85,
        11: 0.82,
        12: 0.80,
        13: 0.78,
        14: 0.76,
        15: 0.74,
        16: 0.72,
        17: 0.70,
        18: 0.68,
    }

    # Get base price based on form and thickness
    try:
        base_price = base_prices[form][thickness]
    except KeyError:
        raise ValueError(f"Invalid form or thickness combination: {form}, {thickness}")

    # Adjust price based on thickness factor
    total_price = base_price * weight * thickness_factors.get(thickness, 1)

    return total_price

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the price of SS 304 Stainless Steel.")
    parser.add_argument("form", choices=["sheet", "plate", "pipe", "bar"], help="Form of the steel")
    parser.add_argument("thickness", type=int, help="Thickness of the material in millimeters")
    parser.add_argument("weight", type=float, help="Weight of the material in kilograms")

    args = parser.parse_args()

    price = calculate_price(args.form, args.thickness, args.weight)
    print(f"Total price: Rs. {price:.2f}")
