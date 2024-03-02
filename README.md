
# Email Validation Script

## Overview
This Python script validates an email address based on certain criteria including length, format, and character restrictions.

## Usage
1. Run the script using Python:
   ```
   python email_validation.py
   ```
2. Enter an email address when prompted.
3. The script will validate the email according to the following criteria:
   - The email must be at least 6 characters long.
   - It must start with a letter.
   - It should contain only one "@" symbol.
   - The domain extension must be ".com" or ".org".
   - Spaces, uppercase letters, and certain special characters are not allowed.
4. The script will output one of the following messages:
   - "Correct email" if the email passes all validation criteria.
   - "Wrong input" if the email does not meet the specified criteria, along with additional messages indicating specific issues such as spaces, uppercase letters, or special characters.

## Important Notes
- Ensure that the input email address follows the specified format and criteria.
- This script provides basic email validation and may not cover all possible edge cases or international email formats.
- Customize the validation criteria or error messages according to your specific requirements.

## Author
Sadman Kabir
