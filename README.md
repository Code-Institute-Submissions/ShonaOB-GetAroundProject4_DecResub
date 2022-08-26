<h1 align=center> GetAround.ie </h1>

<p align=center>Travel like a local... <br/> Locals know the best ways to get around our favourite cities, our site lets the locals rate their favourite transport routes to our favourite tourist sites! <br/>

</p>
<p align="center">
<img src="media/readme/">
</p>

Live app link [here]()


## User Experience

### User Stories

As a user, I would like to: 

1. Register as a user. This will allow me to like other people's ratings, and to log my own ratings. 

2. Create a Review: share my own experiences including a photo if I have one, and a rating from 1 to 5 on the transport I used. 

3. Like other users posts

4. Navigate the site easily, in a familiar way

5. Search for reviews by the city I am visiting

As an administrator, I would like to: 

1. Be able to log in and view the admin panel

2. Be able to manage posts/reviews as required including editing and deleting. 


### 1. Strategy

  + **Project Goal**

   Create a platform that allows people (users) to share their experiences with local transport networks, and rate them from 1 to 5 stars. 


### 2. Scope

This project will cover the building of the basic application, including: 

- registration and authentication of users
- creating reviews
- liking reviews
- searching for reviews by city

## Functional Scope 

**GetAround DER - Diagram Entity Relationship**

<img width= "800" src="media/readme/bestbeer_der.png">

**Agile Methodology**

<details>
<summary>SPRINTS</summary>

Test cases were linked with every User story presented above, and can be found in TESTING.md(TESTING.md) - Automated testing section. 

* Sprint 1

  + Setup Django 
  + Heroku Deployment 

* Sprint 2

  + Create Admin Panel & Superuser
  + Create the Add Country, Add City, Add Sight process through Admin
  + Create Index page with views of listed reviews 

* Sprint 3

  + Create Add Review
  + Set up Site Pagination
  + Create Login / Logout / Register pages

* Sprint 4

  + Set up Likes process

* Sprint 5

  + Amend the visual of the rating to show stars based on rating level

* Sprint 6

  + Create Search Bar
  + Amend CSS for branded styling

* Sprint 7

  + Create and manage final user tests
  + Final Deployment

</details>


### 3. Structure

* The site is clean and tidy, with easy to recognise navigation
* Once logged in, the nav bar updates accordingly
* Filtering with the search bar provides a smooth user experience


### 4. Skeleton

The wireframe for this project was created with Balsamiq:


### 5. Theme / Branding

* Colours

I created the background image myself using Procreate. I then pulled the colours from the background image to use throughout the site for continuity. 

  <img width="300" src="static/images/Bg.jpg">

* Font Selection
 
Font was chosen with [Google Fonts](https://fonts.google.com/) to be used across the website.

The most suited font for this project was Quicksand. 

## Existing Features

### **Navbar** 

If the user is logged in, the navbar will present the option to Create a Review, and to Log Out. 

If the user is NOT logged in, the navbar will present the option to Log In or to Register. 

+ The Navbar will collapse on mobile devices. 

### **Home Page**

The home page contains rows and columns which display cards. 

Each card contains the link to the relevant Review and Rating. 

The Card displays: 
The Featured Image (or placeholder as relevant)
The author
The title
The rating in stars
Created/Updated date
Number of likes
A link to read more

### **Review Details page** 

The Review Details page shows:
- The title
- The featured image
- The review body
- The rating in stars
- The like button 

## Future Features

I would like to ...

1. Add maps to the review details; so that you can load the transport option and location on GoogleMaps
2. Allow video uploads; so that users can share more details of the tranport method
3. Add a price field; so that you can filter the best transport options based on price. 
4. Allow Social Media login and sharing 

## Languages Used

Python 3.0

## Frameworks, Libraries & Programs Used

+ Balsamiq: Balsamiq was used to create the wireframes during the design process.
+ Font Awesome: Font Awesome was used on all pages to add icons for aesthetic and UX purposes.
+ Git: Git was used for version control.
+ Google Fonts: Google fonts are used to add fonts for aesthetic and UX purposes.
+ Django
+ LucidChart for the ERD


## Testing and Code validation 



## Project Bugs and Solutions:

| Bugs              | Solutions |
| ---               | --------- |
| Database inconsistency during unittests|Restart all projects, adding two different databases (development and production) to make it possible to run tests successfully.
| Update Review and Delete Unittest failed when tried to change or delete a review | Debug Update review class models and change save function resolved the problem. 
| Navbar dropdown opening behind site divs | Add z-index to navbar resolved the problem. 
| Register feature was not showing the error when it happened | Debug Register function and remove else statement to redirect the user to the same page when it happens. After deleting this part of the function, everything worked fine. 
| Buttons hidden by footer (only in Chrome | Switch margin-bottom to padding-bottom solved the problem. 
| Bitterness and Money value with the same value on beer review details page | Changed variable present on HTML resolved the issue. 
|Logged users could edit or delete reviews from other users if using delete and update urls directly pointing to others reviews pk| handled using loginmixing on post app functions|


## Deployment 

This App is deployed using Heroku.

<details>
<summary>Heroku Deployment </summary>
1. Login to Heroku

2. Create a new App

3. Update the Config Vars 
 

3. Deployment on Heroku

    3.1.  Navigate to the Deploy tab.
    
    <img src="media/readme/deployment/heroku_dashboard_deploy.png">
    
    3.2.  Choose the main branch to deploy and enable automatic deployment to build Heroku every time any changes are pushed on the repository.
    
    <img src="media/readme/deployment/heroku_automatic_deploys.png">
    
    3.3 Click on manual deploy to build the App.  When complete, click on View to redirect to the live site. 
    
    <img src="media/readme/deployment/heroku_view.png">
</details>

# Credits

## Media

+ All pictures and images used in this project are from [Unsplash](https://unsplash.com).

## Work based on other code

[Codemy](https://www.youtube.com/watch?v=AGtae4L5BbI) - Search Bar <br>
[Pyplane](https://www.youtube.com/channel/UCQtHyVB4O4Nwy1ff5qQnyRw) - Star rating tutorial used to develop beer rating feature. <br>
[CodeInstitute](https://www.codeinstitute.net) - Learning Material and module training videos. The initial template layouts were found using the "Think Therefore I blog" walkthrough project, but amended to suit this project. 

# Acknowledgements

+ All my fellow students on our Slack group - they have been hugely supportive and helpful. 
 +Tutoring @ CodeInstitute - a wonderful resource for when I was stuck along the way. 