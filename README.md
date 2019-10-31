# TheBlog

TheBlog is a web application that allows users to express themselves through writing articles and posting the in the application. 
### Author
* John Mbugua

### Features
As a user of the application, you will be able to:
> * See different posts posted by other users
> * Post your own blog
> * Vote for other people's posts
> * Comment on other people's posts
> * create an account, login and update your profile 

### BDD
| Behaviour    | input     | output     |
| -------------| :--------:| -----------|
| View all posts | Home page displays all posts  | Home page displays all posts |
|login| Click on **login**|allows user to login into the account using the login form|
|create an account| Click on **sign in**|form which allos users to sign in for the first time|
|post a blog| Click on **Post Blog**|brings an input form for posting a blog|
|like a post/dislike| Click on **like/dislike**|The number of likes and dislikes increases by one |
|comment on a post| Click on **comment**|Display a comment box to allow users to post a comment on a specific blog|
|Update profile| Click on **Profile** |Takes the user to the profile page with options to edit and upload profile picture|

## Getting started
#### Prerequisites
 * python 
* Virtual environment
* pip

#### Cloning
Navigate into the folder you want the application to be
In your terminal, run the commands
  > $ git clone https://github.com/Jmos-Mbugua/The-Blog
  > 
  > $ cd The-Blog

### Running the application
* Modify the start.sh file with your own api key
* To run the app type the commands in your terminal
 install all the dependencies listed in the requirements.txt file
> $ chmod a+x start.sh
>
> $ ./start.sh

### Testing the application
* To run the tests for the class in your terminal
 > $ python3.6 manage.py test

 ### Technologies used
Python
Flask
Html
Bootstrap

### Known Bugs
The gmail server port specified is not responding which means the welcome email is not sent
### License
This project is Licensed under MIT.
©2019 Copyright.
### Collaborate
>To Collaborate, Reach me out at:
>>Github: [Jmos-Mbugua](https://github.com/Jmos-Mbugua)
>>Email: johnmbugua849@gmail.com

