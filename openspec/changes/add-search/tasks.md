## 1. Add search selectors

- [x] 1.1 Add `get_posts_by_query(query)` to `post/selectors.py`
- [x] 1.2 Add `get_posts_by_date(date_str)` to `post/selectors.py`
- [x] 1.3 Add `get_posts_by_author(author)` to `post/selectors.py`

## 2. Update list.html for search results

- [x] 2.1 Add optional `search_header` variable to `list.html`
- [x] 2.2 Add `base_url` variable for pagination links
- [x] 2.3 Ensure HTMX pagination preserves search params

## 3. Implement search view logic

- [x] 3.1 Create `SearchView` in `post/views.py`
- [x] 3.2 Route `?words=`, `?date=`, `?author=` to appropriate selectors
- [x] 3.3 Pass `search_header` and `base_url` to template context
- [x] 3.4 Handle HTMX requests for search results

## 4. Update templates

- [x] 4.1 Create `search.html` with `search_header` display
- [x] 4.2 Add search form to `base.html` sidebar
- [x] 4.3 Add `search/` URL pattern to `post/urls.py`

## 5. Verification

- [x] 5.1 `ruff check` passes
- [x] 5.2 `python manage.py check` passes
- [x] 5.3 Manual test: text search shows filtered results with header
- [x] 5.4 Manual test: pagination preserves search params
