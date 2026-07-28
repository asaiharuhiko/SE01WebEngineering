## Context

The sidebar calendar mechanism already existed in `base.html`, but `{% include %}` does not pass context variables to the included template. This meant `calendar_html`, `year`, `month`, and navigation variables were all empty on every page except when rendered directly by `CalendarView`. Additionally, `CalendarView` itself was missing the prev/next month variables needed by the template's navigation links.

## Goals / Non-Goals

**Goals:**
- Sidebar calendar renders correctly on all pages
- Prev/next month navigation links work
- `CalendarView` (`/calendar/year/month/`) continues to function
- Remove duplicate template blocks

**Non-Goals:**
- Calendar CSS styling
- Date-click filtering for blog posts
- Changing calendar display content

## Decisions

1. **Custom inclusion tag over context processor** — A template tag is the most localized and understandable approach. Adding `{% calendar %}` to `base.html` is all that's needed, with no changes to settings.py or individual views.

2. **Add prev/next context to CalendarView** — After removing the `{% if prev_month %}` guard from `calendar.html`, `CalendarView` must also provide these variables or the `{% url %}` tag will raise an error.

3. **Fix typo `calender_html` → `calendar_html`** — The original code had a misspelled variable name, corrected as part of this change.

## Risks / Trade-offs

- **[Template sharing] →** `calendar.html` is now rendered by both the inclusion tag and `CalendarView`. Both must supply an identical set of context variables. Addressed in this change.
