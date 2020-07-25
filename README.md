# BookSmart

### [Live App](https://ms3-booksmart.herokuapp.com/)

### My third milestone project is based on creating a app that will allow the user to record the books that they own and would like to buy.

## UX 

### User Stories

Below are user stories that were made so that I have a vision for my project:

As a new user, I would like the app to be easy to use.

As a user, I would like to store the books that I own and want to buy on a online database.

As a user, I would like to be able to add books with ease.

As a user, I would like to view the books that I have added.

As a user, I would like to be able to update any books or delete any books I have added.

#### Strategy
My plan for the app was to create an online system where the user can record the books they own and want to buy easily.

#### Scope
The site is to provide users who would like a online library to record the books they own and would like to buy by filling in a form with information on the book. The user is also able to delete any books they no longer own or would not like to buy anymore and edit information on the books they have added.

#### Structure
The main pages on the app is the 'My Books' and 'Wishlist' section which will display the books that the users adds, when a book is added it will be displayed in a collapsible with edit and delete icons and the rating of the book the user gives to it or in the wishlist section, the collapsible will have an link to buy icon instead. 
When the collapsible is clicked it will dropdown with the information on the book such as the author and the review from the user. When the users wants to add a book, he can just click on the add icon next to the secton heading in the library which will take the user to the forms to add either a book they own or would like to buy. The add book forms will allow the user to fill in information about the book such as the title, author, year of release and genre, when the user adds a book they own they can also add a personal review and rating of the book in the form and if they are adding a book to the 'Wishlist' section then instead in the form they can add why they want to buy the book and a link for the book to buy. 
When the edit icon is clicked, it will take the user to the same form as the add books form, but with the information already inputed and once the user has made the changes they want they can click update. When the delete icon is clicked in the collapsible it will bring up a modal which will confirm the deletion of the book.

#### Skeleton
Below are links to the wireframes for this project and are designed to include different versions for a desktop, tablet and mobile phone view.

##### Wireframes
##### [Desktop](https://github.com/WHusssain937/Milestone-Project-3/tree/master/wireframes/desktop)
##### [Tablet](https://github.com/WHusssain937/Milestone-Project-3/tree/master/wireframes/tablet)
##### [Mobile](https://github.com/WHusssain937/Milestone-Project-3/tree/master/wireframes/mobile)

#### Surface
The primary background color of app is dark blue which is in the header, footer and collapsible, but the navbar and sidenav background colour is light grey as I believe this offered the app a great balance. The color of all the text except for the forms is white and the font is Sriracha as it worked well with the page and the font is stylish but easily readable. There is a double border around the forms, which helps make it look like the book is a form.

## Features

### Existing Features

##### Materialize Navbar
The links in the navbar will allow the user to go to the page they require.

##### Materialize Side Nav
The sidenav will appear on smaller screens such as tablets and mobiles and when the links in the sidenav are clicked it will take you to the page you require.

##### Materialize Collapsible
The collapsible will display the book title, rating and function icons that the user will see and when clicked will expand and display the information about the book.

##### Add Function Icon
This icon when clicked will take the user to the add book pages depending on which section of the library they are on.

##### Edit Function Icon
This icon when clicked will take the user to the edit page for the book to make any changes and update.

##### Delete Function Icon
This icon when clicked will show the delete confirmation modal.

##### Delete Confirmation Modal
This modal will appear when the user clicks the delete icon, the user will need to confirm that he wants to delete the book.

##### Add Book Forms
These forms will allow the user to add books they own or want to buy.

##### Edit Forms
These forms will allow the user to change and edit the information they inputed.

##### Add To Library Button
This button will submit the add book forms and redirect back to either the My Books or Books to Purchase section depending on what form is submitted.

##### Update Button
This button will update the changes that are made from the edit forms and redirect back to either the My Books or Books to Purchase section depending on what form is submitted.

##### Footer Social Links
The links in the footer will allow the user to visit the app's social media platforms.

#### Features Left to Implement

##### Upload Image 
In future projects, I would like to add a upload a image button to allow the user to upload a image of the book.

##### Star Rating System
I would like to added a star rating system instead of a numbered one in future projects.

## Technologies Used

These are the following languages, frameworks and libraries used in this project:

##### HTML
This was used to build the app and input content.

##### CSS
This was the second language used to style the app.

##### [Python](https://www.python.org/)
This was the third language used to run the backend of the app and its functions

##### [Jquery](https://jquery.com/)
This library was used to to allow the Materialize modal, collapsible, sidenav and tooltips to work.

##### [Materialize](http://archives.materializecss.com/0.100.2/)
This framework was used to create a structure to the app and it was used to create the navbar, sidenav, collapsible and more.

