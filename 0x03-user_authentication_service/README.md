# 0x08. User authentication service

## Resources:books:
Read or watch:
* [Flask documentation](https://intranet.hbtn.io/rltoken/pmustxytL0mvk0Xo1X5A6g)
* [Requests module](https://intranet.hbtn.io/rltoken/YrhQSCpUMTZ-od0EAPANwg)
* [HTTP status codes](https://intranet.hbtn.io/rltoken/iWzNygULyRyOnkBPXDZrRw)

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. User model](./user.py)
* In this task you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy). 


### [1. create user](./db.py)
* In this task, you will complete the DB class provided below to implement the add_user method.


### [2. Find user](./db.py)
* In this task you will implement the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point.


### [3. update user](./db.py)
* In this task, you will implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.


### [4. Hash password](./auth.py)
* In this task you will define a _hash_password method that takes in a password string arguments and returns a string.


### [5. Register user](./auth.py)
* In this task, you will implement the Auth.register_user in the Auth class provided below:


### [6. Basic Flask app](./app.py)
* In this task, you will set up a basic Flask app.


### [7. Register user](./app.py)
* In this task, you will implement the end-point to register a user. Define a users function that implements the POST /users route.


### [8. Credentials validation](./auth.py)
* In this task, you will implement the Auth.valid_login method. It should expect email and password required arguments and return a boolean.


### [9. Generate UUIDs](./auth.py)
* In this task you will implement a _generate_uuid function in the auth module. The function should return a string representation of a new UUID. Use the uuid module.


### [10. Get session ID](./auth.py)
* In this task, you will implement the Auth.create_session method. It takes an email string argument and returns the session ID as a string.


### [11. Log in](./app.py)
* In this task, you will implement a login function to respond to the POST /sessions route.


### [12. Find user by session ID](./auth.py)
* In this task, you will implement the Auth.get_user_from_session_id method. It takes a single session_id string argument and returns a string or None.


### [13. Destroy session](./auth.py)
* In this task, you will implement Auth.destroy_session. The method takes a single user_id integer argument and returns None.


### [14. Log out](./app.py)
* In this task, you will implement a logout function to respond to the DELETE /sessions route.


### [15. User profile](./app.py)
* In this task, you will implement a profile function to respond to the GET /profile route.


### [16. Generate reset password token](./auth.py)
* In this task, you will implement the Auth.get_reset_password_token method. It take an email string argument and returns a string.


### [17. Get reset password token](./app.py)
* In this task, you will implement a get_reset_password_token function to respond to the POST /reset_password route.


### [18. Update password](./auth.py)
* In this task, you will implement the Auth.update_password method. It takes reset_token string argument and a password string argument and returns None.


### [19. Update password end-point](./app.py)
* In this task you will implement the update_password function in the app module to respond to the PUT /reset_password route.


### [20. End-to-end integration test](./main.py)
* Start your app. Open a new terminal window.

---

## Author
* **Joseph Mahiuha** - [Mahiuha](https://github.com/Mahiuha)
