# Shosho-Media
A social network where people of similar hobbies can meet and connect with an interesting spin - by Using Jonathan Haidt ranking system of a social network to ensure a fair and safe network

# NB: Still working for the ranking system in the next update


# Shosho-Media
A social network where people of similar hobbies can meet and connect with an interesting spin - by Using Jonathan Haidt ranking system of a social network to ensure a fair and safe network

## Project Documentation
+ Project Documentation is provided below.

## Features
+ User
    * Mandatory Registration to access the site!

    * Login (For Registered Users)
    * Logout (For Registered Users)
    * Edit Profile (For Registered Users)
      * username
      * email address
      * location
      * profile image
      *bio
  
+ Admin
    * CRUD Operations
    
+ User Profile
    * Edit Profile
    * Reset Password (django all-auth)
    

* Follow
    * Follower List
    * Unfollow friend from friend list
    * Users can search other users and send follow each other
    * Users can view the posts of other users they follow
    

    
## Pages and navigation

![alt text](https://user-images.githubusercontent.com/74027215/183246322-1dc02886-869b-44b7-bc09-81504e24b05d.png)

## Technological considerations

* Django 2.1
* Python 3.7
* Bootstrap 5
* Heroku
* PostgreSQL 12
* AWS S3 bucket

### Needed Django models and their attributes
+ Profile Model
+ Post Model
+ Comment Model
+ Thread Model
+ Message Model
+ Notification Model

### URIs
Completed URLS:


urlpatterns = [

    path('', PostListView.as_view(), name='post-list'),
    path('explore/',Explore.as_view(),name='explore'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/share', SharedPostView.as_view(), name='share-post'),
    path('post/edit/<int:pk>',PostEditView.as_view(),name='post-edit'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/delete',CommentDeleteView.as_view(),name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like',AddCommentLike.as_view(),name='like-comment'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike',DislikeComment.as_view(),name='dislike-comment'),
    path('post/<int:post_pk>/comment/<int:pk>/reply',CommentReplyView.as_view(),name='reply-comment'),
    path('post/<int:pk>/like',AddLike.as_view(),name='like'),
    path('post/<int:pk>/dislike',Dislike.as_view(),name='dislike'),
    path('profile/<int:pk>/',ProfileView.as_view(),name='profile'),
    path('profile/edit/<int:pk>/',ProfileEditView.as_view(),name='profile-edit'),
    path('profile/<int:pk>/followers/add',AddFollower.as_view(),name='add-follower'),
    path('profile/<int:pk>/followers/remove',RemoveFollower.as_view(),name='remove-follower'),
    path('profile/<int:pk>/followers/',ListFollowers.as_view(),name='list-follower'),
    path('search/',UserSearch.as_view(),name='profile-search'),
    path('notification/<int:notification_pk>/post/<int:post_pk>',PostNotification.as_view(),name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>',FollowNotification.as_view(),name='follow-notification'),
    path('notification/<int:notification_pk>/thread/<int:pk>',ThreadNotification.as_view(),name='thread-notification'),
    path('notification/delete/<int:notification_pk>',RemoveNotification.as_view(),name='notification-delete'),
    path('inbox/',ListThreads.as_view(),name='inbox'),
    path('inbox/create-thread',CreateThread.as_view(),name='create-thread'),
    path('inbox/<int:pk>',ThreadView.as_view(),name='thread'),
    path('inbox/<int:pk>/send',CreateMessage.as_view(),name='create-message'),


]

### Heroku deployment
Deployment URL: https://shoshomedia.herokuapp.com/

## Requirements
To run the web app properly you need to follow the following requirements and have them installed in the virtual environment.
+ Check out the requirements.txt


## User

The user app has all the functionalities like login, signup, viewing profile and editing   profile. The proper usage of the app comes with the initial usage of the app. The very beginning the app routes user to login in the app. The app used Django’s in built auth form in order to ensure the security of the user.

   + Login:
   
   In the login page user have to give the user name and the password of the user in order to access to the web app. If the user does not have any account in the web app, they can access the sign up page from there using the sign up link just below the sign in form
+ Register
    + In the sign up page the user have to register himself to the web app. For that the user have to give some information in the very beginning. The user must have to provide the following info.
      + First name
      + vLast name
      + Username
      + Password


  + The requirements of providing password is as follows:
    + Your password cat be too similar to your other personal information.
    + Your password must contain at least 8 characters.
    + Your password cannot be a commonly used password.
    + Your password cannot be entirely numeric.
+ View profile

In the view profile page you can view the information you have listed. To update the information you have provided you can click on the edit button below and this will take you to the edit profile page.  

+ Edit profile

In the edit profile page the user can update the information they have provided before and also now they can add some more informations like prone number, address. The cool part is now they can add and upload the profile picture of them and see that in the other part of the application.  

+ View followers list

A user can check his or her followers in the dropdown menu.


+ Update posts 

In the update posts the user can give the content of the status and click the post button. 

### Screenshots
![6](https://user-images.githubusercontent.com/74027215/183247519-721c7cf9-b84f-488a-af8f-ca5bc6f5c367.png)
![7](https://user-images.githubusercontent.com/74027215/183247521-4993ed45-5248-4110-ad77-ff604d56d83c.png)
![8](https://user-images.githubusercontent.com/74027215/183247524-1ce764b1-5e5c-4e8d-b50f-0d499af323e5.png)
![9](https://user-images.githubusercontent.com/74027215/183247525-cd5220ff-7d87-424d-9457-b67ca9f6eb8d.png)
![11](https://user-images.githubusercontent.com/74027215/183247526-df794b90-7775-4257-b230-faed748c9fea.png)
![1](https://user-images.githubusercontent.com/74027215/183247527-6a6f54f5-d193-4b45-b121-0c1b06a37392.png)
![2](https://user-images.githubusercontent.com/74027215/183247528-42e878f4-6566-42ed-bb05-27965ab706d3.png)
![3](https://user-images.githubusercontent.com/74027215/183247529-a373c2f4-6427-4cfe-9862-e76c0207b5ce.png)
![4](https://user-images.githubusercontent.com/74027215/183247530-165d9356-2a54-47ca-90f2-2c38132433e4.png)
![5](https://user-images.githubusercontent.com/74027215/183247532-c6f36887-7318-48a7-8bbc-962abba3cf41.png)

