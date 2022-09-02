# outline

Outline is a django project that allows the user to create events with due dates, and group them using tables
It also allows the user to create their own account, and add their email and app password
By doing so, the program will send an email reminder on the day of the event.
The user may delete and modify tables and events, such as marking them as completed, deleting them or updating information.
Database and website is hosted on heroku. 

Because of Heroku uses a "Ephemeral filesystem", "any files written will be discarded the moment the dyno is stopped or restarted".
Therefore, I need to re-create a superuser/users every time Heroku's Dyno manager restarts.
-> https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem 
This is currently something I'm working on fixing/changing. 
