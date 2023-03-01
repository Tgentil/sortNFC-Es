# XML Organizer

This script organizes XML files from NF-e (Brazilian Electronic Invoice) based on their payment type. The XML files are moved to different directories according to the payment type: `\example\folder\money` for cash payments and `\example\folder\outher` for card payments.

## Implementation

The script is implemented in Python and uses the following libraries:

- `shutil` for file manipulation
- `os` for directory listing
- `xml.etree.ElementTree` for parsing the XML files

The script works by reading each XML file in the specified directory, parsing it to obtain the payment type, and moving it to the appropriate directory. The directory paths can be configured by changing the `DIRECTORY` and `DESTINATION` constants in the script.

## Setup

1. Clone this repository or download the ZIP file.
2. Make sure you have Python 3 installed.
3. Install the required libraries by running `pip install -r requirements.txt` in the project directory.
4. Configure the `DIRECTORY` and `DESTINATION` constants in the script according to your needs.
5. Run the script with `python organize_xml.py`.

That's it! The XML files in the specified directory should now be organized according to their payment type.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
