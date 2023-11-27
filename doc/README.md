# User Stories
1. **As an aspiring developer**, I want to **publish articles online** so I can **inspire other aspiring developers**.
2. **As an aspiring developer**, I want to be **connected to professional developers** so I can **get to learn from them**.
3. **As a professional developer**, I want to **publish content** so I can **enlighten aspiring developers on how to go about their tech journey**.
4. **As an anonymous reader**, I want to **read articles online** so I can **get the latest information in tech**. 
5. **As an Administrator**, I want to **manage the user's content** so I can **ensure eligible content is published**.
## Acceptance Criteria for User Story 1

Given that I am an aspiring developer who wants to publish an article on DeevDiaries, when I access the DevDiaries information, then I should be able to create customized content.

   1. The system should display a user-friendly interface for accessing DevDiaries information.
   2. The DevDiaries information should be categorized by young developer and Professional developer.
   3. Users should be able to format the content including adding text, images, and links.
   4. Users should be able to customize the article as public or private.
   5. The users should be able to preview the content before publishing.
   6. Once the blog post is created, the user should be able to publish it.
   7. The published blog post should be accessible to others using the application.

## Acceptance Criteria for User Story 2

Given that I am an aspiring developer looking for a mentor on DeevDiaries, when I perform a filter using the predefined criteria, then I should receive results based on my filter options and get connected to my chosen mentor.

  1. The filter functionality should be easily accessible from the main interface.
  2. The professional developer information should be categorized by the programming language they know such as Python, C, C++, Java, etc.
  3. Users should be able to filter the search by category.
  4. Users' filter results should include professional developers that match the filter criteria.
  5.  The results should be displayed in an organized and easy-to-read format.
  6.  The users should be able to send mentorship requests to the professional developer.
  7.  The users should be able to click connected to send a mentorship request is the chosen professional developer.

## Acceptance Criteria for User Story 3

Given that I am a professional developer who wants to mentor an aspiring developer, when I log in to my DevDiaries account, then I should be able to accept mentorship requests from young developers and get connected.

  1. The system should display a user-friendly interface for accessing DevDiaries information.
  2. The professional developer should be able to create a profile detailing the language he can teach.
  3. The user should be able to log in with valid credentials.
  4. The user should be able to see available requests on his page.
  5. The users should be able to accept mentorship requests from the young developer.
  6. Users should be able to send direct comments to the mentee.

## Acceptance Criteria for User Story 4

Given that I am an anonymous reader who wants to read articles on DevDiaries information, when I access the DevDiaries home page then I should be able to read all available contents.

   1. The system should display a user-friendly interface for accessing DevDiaries information.
   2. The article should be well structured and organized by content type.
   3. The user should be able to navigate to any chosen content.
   4. Users should be able to click read to view the details of the blog post.

## Acceptance Criteria for User Story 5

Given that I am an administrator responsible for managing DevDiaries information, when I update DevDiaries content, then the changes should be reflected in the app, and the information should remain accurate.

1. The platform should provide an interface for administrators to edit, update, and delete DevDiaries information and blog posts.
2. After making changes, the updated information should be displayed or removed from the application.
3. Users accessing the platform should see the most recent, active, and accurate DevDiaries details.
4. Any changes made by administrators should be tracked and documented for reference.

## Mis-User Stories

**As an anonymous reader**, I want to **make abusive comments on people's blogs** so I can **discredit the App**.<br>
**As a blogger**, I want to **delete other users' posts** so I can **violate user's privacy and ownership right**.<br>
**As a blogger**, I want to **inject malicious script commands in the comment box** so I can **gain unauthorized access to the database**.<br>
## Mitigation Criteria for Mis-User Story 1

1. An anonymous reader must not be able to read private posts.
2. An anonymous reader must not be able to make a comment on the blog.
## Mitigation Criteria for Mis-User Story 2

1. Strong access controls and authentication mechanisms must be implemented to prevent unauthorized access to the app.
2. The blogger must provide an authentic username and password to log in.
3. The blogger must not be able to log in to another user account.
4. The blogger must not be able to access the delete button on the user account.
5. The blogger must not be able to edit other user articles.
## Mitigation Criteria for Mis-User Story 3

1. Strong access controls and authentication mechanisms must be implemented to prevent unauthorized access to the App.
2. The blogger must log in with valid credentials.
3. The blogger must not be able to send malicious code through the comment.
4. All the text in the text box must be rendered as plain text.
5. Escape HTML must be enforced for all the text boxes.




