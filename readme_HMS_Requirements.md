**Hospital Management System (HMS)**

*Project Requirements*
# **Tech Stack**
- Python 3.x
- MySQL
- mysql-connector-python
# **Required Modules**
The application must include the following six modules. Each module must be implemented as a Python class with add, get\_all, get\_by\_id, update, and delete methods.

- Patient
- Department
- Doctor
- Appointment
- Treatment
- Billing
## **1. Patient Module**
- Add a new patient with name, age, gender, phone number, and address.
- View all patients.
- Search a patient by ID.
- Update patient details.
- Delete a patient record.
- Maintain Electronic Medical Records (EMR) — weight, height, blood pressure, pulse, allergies, previous medication, and other health issues.
## **2. Department Module**
- Add a new department with a unique department code.
- View, update, and delete departments.
- Prevent deletion if doctors are still assigned to the department.
## **3. Doctor Module**
- Add a doctor with name, department, specialization, and years of experience.
- View, update, and delete doctors.
- Manage doctor availability (Available / Unavailable).
- List doctors with their current availability and department name.
## **4. Appointment Module**
- Book an appointment for a patient with a specific doctor at a given time.
- Verify that the doctor is available before confirming the booking.
- View all appointments with patient and doctor names.
- Update appointment time and status (Scheduled, Completed, Cancelled, No-Show).
- Cancel and delete appointments.
## **5. Treatment Module**
- Record treatment details (type and cost) against an appointment.
- View all treatments or filter by appointment.
- Update or delete treatment entries.
## **6. Billing Module**
- Create a bill manually for an appointment.
- Auto-generate a bill by summing all treatment costs linked to the appointment.
- Track payment status (Pending, Paid, Refunded, Cancelled) and payment type (Cash, Card, UPI, Insurance, NetBanking).
- Update and delete bills.
# **7. Dashboard / Analytics**
The dashboard must run advanced SQL queries to provide the following insights:

- Summary numbers — total patients, doctors, departments, appointments, paid revenue, pending revenue.
- Top 5 doctors by total revenue.
- Patients per department with appointment counts.
- Monthly revenue trend (last 12 months).
- Pending payments with patient name and phone number.
- Most common treatments with average and total cost.
- Patient age-group distribution.
- Doctor utilization — completed vs cancelled appointments.
# **General Requirements**
- Centralize all database connection logic in a single class.
- Use parameterized queries (%s placeholders) — no string concatenation.
- Implement custom exception classes for database, validation, and not-found errors.
- Validate all user inputs (type, range, allowed values).
- Use a menu-driven CLI with a 'Back' option in submenus.
- Confirm before destructive operations (delete, cancel).
- Display tabular data in a clean, readable format.
- Never expose raw stack traces to the user.
# **Deliverables**
- Source code organized into a modular folder structure.
- SQL setup script for creating the database and tables.
- requirements.txt with Python dependencies.
- README with setup and usage instructions.
