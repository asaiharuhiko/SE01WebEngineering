## Context

The blog spec requires three search modes: text (title contains), date (calendar day click), and author (author link click). All three should display results using the existing `list.html` format with pagination. A header like "search: keyword" appears above the results.

Currently:
- `list.html` uses relative `?page=X` links which lose search params on pagination
- No search selectors exist
- `search.html` is empty
- Calendar day links point to `/?date=YYYY-MM-DD` but nothing handles that param

## Goals / Non-Goals

**Goals:**
- Text search: type a query, see posts with matching titles
- Date search: click calendar day, see posts from that day
- Author search: click author name, see their posts
- All three reuse `list.html` with correct pagination
- Header displays search type and value

**Non-Goals:**
- Full-text search across content (only title matching per spec)
- Search result highlighting
- Advanced filters (tag, category, etc.)
- Autocomplete or search suggestions

## Decisions

1. **Query params on index URL** — `GET /?search=X`, `GET /?date=X`, `GET /?author=X` instead of separate search endpoints. Keeps URL structure flat and allows IndexView to handle all cases.

2. **`base_url` for pagination** — Pass a `base_url` context variable (e.g., `/?search=django`) to `list.html` so pagination links append `&page=X` correctly. This solves the relative URL problem.

3. **`search_header` in list.html** — Add an optional `search_header` variable. If present, render it above the post list. If absent (normal index), render nothing.

4. **Reuse index template for search results** — Search results render the same `index.html` template with `search_header` and filtered posts. No separate search template needed.

## Risks / Trade-offs

- **[Pagination param collision] →** Using `base_url` with `&page=X` is clean but requires passing the variable through all views that use `list.html`. Addressed by always including `base_url` in context.
- **[Calendar click dual update] →** Clicking a calendar day currently only updates the calendar via HTMX. To also update the post list, a separate HTMX request would be needed. Out of scope for this change; can be added later.
