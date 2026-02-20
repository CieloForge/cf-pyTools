# Profit Estimator 📈

A powerful CLI tool for calculating compound growth and profit estimates with support for various time periods and natural language parsing.

## Features ✨

- **Compound growth calculation** with detailed breakdown
- **Natural language period parsing** (supports "twice a day", "three times a week", "monthly", etc.)
- **Beautiful, colorful output** using Click's styling
- **Effective annual rate calculation** for all period types
- **Period-by-period breakdown** for small numbers of increments
- **Input validation** and error handling
- **Support for various time periods**: hourly, daily, weekly, monthly, yearly, and custom frequencies

## Installation 🛠️

### Prerequisites
- Python 3.12+
- UV 0.10.4 (079e3fd05 2026-02-17)

### Using conda + uv (Recommended)
```bash
conda env create -f environment.yml
conda activate cf-pyTools
cd profit-estimator
uv sync 
source .venv/bin/activate
```

## Usage 🎯

### Calculate Profit Estimate
```bash
uv run python profit-estimator.py estimate --initial <initial_amount> --gain <gain_per_period> --period <period_type> --increments <number_of_periods>
```

#### Examples
```bash
# Calculate growth of $1000 with 5% monthly gain for 12 months
uv run python profit-estimator.py estimate --initial 1000 --gain 5 --period monthly --increments 12

# Calculate growth of $5000 with 2% weekly gain for 52 weeks
uv run python profit-estimator.py estimate --initial 5000 --gain 2 --period weekly --increments 52

# Calculate growth of $2000 with 0.5% gain twice a day for 30 days
uv run python profit-estimator.py estimate --initial 2000 --gain 0.5 --period "twice a day" --increments 60
```

### Get Help
```bash
uv run python profit-estimator.py --help
uv run python profit-estimator.py estimate --help
```

## Options 📋

### Main Command
| Option | Description |
|--------|-------------|
| `--help` | Show help message |

### Estimate Subcommand
| Option | Description |
|--------|-------------|
| `--initial` | Initial investment amount (e.g., 1000.0) [required] |
| `--gain` | Estimated % gain per period (e.g., 5 for 5%) [required] |
| `--period` | Name of the period (e.g., "monthly", "yearly", "weekly", "twice a day") [required] |
| `--increments` | Number of periods (e.g., 12, 60) [required] |

## Supported Period Formats 🕐

The tool supports a wide range of period formats:

### Simple Periods
- `hourly`, `hour`
- `daily`, `day`  
- `weekly`, `week`
- `monthly`, `month`
- `yearly`, `year`, `annually`

### Frequent Periods (textual numbers)
- `once a day`, `once per hour`, `once daily`
- `twice a week`, `twice per month`, `twice weekly`
- `three times a day`, `three times per week`, `three times weekly`
- ... up to twelve times per period

### Frequent Periods (numeric)
- `2 a day`, `2 per hour`, `2 times a week`
- `3 a week`, `3 per month`, `3 times per year`
- ... any numeric frequency

## Technology Stack 🛠️

- **Python 3.12** - Core language
- **Click** - Command-line interface framework
- **Regular Expressions** - For natural language period parsing

## Project Structure 📁

```
profit-estimator/
├── profit-estimator.py    # Main application logic
├── .python-version        # Python version specification
├── pyproject.toml         # Project dependencies
├── uv.lock                # Dependency lock file
└── README.md              # This file
```

## Example Output 📊

```
┌──────────────────────────────────────────────┐
          Compound Growth Estimate             
└──────────────────────────────────────────────┘
  Initial amount       :  $1,000.00
  Gain per monthly  :  +5.00%
  Number of periods     :  12
  Growth multiplier     :  ×1.796

Progression (first few and last periods):
  After  1 monthly   → $1,050.00
  After  2 monthly   → $1,102.50
  After  3 monthly   → $1,157.62
  After  4 monthly   → $1,215.51
  After  5 monthly   → $1,276.28
  ...
  After 12 monthly   → $1,795.86

  Final amount          :  $1,795.86
  Total profit          :  $795.86
  Total return          :  +79.59%
  ≈ Effective annual rate : 79.59%
```

## Contributing 🤝

Feel free to fork, improve, and create a pull request. Your contributions are always welcome!

## License 📄

MIT License - feel free to use this project for personal or commercial purposes.

## Acknowledgments 🙏

- Click library for easy CLI creation
