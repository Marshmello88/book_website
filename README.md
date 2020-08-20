#E-commerce Plant Webshop
For Codeinstitute's Data Centric Development Milestone Project.

About

#Main Technologies used:

 HTML, CSS, JavaScript, Python+Flask, MongoDB



#Requirements for the webshop:

Mandatory:

Data handling: Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. If you are considering using a different database, please discuss that with your mentor first and inform Student Care.

Database structure: Put some effort into designing a database structure well-suited for your domain. Make sure to put some thought into the nesting relationships between records of different entities.

User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).

Use of technologies: Use HTML and custom CSS for the website's front-end.

Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap to accomplish this).

Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.

Version control: Use Git & GitHub for version control.

Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.

Deployment: Deploy the final version of your code to a hosting platform such as Heroku.

Make sure to not include any passwords or secret keys in the project repository.

#Requirements for the cart

for tracking a cart, I am using the following data model:
 - id (the unique id)
 - user_id
 - product_id

 So basically whenever you add a product to the cart, you're just inserting a row in to the cart 
 table with those three properties.
 
1. Add Cart button is in a form. Include hidden field for `product_id` with the value set to the product id.
2. Form submits to the `/add_cart` route
3. In the `add_cart` route, I then insert into the cart collection
4. I fetch the `user_id` from the session.
5. I fetch the items of the cart in the `cart` route.
6. I loop through each cart item, and fetch the prodct using `.find_one` with the product id.


#Stuff to add in the future

#Demo

#UX
The central target audience for HappyPlants are people who want to buy plants or people in search of gifts. 
These are people of all ages. User goals are the following:

- Buy a plant for yourself or as a gift to someone else.
- Find information on plant care.
- Find information on specific plant.
- Find best plant for you. 
- To navigate the website easily.
- Ultimately to buy a product 

Some of the user goals I've included are currently out of scope for this project. So I mainly focused on the design/
plant stats/navigaton/shopping cart.

The palette for HappyPlants is all about color. The blues, yellows, and greens are bright, playful, and tie directly 
into products and are furthermore used consistently throughout the entire website. I think this type of color-scheme 
stands out and can help a website to capture the viewers attention. 
Because the color palette by itself, already creates a strong visual impact I have tried to keep the rest of 
the web design clean and minimalist. The main brand color is turqoise and all the other different shades were picked 
accordingly. 





#Wireframes
The wireframes were drawn up by hand:

#Testing
I have used the following validation services to check the validity of my code:

W3C Markup Validation was used to validate HTML.
W3C CSS validation was used to validate CSS.
The site's functionality was manually tested.

#Deployment

#Media
