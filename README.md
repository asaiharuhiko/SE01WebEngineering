# SE01WebEngineering
2026/Q2 in UoA
## outline
### The blogs
The proposed web application allows the user to create blog posts in a shared blog space.

### Main user actions
- Display all blog posts sorted by date, with the most recent post shown first.
- Display the list of authors.
- Show only the blog posts written by a selected author.
- Register in the system with a unique user name and passwrd, and start writing their own blog posts.
- Find all blog posts matching a user query.

### Basic data model idea

#### User table　(Using Django's AbstractUser)
| Column | Type | Comment |
| --- | --- | --- |
| id | int | primary key (auto create) |
| username | string | unique user name|
| password | string | Password |

#### Article table
| Column | Type | Comment |
| --- | --- | --- |
| id | int | primary key (auto create) |
| title | string | Title of the blog |
| author | ForeignKey | Author name of the blog. (Link to User table) |
| content | text | The content of the blog |
| creation_date | date | The date the blog was created |

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
