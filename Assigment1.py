from datetime import datetime
from enum import Enum

# Enums to represent gender, nationality, Position(for the stuff), ShiftTiming(for the stuff), AssignedLocation(for the stuff), flight status, and special services.
class Gender(Enum):
    female = 1
    male = 2

class Nationality(Enum):
    UAE = 1
    Maldives = 2
    USA = 3
    Canada = 4
    China = 5

class Position(Enum):
    Pilot = 1
    FlightAttendant = 2
    GroundStaff = 3
    GateScanner = 4

class ShiftTiming(Enum):
    Morning = 1
    Afternoon = 2
    Evening = 3
    Night = 4

class AssignedLocation(Enum):
    AirportTerminal = 1
    ControlTower = 2
    Runway = 3

class FlightStatus(Enum):
    OnTime = 1
    Delayed = 2
    Cancelled = 3


class SpecialServices(Enum):
    Wheelchair = 1
    MealPreference = 2

# This is the main class that we would use information for both stuff and passenger. It includes contact information such as user name and email.
class Person:
    def __init__(self, first_name="", last_name="", date_of_birth="", gender=None, email_address="", phone_number=""):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.gender = gender
        self.email_address = email_address
        self.phone_number = phone_number

    def update_contact_information(self, email, phone):
        self.email_address = email
        self.phone_number = phone
        return True

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Person: {self.get_full_name()}, Email: {self.email_address}, Phone: {self.phone_number}"

# The Passenger class extends from the Person class with additional attributes (ex:nationality of thr passenger) and methods (ex:confirm_personal_information) related to air travel.
class Passenger(Person):
    def __init__(self, first_name="", last_name="", date_of_birth="", gender=None, email_address="", phone_number="", nationality=None, passport_number=""):
        super().__init__(first_name, last_name, date_of_birth, gender, email_address, phone_number)
        self.nationality = nationality
        self.passport_number = passport_number

    def confirm_personal_information(self):
        return True

    def request_boarding_pass(self):
        return True

    def request_boarding_pass_change(self):
        return True

    def provide_special_services_detail(self, service: SpecialServices):
        return True

    def __str__(self):
        return f"{super().__str__()}, Nationality: {self.nationality.name}, Passport: {self.passport_number}"

# # The staff class extends from the Person class with additional attributes (ex: staff_id and position) and methods (ex:process_new_booking)  related to air travel.
class Staff(Person):
    def __init__(self, first_name="", last_name="", date_of_birth="", gender=None, email_address="", phone_number="",
                 staff_id="", position=None, shift_timing=None, assigned_location=None):
        super().__init__(first_name, last_name, date_of_birth, gender, email_address, phone_number)

        self.staff_id = staff_id
        self.position = position
        self.shift_timing = shift_timing
        self.assigned_location = assigned_location

    def process_new_booking(self, passenger_details, flight_details):
        return True

    def modify_booking(self, booking_id, new_details):
        return True

    def cancel_booking(self, booking_id):
        return True

    def generate_boarding_pass(self, booking_id):
        return True

    def assign_seat(self, booking_id, seat_number):
        return True

    def handle_special_requests(self, booking_id, requests):
        return True

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Position: {self.position.name}, Shift Timing: {self.shift_timing.name}, " \
               f"Assigned Location: {self.assigned_location.name}, Full Name: {self.get_full_name()}, " \
               f"Email: {self.email_address}, Phone: {self.phone_number}"


# The Flight class represents a flight with its details (ex: flight number and arrival date) and methods (ex: update flight information) to manage.
#The flight infromation is connected to the passenger. Meaning the infromation we get in the output are what the passenger booked for for example, flight number and the arrival date.
class Flight:
    def __init__(self, flight_number="", arrival_date="", arrival_time="", flight_status=None, total_seats=0, special_services=None):
        self.flight_number = flight_number
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.flight_status = flight_status
        self.total_seats = total_seats
        self.special_services = special_services

    def update_flight_status(self, status: FlightStatus):
        self.flight_status = status
        return True

    def get_flight_information(self):
        return f"Flight {self.flight_number} arriving at {self.arrival_time} on {self.arrival_date}"

    def calculate_available_seats(self):
        return self.total_seats

    def set_flight_schedule(self, new_arrival_date, new_arrival_time):
        self.arrival_date = new_arrival_date
        self.arrival_time = new_arrival_time
        return True

    def __str__(self):
        return f"Flight Number: {self.flight_number}, Status: {self.flight_status.name}, Arrival: {self.arrival_date} {self.arrival_time}, Total Seats: {self.total_seats}, Special Services: {self.special_services.name if self.special_services else 'None'}"


# Example usage:
passenger = Passenger("Shatha", "Hassan", "2004-06-03", Gender.female, "shatha.hassan@example.com", "050-772-9609", Nationality.UAE, "123456789")
print(passenger)

flight = Flight("AB123", "2024-08-15", "10:00", FlightStatus.OnTime, 180, SpecialServices.MealPreference)
print(flight)

staff_member = Staff("Mariam", "Ahmed", "1985-04-22", Gender.female, "Mariam.Ahmed@example.com", "050-113-6789", "ST123", Position.GateScanner, ShiftTiming.Evening, AssignedLocation.AirportTerminal)
print(staff_member)