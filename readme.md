# Interview Problems Solutions
Thank you for taking the time to review my solutions. I have made some reasonable assumptions, noted as comments in my code. In an actual work environment, I would clarify the requirements directly with the owner.

I'm a little confused as to what is desired by question 1, but seeing that the goal is to get insight into my coding style, I have made an interpretation of the requirements.

I'm not quite sure why the database schema has both courses and class as tables. The primary keys of each are the same when you consider that the class id simply a combination of section and course code. I'm not sure why they duplicate information as well (instructor). I'm also a bit confused why instructor is a string in one table but a number in the other. I would combine these into one table if I could rewrite the schema. I've written my code to support this schema though.

For question 2, since it would be simple to make any binary tree for students, I made a binary search tree. It should be close to being complete and balanced as well, but I'm not sure.

I interpreted the requirement of "tree location can be used as lookup" as follows:
"If you have the node object, you can access any of the student's details."

It was fun! Please let me know how I did and reach out if you have any questions or concerns.

Cheers!