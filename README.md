# Contents
* [UX](#UX)
    * [Strategy](#Strategy)
       * [Project Goals](#Project-Goals)
       * [User Stories](#User-Stories) 
    * [Structure](#Structure)
       * [Existing Features](#Existing-Features) 
            * [Features on all pages](#Features-on-all-pages)
            * [Home Page Features](#Home-Page-Features)
            * [Login Page Features](#Login-Page-Features)
            * [Sign-Up Page Features](#Sign-Up-Page-Features)
            * [Profile Page Features](#Profile-Page-Features)
            * [Log Out Features](#Log-Out-Features)
            * [404 Page](#404-Page)
            * [500 Page](#500-Page)
            * [Features exclusive to Admin](#Features-exclusive-to-Admin)         
       * [Features Left To Implement](Feature-Left-To-Implement)  
       * [Design](#Design)
            * [Colors](#Colors)
            * [Typography](#Imagery)
            * [Imagery](#Imagery)    
    * [Skeleton](#Skeleton)
      * [Wireframes](#Wireframes)
      * [Database Schema](#Database-Schema)
      * [Sitemap](#Sitemap)
    * [Technolgies Used](#Technologies-Used)
    * [Testing](#Testing)
    * [Deployment](#Deployment)
      * [Deployment Steps](#Deployment-Steps) 
      * [Making a clone to run locally](#Making-a-clone-to-run-locally)
      * [How to Fork the respository](#How-to-Fork-the-Respository)
    * [Credits](#Credits)
      * [Media](#Media)
      * [Content](#Content)
      * [Code](#Code)
      * [Acknowledgements](#Acknowledgements)

# Joyce English School


![Website MockUp](documentation/doc_images/MS4-mockup.png)

The live website can be viewed [here](https://joyce-english-school.herokuapp.com/)


# UX

## Strategy

### Project Goals




**The Ideal User of this site:**
* Is English speaking.
* Has a passion for history. 
* Is Interested in local lore.
* Has a curiosity about their provincial area.
* Wants to learn more about Irish History. 
  

### User Stories

* As a first time user I want to know the site's purpose immediately upon arrival.
* As a first time user I want to access reviews of the school to inform my decision before signing up for a course.
* As a first time user I want the site UX to be intuitive for ease of use.
* As a first time user I want to find information about English language courses in the city of Trieste.
* As a user I want the site to be responsive across all devices.
* As a user I want to be able to create an account easily.
* As a user I want to be able to inform the school of my level of English easily.
* As a user I want to be able to pay for courses using a secure credit card payment system.
* As a returning user I want to be able to book lessons to suit my own schedule.
* As a returning user I want be able to contact the school easily for any further enquires I may have.
* As an existing user I want to receive school updates/news through my account. 
* As an existing user I want to be able to update my profile information and delete my account if I wish.

### User Stories - Admin Only
* As a site administrator I want to be able to create, update and delete course information/course options from the admin view. 
* As a site administrator I want to be able to create, update and delete the information on the Who we are page of the site from the admin view.  



# Structure

## Existing Features

### Features on all pages:
* Navbar
* Footer
* Social Media Icons

### Home page features:





### Login page features:



### Sign-Up page features:



### Profile page features:
 


### Logout features:
* The log out button removes the user's session cookie from the app using the pop method and redirects the user to the login page.

### 404 Page
* A 404 Page has been created in order to deal with user errors in navigation or invalid search data in order to assist the user in returning to the home page. All navigation features are present on the 404 page as well as a button labeled 'home' in order to easily redirect the user back to the relevant page.

<img src="assets/documentation/doc-images/404.png" width="450" height="250" alt="404-page">

### 500 Page 
* A 500 page has been created to deal with any potential internal server errors.

<img src="assets/documentation/doc-images/500.png" width="450" height="250" alt="500-page">

### Features exclusive to Admin:

* Only the Admin can edit/delete all articles content on the site, otherwise the content must belong to the session user in order for it to be edited or deleted. 
* Only Admin can add new topics to the topics page.
* Only Admin can edit/delete existing topics on the topics page.
* Only Admin can add new material to the further reading page.
* Only Admin can edit/delete material on the further reading page.


## Features left to implement






## Design

### Colors

* The colors of this site were chosen in order to replicate the feel of old newspapers and books. It's a simple black and white monochrome palette coupled with shades of grey so as not to overwhelm the user and to adhere to the principles of good UX design. They match the monochrome images that have been selected for this site. 

This palette was created on the [Coolors Website](https://coolors.co).

<img src="documentation/doc_images/MS4 Palette.png" width="450" height="250" alt="milestone palette">


### Typography
* The 'Metal Mania' font was chosen for header text because of its striking style and historical feel as well as it's clarity. Other fonts that were found were perhaps more fitting in terms of how frequently they were used in the past but in order to stick with the principles of good UX the aforementioned font was chosen based on its readability.


<img src="assets/documentation/doc-images/metalmania.png" width="350" height="150" alt="Metal-Mania">


* The 'IM Fell English SC' was chosen based on its similarity to the text often found in older literature in order to enhance the historic feel of the site and promote a positive user experience.


<img src="assets/documentation/doc-images/Englishfont.png" width="350" height="150" alt="English-font">


* Both fonts were found on [Google Fonts](https://fonts.google.com/)



### Imagery





## Skeleton

### Wireframes

* The wireframes were created using [Balsamiq wireframes](https://balsamiq.com/)

* The wireframe mockup links can be found below:

* [Home Page Wireframes](documentation/wireframes/MS4-home-wireframe.pdf)

* [Courses Page Wireframes](documentation/wireframes/MS4-courses-wireframe.pdf)

* [Contact Page Wireframes](documentation/wireframes/MS4-contact-wireframe.pdf)

* [Register Page Wireframes](documentation/wireframes/MS4-register-wireframe.pdf)

* [Profile Page Wireframes]()

* [Login Page Wireframes](documentation/wireframes/MS4-login-wireframe.pdf)

* [Who we are Page Wireframes](documentation/wireframes/MS4-who-we-are-wireframe.pdf)



### Database Schema

<img src="documentation/doc_images/dbschema.png" width="900" height="300" alt="database schema">

* A relational database was used to create this project. During production SQLite was used as the site's database and all data was migrated to Heroku Postgres during deployment to Heroku. The key models can be seen in the image above and are described in depth below:

#### Key Models 

**Courses** 
- This model alongside the exam_courses model are the foundation of the site's purpose. This model stores all relevant information about what each individual course offers.
- The price is stored in this model. 
- Each individual course contains it's own unique description and each course is referenced using a Primary Key which is generated each time a new course is created. 
- This model also stores information regarding course start and end dates and also the number of class hours that will be allocated for the duration of the course. 
- The assigned course images are also stored in this model. 

**Exam Courses**
- The exam_course model follows almost the exact same configuration as the course model aside from a few small differences.
- English exam courses require a specific level of English before a student can comfortably join a specific exam course. The `required_level` field informs the user of the necessary level of English needed for a particular exam course and the `certification_awarded` field informs the user of the certification they will be working towards should they chose to undertake a particular exam course.

**OrderLineItem**
- This model stores an instance of a course along with the `lineitem_total` which updates the price in the checkout. 

**Order**
- This model stores the information that is often expected to be found in an order, namely, the user, billing information, address information, the date of the transaction, the user's contact information and the `stripe_pid`.

**UserProfile**

- This model is created for each user when they register with the site. It stores the user's relevant profile information in the checkout form after their first purchase to allow for quicker and more convenient future purchases. 

- It is also connected to the allauth User model when a user registers with the site. 

- It connects with the `review_creator` field in the reviews model. 

**Reviews**
- This model allows the user to have their own CRUD functionality on the site. It connects to the UserProfile in the `review_creator` and allows the user to add their own reviews to the site by storing them in the database through the `comments` field of the model. It also stores the date of the review so that other users can tell how recent and relevant an individual review is. 


## Technologies Used
- This project is primarily built using HTML5 semantic markup, CSS stylesheets, Javascript, Python, Django, SQLite and Heroku Postgres.
- [Django](https://docs.djangoproject.com/en/3.1/)
    - Django was used as the main python framework in the building of this project.
- [jQuery](https://jquery.com/)
    - This framework was used to create some of the site's interactive functions.
- [Gitpod](https://gitpod.io)
    - This project was built using Gitpod as the IDE.
- [Github](https://github.com/)
    - Github was used for online version control and storing files and documents.
- [Heroku](https://id.heroku.com/)
    - Heroku was used as a cloud based platform to deploy this site.
- [Google fonts](https://fonts.google.com/) 
    - The font styles used on this website were chosen from Google fonts.
- [Materializecss](https://materializecss.com/)
   - Various aspects of this website were structured using Materialize.
   - Materialize was used to make this website responsive
- [Fontawesome](https://fontawesome.com/)
    - The icons used on this page were found in Fontawesome.
- [SQLite](https://www.sqlite.org/index.html)
    - SQLite was used as the database for the creation and development of this project.
- [Heroku Postgres](https://www.heroku.com/postgres)
    - Heroku was used as the database for this project in production mode after deployment to Heroku.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Jinja was used for templating.
- [Stripe](https://stripe.com/ie)
    - Stripe payments was used to build the card payment system of this site.
- [AWS-Amazon Web Services](https://aws.amazon.com/)
    - AWS was used to store all media and static files of this site in production mode.    
- [Balsamiq](https://balsamiq.com/)
    - The wireframes for this project were created using Balsamiq.
 - [Freeformatter- CSS beautifier](https://www.freeformatter.com/css-beautifier.html)
    - This was used to format the CSS stylesheet.
- [Freeformatter- HTML formatter](https://www.freeformatter.com/html-formatter.html)
    - This was used to format each HTML page
- [PEP8online](http://pep8online.com/)
    - PEP8 online was used to make sure all python code was pep8 compliant.
- [Google DevTools](https://developers.google.com/web/tools/chrome-devtools) 
    - Google Dev Tools was extensively used throughout the project for various styling and testing purposes. Its lighthouse feature was used as one of the main testing tools for this project.
- [EmailJS](https://www.emailjs.com/)
    - The contact-form was created using EmailJS following a code institute tutorial.
- [CSS-Tricks](https://css-tricks.com/)
    - This was used as a general reference resource.
- [Favicon.io](https://favicon.io/) 
    - This was used to create the site's favicon.
- [Am I Responsive](http://ami.responsivedesign.is/)
    - This was used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.
- [Beautifier.io](https://beautifier.io/)
    - Beautifier.io was used to format all javascript files in this project.
- [Dbdiagram.io](https://dbdiagram.io/home)
    - Dbdiagram.io was used to create the Database Schema presented in this document.
- [Coolors.co](https://coolors.co/)
    - Coolors.co was used to create the project's color palette.
- [StackOverflow](https://stackoverflow.com/)
    - Stack Overflow was used as a general reference resource. 

## Testing
Testing information can be found here in the separate [TESTING.md file](TESTING.md)

## Deployment
This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like MotherFolklore. The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institiue student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

This project was deployed using Heroku and stored in GitHub.

Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:
1. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

2. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

3. Push these files to GitHub.
Once those steps are done, the website can be deployed in Heroku using the steps listed below:

### Deployment Steps

1. Log into Heroku.
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.

### Set environment variables:

Navigate to the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (the name of the database that is being used for the project)
4. key: MONGO_URI, value:
 * This can be found in MongoDB by navigating  to the clusters section of your MongoDB account.
 * Click the cluster where the database is located.
 * Click the connect button.
 * Select the connect you application button.
 *  Copy the link provided to your application and ensure you have substituted the password and dbname with the correct values).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).


### Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.


### Connect app to Github Repository

1. Click the deploy tab and connect to GitHub.
2. Type the name of the repository into the search bar presented.
3. Click the Code dropdown button next to the green Gitpod button.
4. When the correct repository displays click the connect button.








---


## Credits

### Media
The image used to create the James Joyce favicon was originally obtained from [trybooking.com](https://www.trybooking.com/events/landing?eid=751940&)

Books.jpg https://unsplash.com/photos/IOzk8YKDhYg?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
flag.jpg Image by <a href="https://pixabay.com/photos/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1209605">Free-Photos</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1209605">Pixabay</a>

pages.jpg Image by <a href="https://pixabay.com/users/kranich17-11197573/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6213537">Kranich17</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6213537">Pixabay</a>

teenagers.jpg https://unsplash.com/photos/8nHQx4zi9Wk

children.jpg https://unsplash.com/photos/o_lLsdVTxak

business-class.jpg https://unsplash.com/photos/FDV1BaKNKEo

adults.jpg https://unsplash.com/photos/XkKCui44iM0

summer-camp.jpg https://www.pexels.com/photo/man-people-woman-weather-8033897/

questions.jpg https://pixabay.com/illustrations/ask-writing-who-what-how-why-2245264/

intensive-courses.jpg https://pixabay.com/photos/girl-english-dictionary-read-2771936/

exams.jpg https://unsplash.com/photos/s9CC2SKySJM
### Content


### Code



* The email.js code was sourced from Matt Rudge's Code Institute tutorial on the same subject.

* A large portion of this project's code was inspired by Chris Zielinski's Boutique Ado project walkthrough tutorial. This Code Institute tutorial was instrumental in the creation of this site. 

* The TESTING.md section of this project was inspired by my classmate, Daisy McGirr's, workshop on testing. This workshop proved very useful for a great deal of students, myself included, in approaching all matters of testing. 

### Acknowledgements

* I would firstly like to thank my ever-patient mentor, Aaron Sinnott, whose guidance, knowledge and calm advice has been integral to the creation, development and completion of this project. 

* I would like to thank the entire slack community for being a source of support, knowledge and positive feedback throughout this project, in particular data-centric-dev channel lead Ed B who seemed to be constantly available to answer questions and troubleshoot solutions with students throughout the development of their third milestone projects.

* I would like to thank Daisy McGirr for taking time out of her busy schedule to provide us with the aforementioned testing workshop and for constantly offering encouragement and help to our Springboard class throughout our Code Institute journey.

* I would like to thank my own Springboard class cohorts for being supportive and helpful throughout the duration of the course. This particular channel provided a great deal of respite and also necessary feedback throughout the course which has proven invaluable for maintaining motivation. 

* Finally I would like to thank my boyfriend Shane for constantly helping to test the project throughout its development, providing insightful suggestions as to how to improve user experience. And also for helping to proof read this document and ensure it meets the correct standards of grammar, spelling and readability.