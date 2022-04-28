## Heliumx Project

### For Context
HeliumX is the largest health care digital platform in the country. The platform provides healthcare services for its members. 
Some of its offering includes doctor-customer video sessions, hospital appointment bookings, weekly checkup calendar system, and a community that enjoys daily health care newsletters. 


### Features To Implement

### Community manager: 
- sends daily newsletters to the community members, 
- can view user details
- modify user details 
### Accountant: 
- view subscription details, 
- modify subscription details
### IT support:
- Manually book sessions
- confirm session bookings
- resolves support ticket 
### CEO:
- Can add new user 
- Modify user details 
- Delete user 
- Delete other admin 
- Add new admin 
- Assign role to admin 

### project setup locally
- Run `python3 -m venv venv` to create a virtual environment.

- Activate the virtual environment by running `source venv/bin/activate`.

- Check the requirements.txt file for the required packages.

- Run `pip install -r requirements.txt`.

- Run `python manage.py makemigrations`.

- Run `python manage.py migrate`.

- Run `python manage.py runserver`.

- Run `python manage.py createsuperuser` to create superuser to access django admin.

Heroku link: https://heliumx-api-project.herokuapp.com/

Heroku documentation link: https://heliumx-api-project.herokuapp.com/api/v1/docs

Heroku admin email: admin@admin.com, passwword: 1234
