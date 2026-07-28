## Why

The blog application has three search requirements specified in the project spec but none are implemented:
- Text search: find posts matching a query string in the title
- Date search: click a calendar day to see posts from that day
- Author search: click an author name to see their posts

Currently `search.html` was empty, there was no search view, and no selectors for filtered queries.

## What Changes

- Added `get_posts_by_query(query)`, `get_posts_by_date(date_str)`, `get_posts_by_author(author)` to `post/selectors.py`
- Created `SearchView` in `post/views.py` that handles `?words=`, `?date=`, `?author=` query params on `/post/search/`
- Updated `templates/post/list.html` to accept optional `search_header` and `base_url` for correct pagination
- Created `templates/post/search.html` as the search result page
- Added search form to `templates/base/base.html` sidebar
- Added `search/` URL pattern to `post/urls.py`

## Capabilities

### Modified Capabilities
- `blogs`: Added text, date, and author search functionality

## Impact

- `post/selectors.py`: new query functions
- `post/views.py`: new SearchView
- `templates/post/list.html`: optional header + base_url pagination
- `templates/post/search.html`: new template
- `templates/base/base.html`: search form in sidebar
- `post/urls.py`: new search URL pattern
