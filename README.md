# Company Analyzer

A Python based tool that retrieves and analyzes company information using the **yfinance** library.

The project uses real world financial data to analyze companies across different countries and industries.

## Features

* Retrieve company information using Yahoo Finance
* Analyze companies from different countries and markets
* Retrieve:

  * Company name
  * Country
  * Industry sector
  * Market capitalization
  * Currency
* Convert market capitalization into USD
* Display market capitalization in USD billions
* Filter companies by **market capitalization**
* Filter companies by **country**
* Filter companies by **industry**
* Handle unavailable market capitalization data
* Support multiple global stock exchanges
* Display company data in a structured format

## Technologies Used

* Python
* yfinance
* PyInstaller
* Git & GitHub

## Data Source

Company and financial data is retrieved using **Yahoo Finance through the `yfinance` Python library**.

The project requires an internet connection to retrieve company and exchange rate data.

## Example

The analyzer can provide information such as:

| Company | Country | Sector            | Market Cap (USD Bn) |
| ------- | ------- | ----------------- | ------------------: |
| NVIDIA  | USA     | Technology        |              4,000+ |
| Apple   | USA     | Technology        |              4,000+ |
| SAP     | Germany | Technology        |                300+ |
| Toyota  | Japan   | Consumer Cyclical |                300+ |

*Market capitalization values change over time.*

## Project Structure

```text
Company-Analyzer/
│
├── Company_Analyzer.py
├── README.md
├── requirements.txt
└── dist/
    └── CompanyAnalyzer.exe
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Company-Analyzer.git
```

Move into the project directory:

```bash
cd Company-Analyzer
```

Install the required library:

```bash
pip install -r requirements.txt
```

## Running the Program

Run the Python program:

```bash
python Company_Analyzer.py
```

## Creating the Windows Executable

The project can be converted into a Windows `.exe` file using PyInstaller.

```bash
python -m PyInstaller --onefile --name CompanyAnalyzer Company_Analyzer.py
```

The executable will be created inside:

```text
dist/CompanyAnalyzer.exe
```

## What I Learned

This project helped me practice:

* Python variables and data types
* Lists and tuples
* Dictionaries
* Loops
* Conditional statements
* Functions
* Exception handling
* Working with external Python libraries
* Retrieving real world financial data
* Currency conversion
* Data filtering
* Output formatting


## Future Improvements

Potential improvements include:

* Add more financial metrics
* Add historical stock price analysis
* Add charts and visualizations
* Add CSV export
* Add a graphical user interface
* Improve error handling for unavailable data
* Add more advanced company comparison features

## Disclaimer

This project is intended for educational and programming purposes.

Financial data retrieved from external sources may be delayed, incomplete, or change over time. This project should not be used as a source for investment decisions.

## Author

**Kalpesh Baviskar**

Market Research & Technology Analyst

Interested in technology markets, semiconductors, IoT, connectivity, data analysis, and Python.