##### [Material icons](https://material.io/resources/icons/?style=baseline)
This icon library was used to place icons in my project such as the icons in the collapsible.

##### [Font Awesome](https://fontawesome.com/)
This icon library was also used to place icons in my project such as the icons in the navbar and footer.

##### [Google Fonts](https://fonts.google.com/)
This project was used to inlude the font 'Sriracha' in my project.

##### [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/)
This framework was used to build the app.

##### [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
Templates with Flask were created using Jinja.

##### [MongoDB](https://www.mongodb.com/)
This database was used to store the information inputting in the app.

##### [Heroku](https://www.heroku.com/)
The app is hosted on Heroku.

## Information Architecture

#### Database 
I have chosen MongoDB Atlas as the database as it is required for this project. The data that will be stored in MongoDB will be stored in strings, in future projects I would like to experiment with other data like booleans and datetime.

#### Collections Data Structure
There are two collections which I have used for this project, the first one is called books where the information from the my books section will be stored and the second one is called purchases where the information from the wishlist section will be stored.

#### Books Collection
| Title         | Key in MongoDB  | Form Validation Type | Data Type |
| ------------- |:---------------:|:--------------------:| ---------:|
| Book Title    | book_title      | text                 | string    |
| Author        | author          | text                 | string    |
| Year Released | year_of_release | number               | string    |
| Genre         | genre           | text                 | string    |
| Book Review   | book_review     | text                 | string    |
| Rating        | rating          | number               | string    |

#### Purchases Collection
| Title                      | Key in MongoDB | Form Validation Type| Data Type|
| -------------------------- |:--------------:|:-------------------:| --------:|
| Book Title                 | purchase_title | text                | string   |
| Author                     | name_of_author | text                | string   |
| Year Released              | release_year   | number              | string   |
| Genre                      | purchase_genre | text                | string   |
| Why Do You Want This Book? | why_buy        | text                | string   |
| Link To Buy                | purchase_link  | text                | string   |

## Testing

##### [HTML Validator](https://validator.w3.org/)
The first error that the validator picked up was that the type attribute for the script tag was unnecessary. Another error that was picked up was that in the edit book form, the rating's label for attribute wasn't the same as the input id for rating. These were the only two errors picked up during HTML validation.

##### [CSS Validator](https://jigsaw.w3.org/css-validator/) 
The validator found no issues with the file.

##### [Python Checker](https://extendsclass.com/python-tester.html)
This website check the python code and found no syntax errors. 

### Testing For User Stories Objectives

##### I would like the site to be easy to use.
The site is quite simple and straight forward. There are two links in the navbar for the two main sections. The add, edit and delete icons are easy to understand and use. An issue I had during testing was the feedback I had from my mentor and friends who tested the website, they found that the navbar was confusing with explanation and couldn't understand between 'My Books' and 'Books to Purchase'. To rectify this, I have replaced the name 'Books to Purchase' with 'Wishlist' and have made the necessary changes with the add form and edit form for this section as well. I have removed the add links in the navbar and placed add icons next to the page headings for the sections which will link to the add forms. This has simplifed the site and made it easy to use.  

##### I would like to store the books that I own and want to buy on a online database.
The books are listed in a library and stored in two sections called 'My Books' and 'Wishlist' depending on if the user owns the book or wants to buy, the user can add as many books as they would like.

##### I would like to view the books that I have added.
Each book was stored separately in a collapsible in both the 'My Books' and 'Wishlist' sections. The header in the collapsible in the 'My Books' section, will have the book title, rating and the edit and delete icons for the book and when the collapsible is clicked, the information of the book will appear. The collapsible in the 'Wishlist' section will the same to the 'My Books' section except that in the header there will be no ratings and a third function icon link to buy will be present.

##### Add Book Form
* Click on add book link and it will go to add book form for the 'My Books' section.
* First, I will type in the book title and click the form submit button and as expected the form doesn't submit as the other required fields haven't been filled in.
* Then, I also filled in the author field as well and also as expected the form didnt't submit.
* Then, I filled in the third field box also which is the year the book was released and the form as expected didn't submit.
* Then, I also filled in the fourth field box, the genre of the book and as expected the form didnt't submit.
* Then, I filled in the book review field and submitted the form and as expected the form didnt submit.
* I then filled in the last field, the rating of the book. The rating must be between zero to five so when I put in the number seven the form doesn't submit as expected as the number needs to be five or below.
* When I put three in the ratings field and submit the form, as expected it submits.
* The form then returns to the 'My Books' section with the book listed. 

