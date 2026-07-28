## ADDED Requirements

### Requirement: account app views are tested
The `account` app SHALL have tests covering all four views (login, create
account, logout, information) for GET and POST handlers.

#### Scenario: Login GET renders the login form
- **WHEN** a GET request is made to `account:login`
- **THEN** the response SHALL have status 200, use `account/login.html`
  template, and contain a `UserAccountLoginForm` instance in context

#### Scenario: Login POST with valid credentials logs the user in
- **WHEN** a POST request is made to `account:login` with valid username and
  password
- **THEN** the response SHALL redirect to `post:index` and the user SHALL be
  authenticated

#### Scenario: Login POST with invalid credentials returns form errors
- **WHEN** a POST request is made to `account:login` with invalid credentials
- **THEN** the response SHALL have status 200, render `account/login.html`,
  and SHALL NOT authenticate the user, and SHALL contain form errors

#### Scenario: Create account GET renders the registration form
- **WHEN** a GET request is made to `account:create`
- **THEN** the response SHALL have status 200, use `account/create.html`
  template, and contain a `UserAccountCreateForm` instance in context

#### Scenario: Create account POST with valid data creates user and logs in
- **WHEN** a POST request is made to `account:create` with valid username and
  matching passwords
- **THEN** the response SHALL redirect to `post:index`, the user SHALL exist
  in the database, and the user SHALL be authenticated

#### Scenario: Logout GET renders the logout confirmation page
- **WHEN** a GET request is made to `account:logout`
- **THEN** the response SHALL have status 200 and use `account/logout.html`

#### Scenario: Logout POST logs the user out
- **WHEN** an authenticated user sends a POST request to `account:logout`
- **THEN** the response SHALL redirect to `post:index` and the user SHALL NOT
  be authenticated

#### Scenario: Information page requires login
- **WHEN** an unauthenticated user sends a GET request to `account:information`
- **THEN** the response SHALL redirect (302) to the login page

#### Scenario: Information page displays current user
- **WHEN** an authenticated user sends a GET request to `account:information`
- **THEN** the response SHALL have status 200, use `account/info.html`
  template, and contain the current user in context as `account`

### Requirement: post app business logic is tested
The `post` app SHALL have tests for `services.py` and `selectors.py` covering
all exposed functions.

#### Scenario: create_post assigns the author
- **WHEN** `create_post` is called with a valid form and an author
- **THEN** the returned post SHALL have its author set and SHALL persist in
  the database

#### Scenario: get_latest_posts returns posts in reverse chronological order
- **WHEN** `get_latest_posts` is called
- **THEN** it SHALL return a paginated page of posts ordered by
  `creation_date` descending

#### Scenario: get_latest_posts handles pagination boundaries
- **WHEN** `get_latest_posts` is called with page numbers beyond available
  data
- **THEN** it SHALL return the correct (possibly empty) subset of posts

#### Scenario: get_posts_by_query filters by title case-insensitively
- **WHEN** `get_posts_by_query` is called with a query string
- **THEN** it SHALL return posts whose title contains the query string
  (case-insensitive), or an empty page if no match

#### Scenario: get_posts_by_date filters by creation date
- **WHEN** `get_posts_by_date` is called with a date string
- **THEN** it SHALL return posts created on that date, or an empty page if no
  match

#### Scenario: get_posts_by_author filters by author username
- **WHEN** `get_posts_by_author` is called with a username
- **THEN** it SHALL return posts by that author, or an empty page if no match

#### Scenario: get_post returns a single post or raises 404
- **WHEN** `get_post` is called with an existing ID
- **THEN** it SHALL return the corresponding `BlogPost` instance
- **WHEN** `get_post` is called with a non-existent ID
- **THEN** it SHALL raise `Http404`

#### Scenario: get_authors_list returns paginated usernames
- **WHEN** `get_authors_list` is called
- **THEN** it SHALL return a paginated page of all usernames ordered
  alphabetically

#### Scenario: get_calendar_context returns navigation context
- **WHEN** `get_calendar_context` is called with year, month, and optional day
- **THEN** it SHALL return a dict containing `calendar_html`, `year`,
  `month`, `prev_year`, `prev_month`, `next_year`, `next_month`, and
  `selected_day`

### Requirement: post app calendar utilities are tested
The `post` app SHALL have tests for `BlogCalendar.formatday` and
`get_prev_next_month`.

#### Scenario: formatday with a valid day returns a linked table cell
- **WHEN** `BlogCalendar.formatday` is called with a non-zero day
- **THEN** it SHALL return an HTML `<td>` with class `day` containing a link
  to the search URL with the formatted date

#### Scenario: formatday with zero returns an empty cell
- **WHEN** `BlogCalendar.formatday` is called with day zero
- **THEN** it SHALL return `<td class="noday">&nbsp;</td>`

#### Scenario: get_prev_next_month handles January boundary
- **WHEN** `get_prev_next_month` is called with January
- **THEN** the previous month SHALL be December of the previous year

#### Scenario: get_prev_next_month handles December boundary
- **WHEN** `get_prev_next_month` is called with December
- **THEN** the next month SHALL be January of the following year

#### Scenario: get_prev_next_month handles mid-year months
- **WHEN** `get_prev_next_month` is called with a mid-year month
- **THEN** previous and next months SHALL be within the same year

### Requirement: post app forms are tested
The `BlogForm` SHALL have tests for field inclusion and validation.

