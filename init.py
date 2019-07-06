import re
import csv


def exportTxtToCsv(txtFilePath, CSVFilePath):
    # List to store contacts to export
    contactList = []

    for line in open(txtFilePath, "r"):
        # List to store each contact
        contact = []

        # Find the index of the space between the name and the number
        index = re.search("\d", line).start()-1

        name = line[:index].capitalize()
        number = line[index:].strip()

        for i in range(0, 2):
            contact.append(name)

        for i in range(0, 27):
            contact.append('')

        contact.append("Mobile")
        contact.append(number)

        for i in range(0, 9):
            contact.append('')

        contactList.append(contact)

    # Append to template CSV
    for row in contactList:
        with open(CSVFilePath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
    csvFile.close()


if __name__ == "__main__":
    txtFilePath = ""
    CSVFilePath = ""
    exportTxtToCsv(txtFilePath, CSVFilePath)
