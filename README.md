# SE01WebEngineering
2026/Q2 in UoA
## outline
The proposed web application allows the user to create blog posts in a shared blog space.

### Main user actions
- Display all blog posts sorted by date, with the most recent post shown first.
- Display the list of authors.
- Show only the blog posts written by a selected author.
- Register in the system with a unique user name and passwrd, and start writing their own blog posts.
- Find all blog posts matching a user query.

### Basic data model idea

#### User table
| Column | Type | Comment |
| --- | --- | --- |
| id | int | Unique user name|
| password | string | Password |

#### Article table
| Column | Type | Comment |
| --- | --- | --- |
| title | string | Title of the blog |
| author | string | Author name of the blog |
| content | string | The content of the blog |
| creationDate | date | The date created the blog |

## environment
- HTMX
- Django
- Python >= 3.13
## tools
### uv 
for package management
### Ruff 
for formatting and linting
### coverage.py 
for coverage 
### pytest
for testing
### git 
for version management
### Visual Studio Code 
for coding
