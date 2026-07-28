## Why

The sidebar calendar in `base.html` used `{% include "components/calendar.html" %}`, which only embeds the template without passing any context variables. As a result, `calendar_html`, `year`, `month`, and navigation variables were all empty, causing the calendar to render as nothing on every page except `/calendar/year/month/`.

## What Changes

- Created `post/templatetags/calendar_tags.py` with a `calendar` inclusion tag that generates a `BlogCalendar` for the current month and passes the full context to `calendar.html`
- Updated `templates/base/base.html` to use `{% load calendar_tags %}{% calendar %}` instead of `{% include %}`
- Simplified `templates/components/calendar.html` by removing a duplicate `<div class="calendar">` block
- Added prev/next month context variables to `CalendarView` in `post/views.py` (previously missing)
- Fixed typo: `calender_html` → `calendar_html`

## Capabilities

### Modified Capabilities
- `blogs`: Fixed sidebar calendar to display correctly on all pages

## Impact

- `post/templatetags/__init__.py`: new file
- `post/templatetags/calendar_tags.py`: new file
- `templates/base/base.html`: changed tag invocation
- `templates/components/calendar.html`: simplified template structure
- `post/views.py`: expanded CalendarView context
