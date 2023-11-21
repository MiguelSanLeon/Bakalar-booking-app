# BAKALAR-BOOKING-APP

## Introduction:

This web application is a booking system for a restaurant, created with django and bootstrap. This project uses CRUD functionality to give users the options to create, read, update and delete their bookings, also including a small menu section and a contact section where the user can find information of interest about the restaurant.

![BAKALAR-BOOKING-APP mock up images](documentation_assets/index-page.png)

Visit the deployed website [here](https://bakalar-booking-app-f4bee72469cb.herokuapp.com/).

## Table of Contents

- [BAKALAR-BOOKING-APP](#bakalar-booking-app)
  - [Introduction:](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Strategy Table](#strategy-table)
  - [Scope](#scope)
    - [Phase 1](#phase-1)
    - [Phase 2](#phase-2)
  - [Structure](#structure)
    - [Database model](#database-model)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [General](#general)
    - [Home Page](#home-page)
    - [Register Page](#register-page)
    - [Edit User Page](#edit-user-page)
    - [Login and Logout](#login-and-logout)
    - [Menu page](#menu-page)
    - [Booking Page](#booking-page)
    - [Check Your Bookings Page](#check-your-bookings-page)
    - [Edit Bookings](#edit-bookings)
    - [Contact Us](#contact-us)
    - [Forbidden Page](#forbidden-page)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
  - [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Accessibility](#accessibility)
    - [Tools Testing](#tools-testing)
    - [Manual Testing](#manual-testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

We all have booked a table at a restaurant at some point and being able to do so through a web service should not be an unpleasant experience. For this reason, my project aims to give the user a clear vision of the options available at all times, trying to offer the most complete service possible when booking a table.

### Project Goals

- Responsive design to make the website accessible on different screen sizes.
- Well structured website and easy to navigate.
- Provide security in access to user data and their bookings.
- Allows CRUD functionality for bookings.

### User Stories

Throughout the project I used the GitHub projects board to log all user stories. I used an AGILE perspective to manage the user stories inside my github project. 

![github-project-board](documentation_assets/github-project-board.png)

- USER STORIE 1: As a Admin I can manage the bookings so that I can all the data provided by the user and accept the bookings.
- USER STORIE 2: As a User I can select time, date, number of guests and add comments to my booking so that I describe my booking details properly.
- USER STORIE 3: As a User I can edit my booking so that I can change the date, time, number of guests or add a comment.
- USER STORIE 4: As a User I can delete my booking from the website so that I can cancel it.
- USER STORIE 5: As a User I can view my booking so that I can check my booking details and status.
- USER STORIE 6: As a User I can book a table in the website so that I don't need to call the restaurant for a booking.
- USER STORIE 7: As a User I can see the correct restaurant address so that I could find the exact location of the restaurant, the better route and the estimated time of arrival.
- USER STORIE 8: As a User I can navigate to contact page so that I can have the restaurant address and contact details.
- USER STORIE 9: As a User I can see the restaurant menu so that I can decide to book a table or not.
- USER STORIE 10: As a User I can create a user profile so that I can login to book a table.
- USER STORIE 11: As a user I can edit my user profile so that I can update my data on the website.
  
### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Responsive design | 5 | 5
Display restaurant Menu | 5 | 5
Account registration | 5 | 5
User profile | 5 | 5
Create a booking | 5 | 5
Update a booking | 5 | 5
Cancel a booking | 4 | 4
Contact form | 3 | 4
Avoid double bookings | 4 | 1
Booking acceptance email | 3 | 1

Total | 44 | 40

[Go to the top](#table-of-contents)

## Scope

 As all features can't be implemented in the first release of the project, the project will be divided in two phases. The first phase will include the features that have been identified in order to build the minimum viable product.

### Phase 1

* Responsive design 
* Account registration
* User profile
* Display restaurant Menu
* Create a booking
* Update a booking
* Cancel a booking

### Phase 2

* Contact form
* Avoid double bookings
* Booking acceptance email
* Account email verification
* Social media signup

[Go to the top](#table-of-contents)

## Structure

### Database model

This is the database scheme first model:
![Db-model](documentation_assets/db-model.png)

And this is the final database structure:
![Models](documentation_assets/models.png)

### Colour Scheme

I decided to use a gradient background from [Uigradients](https://uigradients.com/)
![Colour Scheme](documentation_assets/colour-palette.png)

### Typography

I chose 2 fonts for this project, Baskerville and Bebas Neue with sans serif as fallback font for both.

![baskervville](documentation_assets/baskervville.png)
![bebasneue](documentation_assets/bebasneue.png)

This fonts can be found [here](https://fonts.google.com/)

### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to create all the wireframes for desktop and mobile views for this project.

Page | Desktop Version | Mobile Version
--- | --- | ---
Landing page/user logout | ![desktop-index-logout-wireframe](documentation_assets/d-index-logout-wf.png) | ![Mobile-index-logout-wireframe](documentation_assets/m-index-logout-wf.png)
Landing page/ user login | ![desktop-index-login-wireframe](documentation_assets/d-index-login-wf.png) | ![Mobile-index-login-wireframe](documentation_assets/m-index-logout-wf.png)
Sign up page | ![desktop-signup-wireframe](documentation_assets/d-signup-wf.png) | ![mobile-signup-wireframe](documentation_assets/m-signup-wf.png)
Menu page | ![desktop-menu-wireframe](documentation_assets/d-menu-wf.png) | ![mobile-menu-wireframe](documentation_assets/m-menu-wf.png)
Sign in page | ![desktop-signin-wireframe](documentation_assets/d-signin-wf.png) | ![mobile-signin-wireframe](documentation_assets/m-signin-wf.png)
Sign out page | ![desktop-signout-wireframe](documentation_assets/d-signuot-wf.png) | ![mobile-signout-wireframe](documentation_assets/m-signout-wf.png)
Contact page | ![desktop-contact-wireframe](documentation_assets/d-contact-wf.png) | ![mobile-contact-wireframe](documentation_assets/m-contact-wf.png)
Booking page | ![desktop-booking-wireframe](documentation_assets/d-booking-wf.png) | ![mobile-booking-wireframe](documentation_assets/m-booking-wf.png)
Booking Preview page | ![desktop-booking-preview-wireframe](documentation_assets/d-booking-preview-wf.png) | ![mobile-booking-preview-wireframe](documentation_assets/m-booking-preview-wf.png)
Check Booking page | ![desktop-check-bookings-wireframe](documentation_assets/d-check-bookings-wf.png) | ![mobile-check-bookings-wireframe](documentation_assets/m-check-bookings-wf.png)
Edit Booking page | ![desktop-edit-booking-wireframe](documentation_assets/d-edit-booking-wf.png) | ![mobile-edit-booking-wireframe](documentation_assets/m-edit-booking-wf.png)
Edit User Profile page | ![desktop-edit-user-profile-wireframe](documentation_assets/d-edit-user-profile-wf.png) | ![mobile-edit-user-profile-wireframe](documentation_assets/m-edit-user-profile-wf.png)

[Go to the top](#table-of-contents)

## Features

### General

This web application has been designed with bootstrap5 to be responsive across all devices.

* Navigation bar:
  - Navigation bar when there's no user logged in:
![Navbar-logout-image](documentation_assets/navbar-logout-image.png)
  - Navigation bar when there's a user logged in:
![Navbar-login-image](documentation_assets/navbar-login-image.png)
  - The navigation bar contains links to all the sections and  has a hover effect that changes color to provide feedback to the Site User for a better user experience. It also shows the active page highlighting the page name in yellow.

* Footer:
  - Footer image:
![Footer-image](documentation_assets/footer-image.png)
  - The footer contains a link (location) to contact page where the user can find a map, the restaurant address, an email and the phone number.
  - The footer contains links to social media channels.

### Home Page

![home-page-image](documentation_assets/index-page.png)

- The home page displays a title on top of a main image
- Under the main image the user can find a menu button and a booking button when not logged in.

![home-page-login-image](documentation_assets/index-page-login.png)

- When the user is logged in and has some bookings already the index page displays a third button named "check your bookings".

### Register Page

![register-page-image](documentation_assets/register-image.png)

- This is a customized register form. First name, last name and phone number has been added to the original django registration form.
- The user name has to be unique as it is the primary key
- The email is the only optional field.
- The phone number needs to contain 11 digits
- Password1 and Password2 must match.
- The password need to contain letters and numbers and cannot be a very used password.
- All error messages will be posted in the form  to provide a correct feedback to the user in case something went wrong during the registration process.
- When the process is finished the User will receive a succesfull message.

![register-page-error-messages-image](documentation_assets/register-error-messages-image.png)

### Edit User Page

![edit-user-profile-image](documentation_assets/edit-user-profile-image.png)

- The Edit User Profile Page cotains the three input fields that corresponds to the personal contact data from user profile.
- The phone number needs to be 11 digits long, and the form also provides error messages when an error occurs.
- When the process is finished the User will receive a succesfull message.

### Login and Logout

![login-image](documentation_assets/login-image.png)

- The login page it's a simple login form where the user has to provide the Username and the password.
- The page displays a welcome message indicating the user that to make a booking they need to signup first in case the user don't have an account.
- Wrong credentials will trigger error messages to be displayed.
- When the process is finished the User will receive a succesfull message.

![logout-image](documentation_assets/logout-image.png)

- This page only ask the user if the are sure to logout and the button to proceed.
- When the process is finished the User will receive a succesfull message.

### Menu page

![menu-image](documentation_assets/menu-image.png)

- The menu page contains a carousel whit a group of images that shows the different dishes in the menu with an arrow system to navigate through it.
- Each image contains the name of the dish and a brief description.

### Booking Page

![booking-page-image](documentation_assets/booking-page-image.png)

- The booking page show a booking form that contains 4 fields.

  1- The booking date field is required and must be a the present day or a future date. It has a calendar widget that can be use to pick the date.
  2- The booking time field is also required and must be between 14:00 and 22:00

### Check Your Bookings Page

### Edit Bookings

### Contact Us

### Forbidden Page

[Go to the top](#table-of-contents)

## Technologies Used

### Languages Used

### Frameworks, Libraries and Programs Used

[Go to the top](#table-of-contents)

## Testing

### Testing User Stories

### Code Validation

### Accessibility

### Tools Testing

### Manual Testing

[Go to the top](#table-of-contents)

## Deployment

[Go to the top](#table-of-contents)

## Credits

### Content

### Media

### Code

[Go to the top](#table-of-contents)

## Acknowledgements

[Go to the top](#table-of-contents)
