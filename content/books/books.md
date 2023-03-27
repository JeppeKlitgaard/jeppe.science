---
widget: book_portfolio
headless: true  # This file represents a page section.

weight: 20

# ... Put Your Section Options Here (title etc.) ...
title: ''
subtitle: ''

content:
  # Choose which content to display in the widget
  filters:
    # Folders to display content from
    folders:
      - "book_notes"
    # Uncomment below to only show content with specific tags:
#    tags:
#      - Machine Learning
    # Uncomment below to exclude content with specific tags:
#    exclude_tags:
#      - preface    
    # Uncomment below to show specific Hugo Page kinds
    kinds:
      - page
#      - section

  # Field to sort by, such as Date or Title
  sort_by: 'Date'
  sort_ascending: false

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove toolbar, delete/comment all instances of `filter_button` below.
  filter_button:
    - name: All
      tag: '*'
    - name: Non-Fiction
      tag: Non-Fiction
    - name: Essay
      tag: Essay
    - name: Literary Criticism
      tag: Literary Criticism
    - name: Fiction
      tag: Fiction
    - name: Science Fiction
      tag: Science Fiction
    - name: Surreal
      tag: Surreal
    - name: Humour
      tag: Humour
    - name: Dystopian
      tag: Dystopian
    - name: Political
      tag: Political
    - name: Classic
      tag: Classic
    - name: ⭐⭐⭐⭐⭐
      tag: ⭐⭐⭐⭐⭐
    - name: ⭐⭐⭐⭐
      tag: ⭐⭐⭐⭐
    - name: ⭐⭐⭐
      tag: ⭐⭐⭐
    - name: ⭐⭐
      tag: ⭐⭐
    - name: ⭐
      tag: ⭐

  # Default filter toolbar button (e.g. 0 corresponds to the first `filter_button` instance above)
  filter_default: 0

design:
  # Choose how many columns the section has. Valid values: '1' or '2'.
  columns: '1'
  # Choose a listing view
  view: masonry_reviewable
  # For Showcase view, flip alternate rows?
  flip_alt_rows: false
---
