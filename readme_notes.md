
touch patient department.py doctor.py appointment.py treatment.py billing.py


---

### Create
python3 -m venv myenv

**activate**  
myenv\Scripts\Activate.ps1
source myenv/bin/activate

**install**  
pip install -r requirements.txt

**requirements.txt format**  
`packagename=1.0.1 `

---

touch department_menu.py patient_menu.py doctor_menu.py appointment_menu.py treatment_menu.py billing_menu.py dashboard_menu.py




ALTER TABLE departments 
ADD CONSTRAINT UNIQUE (department_name),
ADD CONSTRAINT UNIQUE (department_code);

or 

ALTER TABLE departments ADD UNIQUE (department_name);
ALTER TABLE departments ADD UNIQUE (department_code);


describe departments;


Key Medical & Clinical DepartmentsEmergency/Casualty: Immediate treatment for acute injuries/illnessesCardiology: Heart-related issuesNeurology/Neurosurgery: Brain, nerve, and spinal cord conditionsOrthopedics: Bone, joint, and skeletal issuesObstetrics & Gynecology: Pregnancy, childbirth, and female reproductive healthPediatrics: Children and adolescent careGeneral Surgery: Operative proceduresOncology: Cancer diagnosis and treatmentENT: Ear, Nose, and Throat specialismsPsychiatry: Mental health servicesDermatology: Skin conditionsUrology: Urinary system and male reproductive healthGastroenterology: Digestive system disorders