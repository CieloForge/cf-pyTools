# Currency Converter 🚀

A simple, beautiful, and fast CLI currency converter with real-time exchange rates from open.er-api.com.

## Features ✨

- **Real-time exchange rates** from open.er-api.com
- **170+ supported currencies**
- **Beautiful, colorful output** using Rich library
- **Precise mode** for more decimal places
- **List available currencies** option
- **Error handling** for invalid currencies and API failures
- **Lightning fast** with minimal dependencies

## Installation 🛠️

### Prerequisites
- Python 3.12+
- Conda (for environment management)
- UV 0.10.4+ (for package management)

### Using Conda + UV (Recommended)
1. Create and activate the conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate cf-pyTools
   ```

2. Navigate to the currency-converter directory and activate the UV virtual environment:
   ```bash
   cd currency-converter
   uv sync
   source .venv/bin/activate
   ```

## Usage 🎯

### Convert Currency
```bash
uv run currency <amount> <from_currency> <to_currency>
```

#### Examples
```bash
# Convert 500 Philippine Pesos to US Dollars
uv run currency 500 PHP USD

# Convert 1200 US Dollars to Japanese Yen with precise mode
uv run currency 1200 USD JPY --precise
```

### List Currencies
```bash
uv run currency --list
```

### Get Help
```bash
uv run currency --help
```

## Options 📋

| Option | Description |
|--------|-------------|
| `--list` | List available currencies and exit |
| `--precise` | Show more decimal places in exchange rate (6 instead of 4) |
| `-h, --help` | Show help message |

## Supported Currencies 🌍

The converter supports over 170 currencies from around the world, including:
- **USD** (US Dollar)
- **EUR** (Euro)
- **GBP** (British Pound)
- **JPY** (Japanese Yen)
- **PHP** (Philippine Peso)
- **KRW** (South Korean Won)
- **CAD** (Canadian Dollar)
- **AUD** (Australian Dollar)
- **INR** (Indian Rupee)
- **CNY** (Chinese Yuan)

And many more!

## Technology Stack 🛠️

- **Python 3.12** - Core language
- **Click** - Command-line interface framework
- **Requests** - HTTP client for API calls
- **Rich** - Beautiful console output with color and tables

## API Information 📡

This converter uses the free tier of exchangerate-api.com, which provides:
- Free for personal use
- No API key required
- 1,500 requests per month
- Real-time exchange rates
- Easy to use REST API

## Project Structure 📁

```
currency-converter/
├── currency/
│   ├── __init__.py
│   └── __main__.py       # Main application logic
├── .python-version        # Python version specification
├── pyproject.toml         # Project dependencies
├── uv.lock                # Dependency lock file
└── README.md              # This file
```

## Contributing 🤝

Feel free to fork, improve, and create a pull request. Your contributions are always welcome!

## License 📄

MIT License - feel free to use this project for personal or commercial purposes.

## Acknowledgments 🙏

- exchangerate-api.com for providing free real-time exchange rate data
- Rich library for beautiful console output
- Click library for easy CLI creation
