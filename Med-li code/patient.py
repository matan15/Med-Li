from datetime import datetime

class ReminnderData:
    timeToTake= None
    amountToTake= 0
    boxNumber= 0
    took=False

class Reminder(object):
    def __init__(self, timeToTake: datetime, amountToTake: int, boxNumber: int):
        self.timeToTake = timeToTake
        self.amountToTake = amountToTake
        self.boxNumber = boxNumber
        self.took = False

    def __str__(self) -> str:
        return f"When to take: {self.timeToTake}\n" \
               f"Amount to take: {self.amountToTake}\n" \
               f"Box Number: {self.boxNumber}\n" \
               f"Do the patient took the medicine: {self.took}"

    def __dict__(self) -> dict:
        return {"timeToTake": self.timeToTake.strftime("%d/%m/%Y  %H:%M:%S"),
                "amountToTake": self.amountToTake,
                "boxNumber": self.boxNumber,
                "took": self.took
                }

    def getDataStracture(self):
        dataReminder= ReminnderData()
        dataReminder.timeToTake = self.timeToTake
        dataReminder.amountToTake = self.amountToTake
        dataReminder.boxNumber = self.boxNumber
        dataReminder.took = self.took
        return dataReminder



class Medicine(object):
    def __init__(self, medicineName, expirationDate: datetime, additionalDetails: str):
        self.medicineName = medicineName
        self.expirationDate = expirationDate
        self.additionalDetails = additionalDetails
        self.reminders = []

    def addReminder(self, timeToTake: datetime, amountToTake: int, boxNumber: int) -> None:
        reminder = Reminder(timeToTake=timeToTake, amountToTake=amountToTake, boxNumber=boxNumber)
        self.reminders.append(reminder)

    def __str__(self) -> str:
        if self.reminders:
            reminders = '\n\n'.join(
                [f'{i}. {str(reminder)}' for reminder, i in zip(self.reminders, range(1, len(self.reminders) + 1))])
        else:
            reminders = ''
        return f"Medicine name: {self.medicineName}\n" \
               f"expiration date: {self.expirationDate.month} / {self.expirationDate.year}\n" \
               f"Additional details: {self.additionalDetails}\n" \
               f"Reminders:\n" \
               f"{reminders}"


class Patient(object):
    def __init__(self, name: str, familyName: str, HMOName: str, age: int, location: str, restriction: str,
                 assistantName: str):
        self.name = name
        self.familyName = familyName
        self.HMOName = HMOName
        self.age = age
        self.location = location
        self.restriction = restriction
        self.assistantName = assistantName
        self.boxes = {}
        self.medicines = []

    def __str__(self):
        medicines = '\n\n'.join([f'{i}: {medicine}' for i, medicine in zip(range(1, len(self.medicines) + 1), self.medicines)]) if self.medicines else ''
        details = f"Name: {self.name}\n" \
                  f"Family name: {self.familyName}\n" \
                  f"HMO name: {self.HMOName}\n" \
                  f"Age: {self.age}\n" \
                  f"Location: {self.location}\n" \
                  f"Restriction: {self.restriction}\n" \
                  f"Assistant name: {self.assistantName}\n" \
                  f"Medicines:\n" \
                  f"{medicines}"
        return details

    def addMedicine(self, medicine: Medicine):
        self.medicines.append(medicine)


class Assistant(object):
    def __init__(self, name: str, phoneNumber: str, username: str, password: str, patient: Patient):
        self.name = name
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password
        self.patient = patient