##### Add to Wishlist Form
* Click on add to wishlist and it will go to the add to wishlist form for 'Wishlist' section.
* First, I will type in the book title and click the form submit button and as expected the form doesn't submit as the other required fields haven't been filled in.
* Then, I also filled in the author field as well and also as expected the form didnt't submit.
* Then, I filled in the third field box also which is the year the book was released and the form as expected didn't submit.
* Then, I also filled in the fourth field box, the genre of the book and as expected the form didnt't submit.
* Then, I filled in the field for the reason why to buy the book and submitted the form and as expected the form didnt submit.
* I then filled in the last field, the link to purchase the book and submitted the from and as expected the form submitted.
* The form then returns to the 'Wishlist' section with the book listed. 

##### Edit Book/Wishlist Entry
* When I want to edit a book entry in either the 'My Books' and 'Wishlist' section, I need to click on the edit icon in the collapsible and it will take me to the edit page.
* First, I will click on the edit icon in the 'My Books' section and it will take me to the edit book entry page.
* Then I will change the genre from Novel to Fiction and submit the form and as expected it returns to the 'My Books' section.
* I can view my change and see that it has been a success.
* This will be the same experience for a edit wishlist entry. 

##### Delete Book/Wishlist Entry
* When I want to delete a book entry in either the 'My Books' and 'Wishlist' section, I need to click on the delete icon in the collapsible and it will open a confirmation modal.
* First, I will click on the delete icon in the 'Wishlist' section and it will open the confirmation modal.
* I will then be present with two options yes or no, I will select no, the modal will close as expected.
* Then, I will again click on the delete icon and this time select yes and the modal will close.
* I can now see that the book entry has been deleted
* This will be the same experience as the deleting a my book entry. 

#### Websites & Devices Testing
This site was tested on different devices such as a large desktop screen, laptop, Samsung S10+, Iphone 6/7/8, Ipad Pro and Ipad and on multiple web browsers such as Google Chrome and Firefox to make sure that it was responsive and compatible. I also had my friends and family tests it on their phones and laptops and it was responsive. One issue I had during testing was that on a mobile screen the collapsible header was not responsive due to too much text, I resolved this by getting a materialize helper to hide the rating of the book in the header on small screen, the user can still find the rating when he clicks on the collapsible in the body.

## Deployment
This app is hosted by GitHub Pages, it is directly deployed via the master branch and it was used for version control and commits and then pushed to a repository in Github.

#### Run Locally
To run locally, You can clone this respository directly in the terminal of the environment you are using for code editing type: git clone Booksmart https://github.com/WHusssain937/Milestone-Project-3. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

#### Creating a Environment Variable
You will need to create a environment variable to protect your MongoDB username and password. 

**These are the following steps to create a environment variable:**
1. First, you will need to create a env.py file so type the following command in the terminal: touch env.py.
2. Then, you will need to create a .gitignore file if you dont already have one, the command to type in the terminal: echo env.py > .gitignore.
3. In the env.py file you will need to set a environment variable as follows:
  * import os.
  * os.environ['MONGO_DBNAME'] = 'Your MongoDB Name'.
  * os.environ['MONGO_URI'] = 'Your Mongo String Here'.
4. You will then need to go to your app.py file and call your environment variable as follows:
  * Type, import os
  * from os import path
  * if path.exists('env.py'):
  * import env
  * app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
  * app.config['MONGO_DBNAME'] = os.environ.get('MONGODB_NAME')

#### Deploying to Heroku 
The app is currently being deployed on Heroku using the master branch on Github.

**These are the steps that were taken to deploy to Heroku:**
1. A requirements.txt file was created so that Heroku could install the necessary dependencies to run the app. The command used to create the file: **pip3 freeze --local > requirements.txt**.
2. A Procfile also was created so that Heroku could tell what kind of application it is deploying and how to run. The command used to create the file: **echo web: python run.py > Procfile**.
3. You will then need to create a free [Heroku](https://www.heroku.com/) account.
4. Create a new app for the project, selecting a name for the app and also choosing the closest region.
5. Then you will need to go into the Deploy tab in the app and choose a deployment method. I chose Heroku Git, using Heroku CLI and logged in via the gitpod terminal using the following command: **heroku login**.
6. Once logged in the terminal, commit the changes using the following commands: **git add and git commit -m "commit message here"**.
7. Then you will need to push the changes to heroku using the following command: **git push heroku master**.

8. Return back to app dashboard in Heroku and go to settings and scroll down until you find Reveal Config Vars and put in the following values.

| Key       | Values                      |
| --------- |:---------------------------:|
| IP        | 0.0.0.0                     |
| PORT      | 5000                        | 
| MONGO_URI | link to your Mongo DB       |

9. Click on Open App in Heroku and if all steps have been followed the app will open.

## Credits

### Content
 * The content on the app was written by myself.
 * [Materialize](http://archives.materializecss.com/0.100.2/)

### Acknowledgements
Mentor Dick Vlaanderen was very helpful with troubleshooting issues.

###### This is for educational use
