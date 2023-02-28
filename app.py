"""
Script that organizes NFC-Es 4.00 XML files based on the payment method used.

Files are moved to specific folders depending on the payment method specified in the XML file.

"""

import shutil
import os
import xml.etree.ElementTree as ET

# Specifies the directory where the XML files are located
DIRECTORY = r"C:\Users\example\input\folder"

# Loop through the files in the directory
for filename in os.listdir(DIRECTORY):
    if filename.endswith('.xml'):  # Check if it is an XML file
        # Get the full path of the file
        file_path = os.path.join(DIRECTORY, filename)

        # Read the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Get the name of the file
        file_name = 'NFe' + \
            root.find(
                ".//{http://www.portalfiscal.inf.br/nfe}nNF").text + '.xml'

        # Check the value of the tPag element to determine the destination folder
        if root.find(".//{http://www.portalfiscal.inf.br/nfe}tPag").text == '01':
            DESTINATION = r"C:\Users\example\folder\money"
        else:
            DESTINATION = r"C:\Users\example\folder\outher"

        # Move the file to the correct destination folder
        shutil.move(file_path, os.path.join(DESTINATION, file_name))
