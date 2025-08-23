SELECT column_name, column_type
FROM information_schema.columns
WHERE table_schema = 'alx_book_store'
  AND table_name = 'books';
