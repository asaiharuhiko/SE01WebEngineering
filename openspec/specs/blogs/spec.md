# The blogs
s1320047 ASAI Haruhiko

## General Description
The proposed web application allows the user to create blog posts in a shared blog space.

## Main user actions
The user can 
1.	Display all blog posts sorted by date, with the most recent post shown first.
2.	Display the list of authors.
3.	Show only the blog posts written by a selected author.
4.	Select a date in the calendar and display all posts written on that day.
5.	Register in the system with a unique user name and password, and start writing their own blog posts.
6.	Find all blog posts matching a user query.

## Note
1.	Each blog post is associated with an author, and consists of a title, text content, and creation date.
2.	Initially, the database should contain A authors (about 5) and N blog posts (about 20).
3.	The system should not display more than P posts per page. If there are more matching posts, the app should display “Next” and “Previous” links for pagination.
4.	For the search function, the user types a string in the search box, and the system returns all blog posts containing in the title.

## User interface (sketch)

Home
![home](images/home.png)

Search
![search_text](images/search1.png)
![search_date](images/search2.png)
![search_author](images/search3.png)

author
![author](images/authors.png)

post blog page
![post_blog_page](images/post_blog.png)

Blog text page
![blog_text_page](images/blog_text.png)






## Basic data model idea

The database will contain two tables:

#### User table　(Using Django's AbstractUser)
| Column | Type | Comment |
| --- | --- | --- |
| id | int | primary key (auto create) |
| username | string | unique user name|
| password | string | Password |

#### BlogPost table
| Column | Type | Comment |
| --- | --- | --- |
| id | int | primary key (auto create) |
| title | string | Title of the blog |
| author | ForeignKey | Author name of the blog. (Link to User table) |
| content | text | The content of the blog |
| creation_date | date | The date the blog was created |

## Project plan
1.	Set up the development environment.
2.	Create the database and design its structure.
3.	Implement the business logic.
4.	Create a simple HTML prototype of the interface.
5.	Add richer interaction to the interface.
## Main data entities

### Models
- **BlogPost**: id, title, author (ForeignKey to User), content, creation_date
- **User**: Django's AbstractUser (id, username, password, etc.)

### Forms
- **BlogForm**: ModelForm for BlogPost (fields: title, content, creation_date)

### Views
- **IndexView**: Display all blog posts sorted by date (most recent first)
- **SearchView**: Search posts by title keyword, date, or author
- **CreatePostView**: Create new blog post (login required)
- **PostDetailView**: Display single blog post
- **CalendarView**: Display calendar and posts for selected date
- **AuthorsView**: Display list of all authors

### Services
- **create_post**: Create and save new blog post with author association

### Selectors
- **get_latest_posts**: Retrieve paginated blog posts sorted by date
- **get_posts_by_query**: Search posts by title keyword
- **get_posts_by_date**: Filter posts by creation date
- **get_posts_by_author**: Filter posts by author username
- **get_post**: Retrieve single post by ID
- **get_authors_list**: Retrieve paginated list of all authors
- **get_calendar_context**: Generate calendar HTML and navigation context

### Templates
- **index.html**: Home page with latest posts
- **post_detail.html**: Single blog post view
- **create.html**: Blog post creation form
- **search.html**: Search results page
- **authors.html**: Authors list page
- **author_list.html**: Partial template for HTMX author list updates
- **post_list.html**: Partial template for HTMX post list updates
- **calendar.html**: Calendar component with navigation


## Main user flow

1. **Enter page**: Display home page with latest blog posts sorted by date (most recent first)
2. **Login**: Input username and password → authenticate and redirect to home page
3. **Post Blog**: Click "Post Your Blog" → input title, content, creation date → save to database
4. **Search by keyword**: Input string in search box → display posts matching title keyword
5. **Search by date**: Click day in calendar → display posts created on that date
6. **Search by author**: Click author name → display posts by that author
7. **View post**: Click blog title → display full blog post content
8. **Pagination**: Click "Next"/"Previous" links to navigate through multiple pages of results

## Architecture sketch
![architecture sketch](images/arcsk.png)