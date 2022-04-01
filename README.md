# Educational Ecommerce Website
Fully functioning education e-commerce website with PayU payment gateway and customer account system for online assets.

## Technology Stack
The project is built using:
- django
- html/css
- postgreSQL
- herokus
- JavaScript

## Using this project
- >This is mainly a platform to display my code and it isn't for external use 
- The project's 'static' folder and 'media' folders, (which contain the images/videos) arent included in this github repo.
- however, this can be used as a reference for whenever you need to copy some code, or refer to something you might be getting an error at

## Project skeleton structure
1. This project is divided into 5 main sections (folders): **courses, onlinetraining, products, resources and training**
2. ### All sections (basic django stuff):
   1. **admin.py** customizes how the admin panel looks for this section
   2. **models.py** has the database tables and columns defined.
   3. **urls.py** has the routing from urls to views
   4. **views.py** has the views, i.e. the different pages that you view
3. ### Courses Section
   1. This section is for the sale of online courses. the videos were uploaded on [vimeo](https://vimeo.com) and embedded here via the database.
   2. The shop, user verification, buying, the payment gateway, addition of data to database on payment verification, and linking of course to user, are all done in the **views.py** file
   3. Database **models.py** has all the courses, and the tutorial-videos associated with them
4. ### Onlinetraining/Training
   1. These sections were for the purchase of tickets for live sessions held online or offline. 
   2. The trainings data/pictures, introduction videos, etc were uploaded to database, and displayed in the shop. on buying the customer would get a ticket, or receive an id-password for the online-training session
5. ### Products
   1. This section was for the purchase of offline goods, tools, and kits which would then be delivered to their doorstep.
   2. Customer data was retrieved upon purchase and they would also receive an email upon order confirmation
   3. Customer Name, Address, order details would all get stored in the database
6. ### The main project folder:
   1. this is where the **settings.py** and the first **urls.py** was stored
   2. **settings.py** : where all the default settings, the locations of media folders, static folders, connections between database and project, are all formed. 
   3. **urls.py** : This is where it was defined where the users would get redirected as soon as they first enter the website. Also where people would be redirected further into any of the above apps. 