#### Scenario: BlogForm includes expected fields
- **WHEN** a `BlogForm` is instantiated
- **THEN** its fields SHALL be `title`, `content`, and `creation_date`

#### Scenario: BlogForm requires title and content
- **WHEN** `BlogForm` is validated without a title
- **THEN** it SHALL NOT be valid
- **WHEN** `BlogForm` is validated without content
- **THEN** it SHALL NOT be valid

### Requirement: post app views return correct HTTP responses
The `post` app SHALL have tests covering all six views (index, search, create,
detail, calendar, authors) for status codes, templates, and HTMX behaviour.

#### Scenario: IndexView renders the home page
- **WHEN** a GET request is made to `post:index`
- **THEN** the response SHALL have status 200 and use `post/index.html`
  template

#### Scenario: IndexView includes posts and base_url in context
- **WHEN** a GET request is made to `post:index`
- **THEN** the context SHALL contain `posts` (a paginated page) and
  `base_url` (set to `/?`)

#### Scenario: IndexView returns HTMX partial when requested
- **WHEN** a GET request with `HX-Request: true` is made to `post:index`
- **THEN** the response SHALL use `post/post_list.html` template and set
  `base_url` to `reverse("post:index") + "?"`

#### Scenario: IndexView handles empty post list
- **WHEN** a GET request is made to `post:index` with no posts in the
  database
- **THEN** the `posts` context SHALL contain zero items

#### Scenario: SearchView returns results by word, date, and author
- **WHEN** a GET request is made to `post:search` with `words`, `date`, or
  `author` parameter
- **THEN** the response SHALL have status 200, use `post/search.html`
  template, and contain filtered `posts` in context with a `search_header`

#### Scenario: SearchView redirects when no search parameter is given
- **WHEN** a GET request is made to `post:search` without any search
  parameter
- **THEN** the response SHALL redirect to `post:index`

#### Scenario: SearchView returns HTMX partial
- **WHEN** a GET request with `HX-Request: true` and a search parameter is
  made to `post:search`
- **THEN** the response SHALL use `post/post_list.html` template

#### Scenario: SearchView sets correct base_url for pagination
- **WHEN** a GET request with `words`, `date`, or `author` is made to
  `post:search`
- **THEN** the context SHALL contain `base_url` with the correct query
  parameter

#### Scenario: CreatePostView requires login
- **WHEN** an unauthenticated GET request is made to `post:create`
- **THEN** the response SHALL redirect to the login page

#### Scenario: CreatePostView GET renders the creation form
- **WHEN** an authenticated GET request is made to `post:create`
- **THEN** the response SHALL have status 200, use `post/create.html`
  template, and contain a `BlogForm` instance in context

#### Scenario: CreatePostView POST creates a blog post
- **WHEN** an authenticated POST request is made to `post:create` with valid
  data
- **THEN** the response SHALL redirect to `post:index`, and the post SHALL
  exist in the database with the correct author

#### Scenario: CreatePostView POST with invalid data re-renders form
- **WHEN** an authenticated POST request is made to `post:create` with
  invalid data
- **THEN** the response SHALL have status 200, re-render `post/create.html`,
  and the form SHALL NOT be valid

#### Scenario: PostDetailView shows existing post
- **WHEN** a GET request is made to `post:detail` with an existing post ID
- **THEN** the response SHALL have status 200, use `post/post_detail.html`
  template, and contain the post in context

#### Scenario: PostDetailView returns 404 for non-existent post
- **WHEN** a GET request is made to `post:detail` with a non-existent ID
- **THEN** the response SHALL have status 404

#### Scenario: CalendarView renders the calendar component
- **WHEN** a GET request is made to `post:calendar` with valid year and
  month
- **THEN** the response SHALL have status 200, use
  `components/calendar.html` template, and contain `calendar_html`,
  `year`, `month`, and navigation context

#### Scenario: CalendarView handles selected_day parameter
- **WHEN** a GET request is made to `post:calendar` with a `day` query
  parameter
- **THEN** the context SHALL contain `selected_day` set to the parameter
  value

#### Scenario: AuthorsView renders the authors list
- **WHEN** a GET request is made to `post:authors`
- **THEN** the response SHALL have status 200, use `post/authors.html`
  template, and contain `authors` (a paginated page of usernames) in
  context

#### Scenario: AuthorsView returns HTMX partial
- **WHEN** a GET request with `HX-Request: true` is made to `post:authors`
- **THEN** the response SHALL use `post/author_list.html` template

### Requirement: BlogPost model has a string representation
The `BlogPost` model SHALL have a `__str__` method that returns the title.

#### Scenario: str(post) returns the title
- **WHEN** `str()` is called on a `BlogPost` instance
- **THEN** it SHALL return the post's title

### Requirement: tests use Django TestCase and run via pytest
All tests SHALL inherit from `django.test.TestCase` and be discoverable under
each app's `tests.py`. `pytest` with `pytest-django` is configured as the test
runner via pyproject.toml.

#### Scenario: Tests are runnable with pytest
- **WHEN** `pytest` is executed
- **THEN** all tests in `account/tests.py` and `post/tests.py` SHALL pass
  with no errors

#### Scenario: Tests are runnable with manage.py
- **WHEN** `python manage.py test` is executed
- **THEN** all tests in `account/tests.py` and `post/tests.py` SHALL pass
  with no errors
