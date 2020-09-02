#E-commerce Plant Webshop
For Codeinstitute's Data Centric Development Milestone Project.

#About

#Main Technologies used:

 HTML, CSS, JavaScript, Python+Flask, MongoDB


#Requirements for the project:

- Data handling: Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate 
data records about a particular domain. If you are considering using a different database, please discuss that with your 
mentor first and inform Student Care.

- Database structure: Put some effort into designing a database structure well-suited for your domain. Make sure to put 
some thought into the nesting relationships between records of different entities.

- User functionality: Create functionality for users to create, locate, display, edit and delete records 
(CRUD functionality).

- Use of technologies: Use HTML and custom CSS for the website's front-end.

- Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap 
to accomplish this).

- Documentation: Write a README.md file for your project that explains what the project does and the value that it 
provides to its users.

- Version control: Use Git & GitHub for version control.

- Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or 
tutorials). Attribute any code from external sources to its source via comments above the code and (for larger 
dependencies) in the README.

- Deployment: Deploy the final version of your code to a hosting platform such as Heroku.

- Make sure to not include any passwords or secret keys in the project repository.


#Shopping cart requirements + setup


First thing I did was plan the data structure for the cart and figure out how I was going to save it.  

for tracking a cart, I am using the following data model:
 - id (the unique id)
 - user_id
 - product_id
 - quantity
 

 So basically whenever I add a product to the cart, I'm just inserting a row in to the cart 
 table with those properties.
 
I went through the following steps: 
 
1. Add to Cart button is in a form. Include hidden field for `product_id` with the value set to the product id.
2. Connect current username to the "name" attribute on the cart button
3. Form submits to the `/add_cart` route
4. In the `add_cart` route, I then insert into the cart collection
5. I fetch the `user_id` from the session.
6. I fetch the items of the cart in the `cart` route.
7. I loop through each cart item, and fetch the prodct using `.find_one` with the product id.


#Stuff to add in the future

- add a search function
- add a filter function (based on names/preferences/difficulty etc)
- add a quiz
- add a page for every plant with accurate description
- allow users to process payment 
- allow users to buy without logging in


#Demo

![front page](assets/img/Capture.jpg?raw=true)
![shop display](assets/img/Capture2.jpg?raw=true)

#UX
The central target audience for HappyPlants are people who want to buy plants or people in search of gifts. 
These are people of all ages. User goals are the following:

- Buy a plant for yourself or as a gift to someone else.
- Find information on plant care.
- Find information on specific plant.
- Find best plant for you. 
- To navigate the website easily.
- Ultimately to buy a product 

Some of the user goals I've included are currently out of scope for this project, since I have mostly focused on CRUD
functionality. The shopping cart is not a fully functional shopping cart, meaning that at this stage the user can't 
check out yet.

The palette for HappyPlants is all about color. The blues, yellows, and greens are bright, playful, and tie directly 
into products and are used consistently throughout the entire website. I think this type of color-scheme 
stands out and can help a website to capture the viewers attention. 
Because the color palette by itself, already creates a strong visual impact I have tried to keep the rest of 
the web design clean and minimalistic. The main brand color is turqoise and all the complementary shades were chosen
through adobe colorwheel. The information/products presented on the webpage are laid out in a way that are easy for 
the user to navigate. However in the future I would also like to add more product details.


#Wireframes

These wireframes were drawn up by hand during the initital stages of the planning process. Since I mostly 
relied on a bootstrap theme for my homepage, most of the blueprint was already taken care of. The shop and 
the cart follow pretty basic schematics.


![front page](assets/img/wireframes_shop.jpg?raw=true)

#Testing
I have used the following validation services to check the validity of my code:

W3C Markup Validation was used to validate HTML.
W3C CSS validation was used to validate CSS.
The site's functionality was manually tested.


I. Home page

Does each navigation item change color when hovered over?

- Yes/Pass

Does the color go back to the original state when onhovered?

- Yes/Pass

Do the buttons redirect to their respective pages?

- Yes & No/Partial Pass

Aside from the webshop, I have two additional pages of content. Currenty the content for the quiz is not included, 
so the URL for this page has not yet been added.

When clicking the menu item "contact", does it automatically scroll to the correct place?

