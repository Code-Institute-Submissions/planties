# Planties

Welcome to my fourth website!

This website was built as a **development milestone project** for the completion of the **Full-Stack Frameworks With Django** module and it's part of the learning material for [Code Institute's](https://codeinstitute.net/about-us/) Fullstack Web Developer program.

A live **desktop demo** can be found [here](https://planties.herokuapp.com/).

The **source code** for this project can be found [here](https://github.com/gaspar91/planties).


# Table of Contents

- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structute](#Structute)
    - [Skeleton](#Skeleton)
- [User Stories](#user-stories)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Observations](#observations)
- [Deployment](#deployment)
- [Credits](#credits)


# UX

## Strategy

This website was built to be an e-commerce plant shop for users to purchase, feel inspired and share their love for plants.

The website offers users the opportunity to purchase different kinds of plants and flowers, including a section with flowers for special occasions.

It also includes a blog with posts with different kinds of topics about plants.


## Scope

To comprehend what highlights should be incorporated, I perused the web for other comparable sites. 
I had a reasonable thought regarding what should be incorporated from my side yet I needed to view at it from a customer's viewpoint too.
For this, I did a brisk research as a costumer to comprehend what I would find interesting and catch my attention.
In light of this, I recognized these key points:

  1. An outwardly engaging **Home Page** which gives a quick look at what the store is selling.
    
  2. An **About** page to give some comprehension about what the store's objective.

  3. A **Product** page to exhibit all the products available.

  4. A **Special Occasions** page to help customers get inspired and find what they need for that special day.

  5. A **Profile** page for clients to enter their personal information and check their past orders.

  6. A **Blog** where customers can view and comment about diverse topics concerning plants.

  7. A **Shopping Bag** where customers can leave their desired products and then proceed to the checkout.


## Structute

There are 8 main pages, including the Home page, a Checkout page and a Login/Register page.
Other than these, there is a main page which fills in as the base for the wide range of various pages.

- **Home Page**

The home page gives gives a quick look at what the store is selling and a direct way to the Products page.

- **About Page**

This page discusses what is the store's concept and idea.

- **Products Page**

This page exhibits all of the store's products which can be arranged by *price*, *rate* and *category*.
Clients can click in every product which will lead them into the product detail page where there's a description of the product and the possibility of adding it to the shopping bag.

- **Plants Page**

This page exhibits all of the store's plants which can be arranged as *live plants* and *artificial plants*.
Clients can click in every product which will lead them into the product detail page where there's a description of the product and the possibility of adding it to the shopping bag.

- **Accessories Page**

This page exhibits all of the store's accessories which can be arranged as *pots* and *decorations*.
Clients can click in every product which will lead them into the product detail page where there's a description of the product and the possibility of adding it to the shopping bag.

- **Special Occasions Page**

This page exhibits all of the store's products for special occasions which arranged by *Valentines Day*, *Wedding Bouquets* and *Christmas*.
Clients can click in every product which will lead them into the product detail page where there's a description of the product and the possibility of adding it to the shopping bag.

- **Posts page**

This page as the name implies comprises of a series of posts added by the admin.
Clients can sort posts by Name A-Z and vice versa. Users can view posts but can only leave a comment if they are signed in.

- **Shopping Bag**

This page shows the user what they have added to the bag and can update and remove products.
There's also the possibility of browsing more products or continuing to the checkout page.

- **Checkout Page**

Here the client can enter their billing details to finish the checkout.
Afterwards, the user receives an email with their order details and the order is added to their profile.

- **Register/Login Page**

The users are given the choice to Register/login.
For new clients, they can divert to the Register page from here.
They need to incorporate their email address, name and secret password to login.
Whenever that is done, an affirmation connection will be shipped off their email address.
When the email is affirmed, they can log in to the site.

- **Profile Page**

The signed-in clients can add or update their information on this page.
In the event that they have made any past purchases, that information is automatically filled in this page.

## Skeleton

You'll be able to view the sketches, wireframes, and mockups for this project in the **assets** folder in the [Github project repository](https://github.com/gaspar91/planties).

I used [Balsamiq](https://balsamiq.com/) to build the wireframes, so you might need the program in order to view some of the documents.


# User Stories

  ## User

  1. View the shop's products as well as the product details.
  2. Be able to sort products by price, rate, name or category.
  3. Search products by name or description and get the number of results. 
  4. Easy access to size and quantity of a product, when purchasing.
  5. Easy access to the number of products in my bag and total to pay.
  6. Be able to update sizes and products or remove the former from my bag.
  7. Having my information automatically filled in the checkout.
  8. Feeling reassured that my order went through by receiving a confirmation email with my order details.
  9. View the blog's posts as well as being able to give my opinion.
  10. Access the website in several devices.

  ## Admin

  1. Be able to add, update or delete products and posts.
  2. Be able to authorize or delete comments.


# Features

## Existing Features

- Responsive layout: Site is accessable and scalable across devices.
- The Bag Total is updated automatically when adding or removing products from the bag.
- Users can update, add and remove products from the shopping bag.
- Users can explore the website even if they aren't logged in.
- Users can only purchase products if they are signed in.
- Users can only comment on posts if they are logged in.
- Only the Admin has access to add, edit and delete products and posts.
- Users can look for products in the search bar by name or description.
- Users that fillout their information in the profile will view them in the checkout form and vice-versa.
- Users can save their information to their profile when filling the checkout form.
- Past orders can be viewed in the users profile page.
- Users comments will only show after the Admin aproves them.
- Scroll to top button added in all pages with products and posts in all devices, and in the shopping bag on mobile.
- Depending on the function that the User or the Admin perform, a message will appear on the top left corner of the screen.
- A pop up windown will appear in case the Admin decides to remove something, to avoid removing things by accident.
- After checking out, user get an email with their order details.
- If a user writes "/add", "edit" or "delete" in the end of the link, a pop up message will appear stating that only the super user is allowed to access that page.

## Features Left to Implement

- User can search for posts by name or category.
- Posts have categories and images.
- Redirect the user back to the product they want to purchase when having to login.
- A contact page with a form for further inqueries/sugestions from clients.
- User can login with their social media accounts.
- Have measurements of the plants and other prouct sizes.
- Adjust the size of the product in the shopping bag.
- social media icons so users can check more information about the shop.
- Linking a related product a to blog post.
- Order Tracking System.


# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - The project uses HTML5 to construct the pages within the application.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.
- [Jquery (ver 3.4.1)](https://jquery.com/download/)
  - The project uses the Jquery in order to make it much easier to use JavaScript.
- [Gitpod](https://www.gitpod.io/)
  - The project uses Gitpod as the primary IDE for coding.
- [Github](https://github.com/)
  - The project uses Github for remote storing of code online.
- [Balsamiq](https://balsamiq.com/)
  - The project uses Balsamiq to create wireframes.
- [Adobe Xd CC](https://www.adobe.com/pt/products/xd.html)
  - The project uses Adobe Xd CC to create mockups.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - The project uses Jinja for templating with Flask.
- [Heroku](https://www.heroku.com/)
  - The project uses Heroku for app hosting.
- [Python](https://www.python.org/)
  - The project uses Python as a programming language.
- [Google Fonts](https://fonts.google.com/)
  - The project uses Montserrat as the main font.
- [Django (ver 3.1.5)](https://www.djangoproject.com/)
  - The project uses Django as a programming language.
- [Stripe](https://stripe.com/)
  - The project uses Stripe's test payment functionality.
- [SQL](https://www.mysql.com/)
  - The project uses SQL as the relational database to hold the backend information for the varions models used, when running locally.
- [PostgreSQL](https://www.postgresql.org/)
  - The project uses Heroku's PostgreSQL relational database to hold the backend information for the various models used, when deployed remotely.
- [AWS S3](https://aws.amazon.com/)
  - The project uses AWS' S3 to store static and media files.


# Testing

All the links have been manually tested.
Tested if there are any problems in the coding or code styling from the Problems tab in Gitpod.
There are some long line that I couldn't figure out how to me more PEP8 friendly. 
I did a detailed testing on each page and updated the results using an Excel as you can see below.
You can also see it in the **assets** folder.

![GitHub Logo](/assets/readme-files/planties-1.jpg)
![GitHub Logo](/assets/readme-files/planties-2.jpg)

# Observations

- The website has been checked for responsiveness on a multitude of screen sizes from PC to portable devices, such as tablets and mobile phones.

- All HTML code was run through the [W3C HTML Validator](https://validator.w3.org/) and returned some errors about the pages not starting with a document type declaration.

- Not all code is PEP8 friendly, mostly because the lines were too long and I wans't sure how to fix them.

- The website was made in less than two weeks because I chose to go with [WhiteNoise](http://whitenoise.evans.io/en/stable/) instead of AWS and it wasn't deploying to Heroku properly, so I had to start over.

# Deployment

The website was developed on [GitPod](https://gitpod.io/) and is has been deployed to [Heroku](https://dashboard.heroku.com/), with the source code being available on [my repository](https://github.com/gaspar91/planties).

### Local deployment

1. To run the site locally, you can either download the zip file of this repository by clicking 'download.zip' button at the top of the page and extracting the zip file to your chosen folder or clone this repository. See the steps to clone the repo here : https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository. <br>
If you are cloning the site, make sure you have Python 3 installed for this to work. 

2. Then create a virtual environment with your IDE. Open your preferred IDE, then open a terminal session in the unzip folder or cd to the correct location. 

3. Install the required dependencies with the following command:
```
pip3 install -r requirements.txt
```

4. Create an env.py file and add the following with your own values:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<your value>"    
os.environ["STRIPE_PUBLIC_KEY"] = "<your value>"    
os.environ["STRIPE_SECRET_KEY"] = "<your value>"    
os.environ["STRIPE_WH_SECRET"] = "<your value>" 
os.environ["EMAIL_USER"] = "<your value>"
os.environ["EMAIL_PASS"] = "<your value>"
```
(Django Secret Keys can be generated with websites such as [miniwebtool](https://miniwebtool.com/django-secret-key-generator/).)

5. Add the env.py files to .gitignore so that it is not published at any stage. This is to keep the secret keys and values safe.

6. You need to make migrations to set up the SQLite3 tables. You can do that by:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

7. Create a superuser for your project by using the following command:

```
python3 manage.py createsuperuser
```

8. You can now run this locally by the following command:

```
python3 manage.py runserver
```

9. Once the site is running locally, go to the end of the url and type in /admin to add products, posts, comments, etc.


### Deploying to Heroku 

Once you have set up locally, you can deploy to Heroku by following the below steps:

1. Create an account in Heroku if you dont have one or sign in if you have an existing one.

2. In Heroku, create a new app with a unique name and set your registration.

3. To use the Postgres database for deployment, select 'Heroku Postgres' as a free add-on.

4. Go to Settings in Heroku, click on 'Reveal Config Variables' and enter the following values:

| **Key** | **Value** |
--- | ---
 AWS_ACCESS_KEY_ID | your AWS bucket ID
 AWS_SECRET_ACCESS_KEY | your AWS secret key
 DATABASE_URL | your Heroku Postgres database url
 EMAIL_HOST_PASS | your password to use your gmail account for emails
 EMAIL_HOST_USER | your email address
 SECRET_KEY | secret key used for your Django project
 STRIPE_PUBLIC_KEY | obtained through your Stripe account
 STRIPE_SECRET_KEY | obtained through your Stripe account
 STRIPE_WH_SECRET | obtained through your Stripe account
 USE_AWS | True

 5. You need to login to Stripe, go to the developers section to get the pubic key ad secret key. For the AWS secret key, you need to login to AWS and create a new bucket. Creating a new S3 bucket documentation can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

 6. In Gitpod, create a requirements.txt file:
```
pip3 freeze --local > requirements.txt
```

7. Create a Procfile:
```
echo web: gunicorn planties.wsgi:application > Procfile
```

8. As with local deployment, make migrations to set up the Postgres database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

9. Create a superuser similar to the way in local deployment.

10. Run the server.

11. As with the local deployment, add /admin to the url to go to the admin and add or edit.

12. Add and commit your changes.

13. Login to Heroku by using the command:
```
heroku login -i
```

14. Once logged in, link your Heroku app created above as the remote repository with this command:
```
heroku git:remote -a <your app name here>
```

15. Complete the deployment by pushing the project to Heroku:
```
git push heroku master
``` 

16. In Heroku, go to the Deploy tab and connect your app to your GitHub repository and **Enable Automatic Deployment** as the deployment method to automatically push the changes to Heroku from Github.

17. Your site would now be deployed to Heroku.


# Credits

### Content

- This project was developed refering to the Boutique Ado Django mini-project from **Code Institute** course materials.
The codes are customized and modified to fit the purpose of this milestone project.

- For the **Blog** app, I referred to this website [The Start Up](https://medium.com/swlh/build-your-own-blog-with-django-part-1-e5715b7cd9bc).

- The posts and comments use **slugs** which is not taught in the course and tutors are not familiar with, so I got a bit more intel by comparing it with the code from the website [Django Girls](https://tutorial.djangogirls.org/en/django_forms/) and [Alex Garrett](https://www.alexgarrett.tech/blog/article/compose-edit-and-publish/).


### Media

The photos used in this website were obtained from [Unsplash](https://unsplash.com/).


### Acknowledgements

I received inspiration for this project from:

- [Code Institute](https://codeinstitute.net/)
- [Behance](https://www.behance.net/)
- [ww3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)


###### Disclaimer: This project was created for educational use only as part of the Code Institute Full Stack Software Development Course</i>

