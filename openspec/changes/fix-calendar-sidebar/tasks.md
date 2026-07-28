## 1. Create template tag

- [x] 1.1 Create `post/templatetags/__init__.py`
- [x] 1.2 Define `calendar` inclusion tag in `post/templatetags/calendar_tags.py`

## 2. Update templates

- [x] 2.1 Replace `{% include %}` with `{% calendar %}` in `templates/base/base.html`
- [x] 2.2 Remove duplicate `<div class="calendar">` block in `templates/components/calendar.html`

## 3. Fix CalendarView

- [x] 3.1 Add prev/next month context variables to `CalendarView` in `post/views.py`
- [x] 3.2 Fix typo `calender_html` → `calendar_html`

## 4. Verification

- [x] 4.1 `ruff check` passes
- [x] 4.2 `python manage.py check` passes