- Yes/Pass

Does clicking on cart while logged off produce the following flash message: "Please login to view your cart"?

-Yes/Pass

II. Responsiveness

Does the home page behave responsively when viewed on all* screen sizes?

- Yes/Pass

Note*: "All" in this context means the screen sizes that I tested on, which are: Laptop with MDPI screen iPhone 6/7/8,
iPhone X, iPad, iPad Pro, iPhone 6/7/8 plus. Overall the landscape mode across all devices (except for iPads) lacks 
uniformity, as I was focused mainly on re-positioning "stray" html elements. Furthermore, iPad Pro portrait mode, was
not made responsive due to time constraints. This also applies to all of the questions below. The best way to view the 
website is with the laptop MPDI screen. 


Does the shop behave responsively when viewed on all screen sizes?

- Yes/Pass

Does the "plant for beginners" page behave responsively when viewed on all screen sizes?

-Yes/Pass

Does the "top 10 plant care tips" page behave responsively when viewed on all screen sizes?

-Yes/Pass

Does the cart behave responsively when viewed on all screen sizes?

- Yes/Pass

III. Login/Register

Does the join button redirect to the correct page?

- Yes/Pass

When registering, does the following message flash when entered passwords do not match: "Passwords are not the same"?

-Yes/Pass


Does "You're account has been registered" flash when a user has been registered?

-Yes/Pass

Is a user redirected to the login page upon finalizing their registration?

-Yes/Pass

Does "Invalid password or username provided" flash when trying to login with wrong username/passw.

-Yes/Pass

Does "You were successfully logged in" flash when a user has successfully logged in?

-Yes/Pass

Does the navigation menu display the username? 

-Yes/Pass

Does a "sign out" option appear in a drop down menu?

-Yes/Pass

Can a user add items to cart and does a flash message "Item(s) added to cart" appear when an item is added?

Yes/Pass

Can a user add the same item mulitple times?

-Yes & No/Partial Pass

At this stage it's only possible to select a quantity and add it to the cart only once from the shopping page.
A user CAN however edit the amount of a given item in the cart page.

IV. THE CART

Does the cart display all the items added by a user?

-Yes/Pass

Does the cart display the correct quantity of the added item?

-Yes/Pass

Does the cart display the aggregated price correctly when multiple of the same item is added to the cart?

-Yes/Pass

Can a user edit the quantity of the item and does the price display correctly afterwards?

-Yes/Pass

Does a user get a flash message when a cart has been updated? 

-Yes/Pass

Can a user delete an item?

-Yes/Pass

Can a user re-add an item which was deleted from the cart page?

-No

Currently when a user deletes an item, that item cannot be re-added from the shop page. This still needs to be worked out.


#Deployment to Heroku

Steps to take:

- Firstly, create a Heroku app by clicking the "New" button in the Heroku dashboard.

- Secondly, we need to link our local Git repository to Heroku, which is what we're going to do in this video.

- Thirdly, create a requirements.txt file (pip freeze > requirements.txt), which contains a list of our dependencies.

- And finally, create a Procfile (echo web: python run.py > Procfile), which is a special kind of file that tells Heroku how to run the project.

- In heroku dashboard select the master branch then click "Deploy Branch".

#Media

I do not own the media used in this project. I also did not write any of the material listed on this website.

Most of the pictures used on this website are property of https://www.thesill.com. 

Plant photos listed in the shopping page are property of https://shop.chelseagardencenter.com.

Articles are taken from various websites including: 

https://www.thesill.com

https://www.thespruce.com/easy-houseplants-hard-to-kill-4141665 

https://www.housebeautiful.com/lifestyle/gardening/g31355906/easy-low-maintenance-plants/ 

https://bloomscape.com/plant-care-guide/pothos/ 

https://blog.gardenloversclub.com

https://www.lifehack.org/390369/10-indoor-plants-that-are-easy-take-care 

https://smartgardenguide.com/best-houseplants-for-beginners/ 

https://thegardeningcook.com/how-to-grow-dracaena-fragrans-corn-plant/ 

The following bootstrap theme was used for the front page and navigation: 

Grayscale v6.0.1 (https://startbootstrap.com/themes/grayscale)