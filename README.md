BookSmart

My third milestone project is based on creating a site that will allow the user to record the books that they own and would like to buy.

UX 

User Stories

Below are user stories that were made so that I have a vision for my project:

As a user, I would like to store the books that I own on a online database.

As a user, I would like to store the books that I want to buy on a online database.

As a new user, I would like the site to be easy to use.

As a user, I would like to be able to add books with ease.

As a user, I would like to see the books that I have added.

As a user, I would like to be able to update any books or delete any books I have added.

Strategy
My plan for the site was to create an online system where the user can record the books they own and want to buy easily.

Scope
The site is to provide users who would like a online library to record the books they own and would like to buy by filling in a form with information on the book. The user is also able to delete any books they no longer own or would not like to buy anymore and edit information on the books they have added.

Structure
The main pages on the site is the my books and books to purchase section which will display the books that the users adds, when a book is added it will be displayed in a collapsible with edit and delete icons and the rating of the book the user gives to it. When the collapsible is clicked it will dropdown with the information on the book such as the author and the review from the user. When the users wants to add a book, he can just click on the add book links in the navbar which will take the user to the forms to add either a book they own or would like to buy. The add book forms will allow the user to fill in information about the book such as the title, author, year of release and genre, when the user adds a book they own they can also add a personal review and rating of the book in the form and if they are adding a book to purchase then instead in the form they can add why they want to buy the book and a link for the book to buy. When the edit icon is clicked, it will take the user to the same form as the add books form, but with the information already inputed and once the user has made the changes they want they can click update. When the delete icon is clicked in the collapsible it will bring up a modal which will confirm the deletion of the book.

Skeleton
Below are links to the wireframes for this project and are designed to include different versions for a desktop, tablet and mobile phone view.

add wireframes link here when inputed

Surface
The primary background color of site is dark blue which is in the header, footer and collapsible, but the navbar and sidenav background colour is light grey as I believe this offered the site a great balance. The color of all the text except for the forms is white and the font is Sriracha as it worked well with the page and the font is stylish but easily readable. There is a double border around the forms, which helps make it look like the book is a form.

Features

Existing Features

Materialize Navbar
The links in the navbar will allow the user to go to the page they require.

Materialize Side Nav
The sidenav will appear on smaller screens such as tablets and mobiles and when the links in the sidenav are clicked it will take you to the page you require.

Materialize Collapsible
The collapsible will display the book title, rating and function icons that the user will see and when clicked will expand and display the information about the book.

Edit Function Icon
This icon when clicked will take the user to the edit page for the book to make any changes and update.

Delete Function Icon
This icon when clicked will show the delete confirmation modal.

Delete Confirmation Modal
This modal will appear when the user clicks the delete icon, the user will need to confirm that he wants to delete the book.

Add Book Forms
These forms will allow the user to add books they own or want to buy.

Edit Forms
These forms will allow the user to change and edit the information they inputed.

Add To Library Button
This button will submit the add book forms and redirect back to either the My Books or Books to Purchase section depending on what form is submitted.

Update Button
This button will update the changes that are made from the edit forms and redirect back to either the My Books or Books to Purchase section depending on what form is submitted.

Footer Social Links
The links in the footer will allow the user to visit the site's social media platforms.

Features Left to Implement

Upload Image 
In future projects, I would like to add a upload a image button to allow the user to upload a image of the book.

Star Rating System
I would like to added a star rating system instead of a numbered one in future projects.

Technologies Used

These are the following languages, frameworks and libraries used in this project:

HTML
This was used to build the site and input content.

CSS
This was the second language used to style the site.

Python
This was the third language used to run the backend of the website and its functions

Jquery
This library was used to to allow the Materialize modal, collapsible, sidenav and tooltips to work.

Materialize
This framework was used to create a structure to the site and it was used to create the navbar, sidenav, collapsible and more.

Material icons
This icon library was used to place icons in my project such as the icons in the collapsible.

Font Awesome
This icon library was also used to place icons in my project such as the icons in the navbar and footer.

Google Fonts
This project was used to inlude the font 'Sriracha' in my project.

Flask Framework
This framework was used to build the site.

MongoDB
This database was used to store the information inputting in the site.

Testing

HTML Validator
The first error that the validator picked up was that the type attribute for the script tag was unnecessary. Another error that was picked up was that in the edit book form, the rating's label for attribute wasn't the same as the input id for rating. These were the only two errors picked up during HTML validation.

CSS Validator 
The validator found no issues with the file.

Python Checker https://extendsclass.com/python-tester.html
This website check the python code and found no syntax errors.