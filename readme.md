## Feedback Form Automation Script (NMIMS)

This script automates the process of logging into a website and filling out a feedback form. It uses the Playwright library to interact with web pages in a headless or headed browser environment.

Playwright allows us to automate browser actions like clicking buttons, filling forms, and navigating pages. This script is designed to handle forms with multiple pages and dynamic dropdown menus.

## Features

- Automated login to a specified website (**secure storage of credentials recommended, not in script!**).
- Dynamically fills out feedback forms based on dropdown IDs matching the pattern `answer<number>`.
- Allows selection of a specific value for each applicable dropdown (replace "5" with your desired value).
- Navigates through multiple pages of feedback forms automatically.

## Requirements

- Python 3.7 or higher
- Playwright library
- Firefox or Chrome browser installed

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/PrabirKalwani/feedback-form-automater.git
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   myenv\Scripts\activate     # On Windows
   ```

3. Install Playwright:

   ```bash
   pip install playwright
   playwright install
   ```

## Usage

1. Run the script:

   ```bash
   python feedback.py
   ```

2. The script will:
   - Log in to the website (**secure credentials!**).
   - Click on the necessary toggles and buttons.
   - You just have to click next on the new tab that opens up
   - Fill in all dropdowns with IDs starting with `answer` and select your chosen value for each.
   - Navigate through multiple pages of feedback forms.
