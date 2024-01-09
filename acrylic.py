import argparse

def calculate_price(thickness, weight):
    # Base price per kg for common thickness (2mm)
    base_price_per_kg = 250

    # Price adjustment factors for different thicknesses
    price_adjustments = {
        1: 0.2, # 20% higher for 1mm
        2: 0.1, # 10% higher for 2mm (included in base price)
        3: 0, # No adjustment for 3mm
        4: -0.05, # 5% lower for 4mm
        5: -0.1, # 10% lower for 5mm
        6: -0.15, # 15% lower for 6mm
        7: -0.2, # 20% lower for 7mm
        8: -0.25, # 25% lower for 8mm
        9: -0.3, # 30% lower for 9mm
        10: -0.35, # 35% lower for 10mm
        12: -0.4, # 40% lower for 12mm
        15: -0.45, # 45% lower for 15mm
        18: -0.5, # 50% lower for 18mm
    }

    # Adjust price based on thickness
    thickness_factor = 1 + price_adjustments.get(thickness, 0)

    total_price = base_price_per_kg * weight * thickness_factor
    return total_price

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the price of acrylic sheets.")
    parser.add_argument("thickness", type=int, help="Thickness of the sheet in millimeters (1-18)")
    parser.add_argument("weight", type=float, help="Weight of the sheet in kilograms")

    args = parser.parse_args()

    if args.thickness < 1 or args.thickness > 18:
        print("Invalid thickness. Please enter a value between 1 and 18.")
    else:
        price = calculate_price(args.thickness, args.weight)
        print(f"Total price: Rs. {price:.2f}")
