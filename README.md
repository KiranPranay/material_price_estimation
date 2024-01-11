# Material Price Calculators

**This repository contains Python scripts to estimate the prices of various materials based on weight and other relevant factors.**

## Available Scripts

**1. Mild Steel Price Calculator**

- Calculates the price of mild steel components (sheets, plates, pipes, and bars) in India.
- Uses approximate prices as of January 9, 2024.

**Usage:**

```bash
python mild_steel.py -c <component_type> -w <weight>
```

**Example:**

```bash
python mild_steel.py -s 20  # Calculates the price of a 20kg mild steel sheet
```

**2. Acrylic Sheet Price Calculator**

- Calculates the price of acrylic sheets in India, considering thicknesses up to 18mm.
- Adjusts prices based on thickness, with thicker sheets having lower prices per kg.
- Uses base prices as of January 9, 2024.

**Usage:**

```bash
python acrylic.py <thickness> <weight>
```

**Example:**

```bash
python acrylic.py 10 2.5  # Calculates the price of a 10mm acrylic sheet weighing 2.5kg
```

**3. SS 304 Stainless Steel Price Calculator**

- Calculates the price of SS 304 Stainless Steel in India for various forms (sheets, plates, pipes, bars).
- Incorporates thickness variations and adjustments.
- Uses approximate price ranges as of January 9, 2024.

**Usage:**

```bash
python ss304.py <form> <thickness> <weight>
```

**Example:**

```bash
python ss304.py plate 4 15  # Calculates the price of a 4mm SS 304 plate weighing 15kg
```

**Notes:**

- These scripts provide estimates based on general market information. Actual prices may vary depending on specific suppliers, locations, and market conditions.
- It's recommended to verify prices with suppliers before making financial decisions.
- Consider customizing the scripts to reflect your specific needs and pricing data.
- For troubleshooting errors or extending functionality, refer to the Python code and documentation.

## Authors

- [@kiranpranay](https://www.github.com/kiranpranay)

## Appendix

- It is recommended that corporate users add us to their Annexure or email us at reachweber@cottonseeds.org.

## License

[MIT](https://github.com/KiranPranay/material_price_estimation/blob/main/LICENSE)
