# Python Fuzz Testing with Atheris

## Overview
This project implements fuzz testing using [Atheris](https://github.com/google/atheris), a Python fuzzing engine. It is designed for security and reliability testing of Python functions, particularly in **software engineering research**.

## Features
- Automated fuzz testing for Python functions.
- Supports valid, edge, and invalid inputs.
- Comprehensive logging of crashes and unusual behavior.
- Detailed reporting in CSV format.
- Integration with GitHub Actions for CI/CD.

## Installation

Clone the repository and set up the virtual environment:

```bash
git clone https://github.com/biplabneupane/python-fuzz-tester.git
cd python-fuzz-tester
python3 -m venv fuzz_env
source fuzz_env/bin/activate
pip install -r requirements.txt
```

## Usage

To run the fuzz tests, execute the following command:

```bash
python -m fuzzing.fuzz
```

### Example Output

```text
📝 Testing valid input: 'Hello, world!'
✅ Processed successfully: 'Hello, world!'

📝 Testing edge input: ''
✅ Processed successfully: ''

📝 Testing invalid input: None
⚠️ Crash detected: 'None' - Error: Input must be a string
```

## Input Categories

1. **Valid Inputs:** Strings that conform to expected input formats.
2. **Edge Cases:** Empty strings, very long strings, special characters.
3. **Invalid Inputs:** Null values, incorrect data types.

## Logging and Reporting

The results of fuzz testing are logged in the `logs/fuzz_data.csv` file.

### CSV Format:

```
Timestamp,Input,Length,Crashed,Error_Message
2025-03-20T05:09:31.157428+00:00,../../etc/passwd,16,1,Potential Path Traversal detected
2025-03-21T05:25:50.671601+00:00,,0,0,None
```

- **Timestamp:** When the input was tested.
- **Input:** The exact string tested.
- **Length:** Length of the input.
- **Crashed:** 1 if the input caused a crash, 0 otherwise.
- **Error_Message:** Details of the error if a crash occurred.

## GitHub Actions (CI/CD)

To ensure continuous integration and automated testing, we use GitHub Actions. Add the following workflow file under `.github/workflows/fuzz_test.yml`:

```yaml
name: Fuzz Testing

on:
  push:
    branches:
      - main

jobs:
  fuzzing:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m venv fuzz_env
          source fuzz_env/bin/activate
          pip install -r requirements.txt

      - name: Run fuzz tests
        run: |
          python -m fuzzing.fuzz

      - name: Upload logs
        uses: actions/upload-artifact@v3
        with:
          name: fuzz_logs
          path: logs/fuzz_data.csv
```

## Contribution Guidelines

- **Pull Requests:** Create pull requests for new features or bug fixes.
- **Issue Reporting:** Use GitHub issues for reporting bugs or suggesting enhancements.
- **Code Standards:** Follow PEP8 for Python code.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

For questions or feedback, feel free to reach out to [Biplab Neupane](https://github.com/biplabneupane).

