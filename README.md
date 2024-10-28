A simple responsive library management system using Django and Bootstrap

Features:
- Create admin through the 'python manage.py createsuperuser' command and use it to log in as admin.
- Admin can log in and view available books that can be be borrowed, add books to be borrowed.
- Admin can  see a list of all registered students.
- Admin can issue a book to an existing student and view issued books, return deadline date and fine  
- Student can signup and login to view a list of available books, borrow books, check borrow status if they have been issued any books and fines incase the return deadline has passed.
- A student can also view their profile details, change the details and update it.
- A student can also change their password and save the update.



How to run the project:
- Install Python
- Create a virtual environment
- Download This Project Zip Folder and Extract it inside the virtual environment
- Open Terminal and Execute Following Commands :

``` python -m pip install -r requirements.txt ```
- Move to project folder in Terminal. Then run following Commands :

```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
Open your browser and launch it on http://127.0.0.1:8000/



OPEN TO THE 'SCREENSHOTS' FOLDER TO VIEW SCREENSHOTS OF THE PROJECT
