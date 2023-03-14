import pickle
import time
from colorama import Fore
from patient import Assistant
from patient import Patient
from patient import Medicine
from datetime import datetime
from patient import Reminder
import sys
import calendar
import socket


def talkToServer(reminder: Reminder):
    HOST = '127.0.0.1'
    PORT = 65000
    # Create a socket connection.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Create an instance of ProcessData() to send to server.
    variable = reminder.getDataStracture()
    # Pickle the object and send it to the server
    data_string = pickle.dumps(variable)
    s.send(data_string)
    s.close()
    print('Data Sent to Server')


def main():
    patient = Patient(name="Nes", familyName="familyName", HMOName="Clalit", age=50, location="Ashdod",
                      restriction="Dementia", assistantName="Nir")

    assistant = Assistant(name="Nir", phoneNumber="0521111111", username="admin", password="123", patient=patient)

    print(Fore.LIGHTWHITE_EX + "Hello from Med-li\n")
    time.sleep(2)

    while True:
        print(Fore.LIGHTCYAN_EX + "Please log in to your account:")
        username = input(Fore.LIGHTCYAN_EX + "Enter your username: ")
        password = input(Fore.LIGHTCYAN_EX + "Enter your password: ")
        if assistant.username == username and assistant.password == password:
            print("")
            print(Fore.LIGHTGREEN_EX + f"You are now controlling {assistant.patient.name}")
            patient = assistant.patient
            while True:
                choice = int(input(Fore.LIGHTWHITE_EX + "Enter the number of the option you like to do (1-4):\n"
                                                        "1. Show patient details\n"
                                                        "2. Add medicine\n"
                                                        "3. Add reminder\n"
                                                        "4. exit\n"))
                if choice == 1:
                    print(patient)
                elif choice == 2:
                    medicine = Medicine(
                        medicineName=input(Fore.LIGHTWHITE_EX + "Enter the name of the medicine: "),
                        expirationDate=datetime(
                            day=1,
                            month=int(input(Fore.LIGHTWHITE_EX + "Enter the month of expiration date: ")),
                            year=int(input(Fore.LIGHTWHITE_EX + "Enter the year of expiration date: "))
                        ),
                        additionalDetails=input(Fore.LIGHTWHITE_EX + "Enter additional details: "))
                    patient.addMedicine(medicine)
                    print(Fore.LIGHTGREEN_EX + "The medicine added successfully!")
                elif choice == 3:
                    if patient.medicines:
                        print(Fore.LIGHTWHITE_EX + "Choose the number of the medicine that you want to add a reminder:")
                        if len(patient.medicines) == 1:
                            print(Fore.LIGHTWHITE_EX + f"1. {patient.medicines[0]}")
                        else:
                            for medicine, i in (patient.medicines, range(1, len(patient.medicines) + 1)):
                                print(Fore.LIGHTWHITE_EX + f"{i}. {medicine}")
                        index = int(input())
                        medicine = patient.medicines[index - 1]
                        print(calendar.month(datetime.now().year, datetime.now().month))
                        timeToTake = datetime(year=datetime.now().year,
                                              month=datetime.now().month,
                                              day=int(
                                                  input(Fore.LIGHTWHITE_EX + "Enter in which day the patient should "
                                                                             "take the medicine: ")),
                                              hour=int(
                                                  input(Fore.LIGHTWHITE_EX + "Enter in which hour the patient should "
                                                                             "take the medicine: ")),
                                              minute=int(input(
                                                  Fore.LIGHTWHITE_EX + "Enter in which minutes the patient should "
                                                                       "take the medicine: "))
                                              )
                        amountToTake = int(input(Fore.LIGHTWHITE_EX + "Enter how much medicines the patient should "
                                                                      "take in one time: "))
                        boxNumber = 0
                        while boxNumber > 5 or 1 > boxNumber:
                            boxNumber = int(input(Fore.LIGHTWHITE_EX + "Enter in which box will be the medicine: "))
                            if boxNumber > 5 or 1 > boxNumber:
                                print(
                                    Fore.LIGHTRED_EX + "The box number that you entered is wrong. Please enter number "
                                                       "from 1 to 5.")
                        medicine.addReminder(
                            timeToTake=timeToTake,
                            amountToTake=amountToTake,
                            boxNumber=boxNumber)
                        talkToServer(medicine.reminders[len(medicine.reminders) - 1])
                        patient.boxes[boxNumber] = medicine
                        print(Fore.LIGHTGREEN_EX + "The reminder added successfully!")
                    else:
                        print(
                            Fore.LIGHTRED_EX + "There is no medicines. First create a medicine to create a reminder "
                                               "to this medicine.")
                elif choice == 4:
                    print(Fore.LIGHTGREEN_EX + "You disconnected successfully!")
                    sys.exit()
                else:
                    print(Fore.LIGHTRED_EX + "You chose bad option. please try again!")
        else:
            print(Fore.LIGHTRED_EX + "The username or the password is incorrect! Try again.")


if __name__ == '__main__':
    main()
