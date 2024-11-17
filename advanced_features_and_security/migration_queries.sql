BEGIN;
--
-- Create model Author
--
CREATE TABLE "bookshelf_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL);
--
-- Create model Book
--
CREATE TABLE "bookshelf_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "author_id" bigint NOT NULL REFERENCES "bookshelf_author" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "bookshelf_book_author_id_b7811fba" ON "bookshelf_book" ("author_id");
COMMIT;
BEGIN;
--
-- Add field publication_year to book
--
CREATE TABLE "new__bookshelf_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publication_year" integer NOT NULL, "title" varchar(200) NOT NULL, "author_id" bigint NOT NULL REFERENCES "bookshelf_author" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__bookshelf_book" ("id", "title", "author_id", "publication_year") SELECT "id", "title", "author_id", 2000 FROM "bookshelf_book";
DROP TABLE "bookshelf_book";
ALTER TABLE "new__bookshelf_book" RENAME TO "bookshelf_book";
CREATE INDEX "bookshelf_book_author_id_b7811fba" ON "bookshelf_book" ("author_id");
COMMIT;
