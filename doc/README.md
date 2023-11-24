# User Stories
As a **young developer**, I want to **publish my article online** so I can **teach others of my peers and receive feedback** <br>
As a **young developer**, I want to **be connected to professional developers** so I can **acquire new skills from them** <br>
As a **tech pro**, I want to **publish my new skill** so I can **share my knowledge with the online community** <br>
As the **tech pro**, I want to **connect to young developers** so I can **build next generation developers all over the world**<br>
As the **tech pro**, I want to **read other people's articles** so I can **contribute to the topics**
As an **anonymous reader**, **I want to read articles online** so I can **get latest information in tech** 



# Acceptance Criteria user story 1
(As a **young developer**, I want to **publish my article online** so I can **teach others of my peers and receive feedback**) <br>
The young developer must be able to create a profile account<br>
The young developer must be able to receive an account confirmation link to complete the login process <br>
The young developer must be able to create, delete or edit his article <br>
The young developer must be able to publish his article <br>

# Acceptance Criteria user story 2 
(As a **young developer**, I want to **be connected to professional developers** so I can **acquire new skills from them** )<br>
The young developer must be able to create a profile account<br>
The young developer must be able to search for matching pro using filter <br>
The young developer must be able to see available pro <br>
The young developer must be able to select available pro by category <br>
The young developer must be able to connect to the selected pro  <br>

# Acceptance Criteria user story 3
(As an **tech pro**, I want to **publish my new skill** so I can **educate people in the online community** )<br>
The pro developer must be able to create a profile account<br>
The pro developer must be able to create, delete or edit personal article <br>
The pro developer must be able to publish his article <br>
The article must be available for others to read

# Acceptance Criteria user story 4 
(As the **pro deeveloper**, I want to **mentor young developers** so I can **build next generation developers all over the world**)<br>
The pro must be able to create a profile account<br>
The pro developer must be able to receive request from any young developer that choose him <br>
The pro developer must be able to accept the request <br>

# Acceptance Criteria user story 5
(As the **pro developer**, I want to **read other people's articles** so I can **contribute to the topics**) <br>
The pro developer must be able to create a profile account successfully<br>
The pro developer must be able to read available articles <br>
The pro developer must be able to make comment on other people's post  <br>


# Acceptance Criteria user story 6
(As an **anonymous reader**. I want to **read articles online** so I can **update my tech knowledge**)<br>
The anonymous reader must be able to acess the blog using the correct link<br>
The anonymous reader must be able to reader information at the home page<br>
The anonymous reader must be able to reader other general articles on the blog page<br>




# Mis-User Stories
As a **anonymous reader**, I want to **make an abusive comment on people's blog** so I can **proke them to angry** <br>
As a **bloger**, I want to **delete other user's post** so I can **violate user's privacy and ownership right** <br>
As a **bloger**, I want to **inject malicious script command in the comment box** so I can **gain unauthorized access to the database** <br>


## Mitigation Criteria for mis-user story 1
An anonymous reader must not be able to reader private post<br>
An anonymous reader must not be able to make comment on the blog<br>

## Mitigation Criteria for mis-user story  2
strong access controls and authentication mechanisms must be implemented to prevent unauthorized access to website
The bloger must provide authentic username and password to login<br><br>
The bloger must not be able to login to another user account<br>
The bloger must not be able access delete button on ther user account<br>
The bloger must not be able to edit other usrer article<br>


## Mitigation Criteria for mis-user story  3
strong access controls and authentication mechanisms must be implemented to prevent unauthorized access to website
The blogger must login with valid credentials<br>
The bloger must not be able to send malicios code through the comment<br>
All the text in the text box must be render as plain text<br>
Escape html must be enforced for all the text boxes<br>

