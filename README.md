# CF Python Tools 🐍

A curated collection of professional Python tools featuring both command-line interfaces (CLI) and graphical user interfaces (GUI), built with modern development practices and beautiful designs.

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![UV Package Manager](https://img.shields.io/badge/uv-0.10.4-orange.svg)](https://github.com/astral-sh/uv)
[![Conda Environment](https://img.shields.io/badge/conda-supported-brightgreen.svg)](https://conda.io/)
[![Project Count](https://img.shields.io/badge/projects-2-yellow.svg)](README.md#-projects-overview)

## 🚀 Projects Overview

### 1. Currency Converter
A simple, beautiful, and fast CLI currency converter with real-time exchange rates from open.er-api.com.

[![View Project](https://img.shields.io/badge/view-project-orange.svg)](currency-converter/README.md)
[![PyPI](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](currency-converter/pyproject.toml)
[![Type: CLI](https://img.shields.io/badge/type-CLI-blueviolet.svg)](currency-converter/README.md)

- **Features**: Real-time rates, 170+ currencies, beautiful output, precise mode
- **Technology**: Python 3.12, Click, Requests, Rich
- **Usage**: `uv run currency <amount> <from> <to>`

### 2. Profit Estimator
A powerful CLI tool for calculating compound growth and profit estimates with support for various time periods and natural language parsing.

[![View Project](https://img.shields.io/badge/view-project-orange.svg)](profit-estimator/README.md)
[![PyPI](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](profit-estimator/pyproject.toml)
[![Type: CLI](https://img.shields.io/badge/type-CLI-blueviolet.svg)](profit-estimator/README.md)

- **Features**: Compound growth, natural language parsing, detailed breakdowns
- **Technology**: Python 3.12, Click
- **Usage**: `uv run python profit-estimator.py estimate --initial <amount> --gain <%> --period <type> --increments <number>`

## 📁 Project Categories

### 🖥️ Command-Line Tools (CLI)
Tools designed for terminal environments, offering fast, scriptable, and efficient workflows.

### 🖱️ Graphical Tools (GUI)
Coming soon! Tools with intuitive graphical interfaces for users who prefer visual interaction.

### 🌐 Web Applications
Future projects that run in web browsers, accessible from anywhere.

### 📱 Mobile Apps
Planned tools for iOS and Android platforms using Python frameworks like Kivy or BeeWare.

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.12+
- Conda (for environment management)
- UV 0.10.4+ (for package management)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cf-pyTools
   ```

2. **Create and activate the conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate cf-pyTools
   ```

3. **Install dependencies for each project**
   ```bash
   # For Currency Converter
   cd currency-converter
   uv sync
   source .venv/bin/activate
   
   # For Profit Estimator
   cd ../profit-estimator
   uv sync
   source .venv/bin/activate
   ```

## 📁 Repository Structure

```
cf-pyTools/
├── currency-converter/          # Real-time currency conversion tool (CLI)
│   ├── currency/               # Main application code
│   ├── README.md               # Project documentation
│   ├── pyproject.toml          # Project dependencies
│   └── uv.lock                 # Dependency lock file
├── profit-estimator/           # Compound growth calculator (CLI)
│   ├── profit-estimator.py     # Main application code
│   ├── README.md               # Project documentation
│   ├── pyproject.toml          # Project dependencies
│   └── uv.lock                 # Dependency lock file
├── environment.yml             # Conda environment configuration
└── README.md                   # This file
```

## 🎯 Usage Examples

### Currency Converter
```bash
# Convert 500 Philippine Pesos to US Dollars
uv run currency 500 PHP USD

# Convert 1200 US Dollars to Japanese Yen with precise mode
uv run currency 1200 USD JPY --precise

# List all supported currencies
uv run currency --list
```

### Profit Estimator
```bash
# Calculate growth of $1000 with 5% monthly gain for 12 months
uv run python profit-estimator.py estimate --initial 1000 --gain 5 --period monthly --increments 12

# Calculate growth of $2000 with 0.5% gain twice a day for 30 days
uv run python profit-estimator.py estimate --initial 2000 --gain 0.5 --period "twice a day" --increments 60
```

## 🛡️ Technology Stack

- **Language**: Python 3.12
- **Package Manager**: UV (Unified Version Control)
- **Environment Management**: Conda
- **CLI Framework**: Click
- **HTTP Client**: Requests
- **Console Output**: Rich
- **Natural Language Processing**: Regular Expressions
- **GUI Frameworks**: Planned (Tkinter, PyQt, Kivy)
- **Web Frameworks**: Planned (FastAPI, Flask, Django)

## 📈 Key Features

### Common Features
- **Professional Interfaces**: Beautiful CLI with Rich or modern GUI designs
- **Error Handling**: Robust input validation and error reporting
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Modern Development**: Built with Python 3.12 and best practices

### Currency Converter Specific
- Real-time exchange rates from exchangerate-api.com
- Support for 170+ global currencies
- Precise decimal places option
- Currency list lookup functionality
- API failure handling

### Profit Estimator Specific
- Compound growth calculations with detailed breakdowns
- Natural language period parsing (e.g., "twice a day")
- Effective annual rate calculations
- Period-by-period progression tracking
- Support for various time frequencies

## 🔧 Development

### Adding a New Project

1. Create a new directory
2. Initialize with UV: `uv init`
3. Create your Python files
4. Write a README.md for documentation
5. Add dependencies to pyproject.toml
6. Update this README with project information

### Updating Dependencies

```bash
cd <project-directory>
uv pip install <package-name>
uv sync
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- exchangerate-api.com for providing free real-time exchange rate data
- Rich library for beautiful console output
- Click library for easy CLI creation

## 📞 Contact

For questions, suggestions, or feedback, please open an issue or reach out directly.

---

Made with ❤️ using Python 3.12