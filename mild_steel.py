import argparse

def calculate_price(component_type, weight):
   prices = {
       "sheets": 56,
       "plates": 58,
       "pipes": 57,
       "bars": 55
   }

   price_per_kg = prices.get(component_type)
   if price_per_kg is None:
       raise ValueError(f"Invalid component type: {component_type}")

   total_price = price_per_kg * weight
   return total_price

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Calculate the price of mild steel components.")
   parser.add_argument("component_type", choices=["sheets", "plates", "pipes", "bars"], help="Type of component")
   parser.add_argument("weight", type=float, help="Weight of the component in kilograms")

   args = parser.parse_args()
   price = calculate_price(args.component_type, args.weight)
   print(f"Total price: Rs. {price:.2f}")
