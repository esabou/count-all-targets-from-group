# Snyk Organization Target Counter

## Description

This Python script interacts with the Snyk REST API to retrieve information about your Snyk organizations and the targets associated with them. It performs the following actions:

1.  **Retrieves a list of organizations** associated with your Snyk account using the Snyk API.
2.  **Prints the ID and name** of each organization.
3.  **Retrieves the targets** for each organization.
4.  **Prints the number of targets** for each organization.
5.  **Calculates and prints the total number of targets** across all organizations.

This script is useful for getting an overview of your Snyk setup, particularly the distribution of targets across your organizations.

## Prerequisites

Before running the script, ensure you have the following:

* **Python 3.6 or later** installed on your system.
* **A Snyk account** with an API token.
* **The `requests` library** installed. You can install it using pip:

    ```bash
    pip install requests
    ```

## Setup

1.  **Clone the repository** (or download the Python script) to your local machine.
2.  **Obtain your Snyk API token:**
    * Log in to your Snyk account at [https://app.snyk.io/](https://app.snyk.io/).
    * Go to **Settings** \> **Organization** \> **API**.
    * Copy your API token.
3.  **Configure the script:**
    * Open the Python script (`your_script_name.py`) in a text editor.
    * Replace the placeholder value for `SNYK_TOKEN` with your actual Snyk API token:

        ```python
        SNYK_TOKEN = "YOUR_SNYK_API_TOKEN"  # Replace with your token
        ```
    * (Optional) If you need to specify a Snyk API base URL or API version, modify the `BASE_URL` and `API_VERSION` variables accordingly.  The defaults should work for most users.

## Usage

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory** where you saved the Python script.
3.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your Python script (e.g., `snyk_target_counter.py`).

4.  **View the output:** The script will print the following information to the console:

    * A list of organizations with their IDs and names.
    * The number of targets for each organization.
    * The total number of targets across all organizations.

## Output Example


Organizations:
ID: 12345678-abcd-1234-efgh-1234567890ab, Name: My Organization 1
ID: 98765432-dcba-4321-hgfe-0987654321cd, Name: My Organization 2

Target Counts per Organization:
Organization: My Organization 1 (ID: 12345678-abcd-1234-efgh-1234567890ab) - Number of Targets: 15
Organization: My Organization 2 (ID: 98765432-dcba-4321-hgfe-0987654321cd) - Number of Targets: 25

Total Number of Targets Across All Organizations: 40


## Contributing

Feel free to contribute to this script by submitting pull requests or opening issues.

## License

This script is licensed under the [MIT License](LICENSE) (Add a LICENSE file if you have one).
