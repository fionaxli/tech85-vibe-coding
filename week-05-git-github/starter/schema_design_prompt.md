# Schema Design with Claude Code

A schema is the blueprint for your database: which tables exist, which columns each table has, and what type of data each column holds. Getting this right before you start building saves a lot of refactoring later.

This guide walks you through designing a schema with Claude Code's help.

---

## The prompting formula

Tell Claude Code what you are building and what data you need to store:

> "I'm building [describe your project in one sentence]. I need to store [describe the data — what each 'record' represents, and what fields it has]. Help me design a SQLite schema. Show me the CREATE TABLE statements."

Be specific about the data. The more detail you give, the better the schema.

---

## Example exchange

**You:**
> "I'm building a weather journal app. Each entry records: the city the user looked up, the date, the temperature in Fahrenheit, a weather description like 'sunny' or 'rainy', and the user's personal notes about the day. Help me design a SQLite schema. Show me the CREATE TABLE statements."

**Claude Code:**
```sql
CREATE TABLE IF NOT EXISTS weather_entries (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    city        TEXT    NOT NULL,
    entry_date  TEXT    NOT NULL,  -- stored as 'YYYY-MM-DD'
    temp_f      REAL    NOT NULL,
    description TEXT    NOT NULL,
    notes       TEXT    DEFAULT '',
    created_at  TEXT    NOT NULL   -- stored as ISO 8601 timestamp
);

-- Index to make queries by city or date fast
CREATE INDEX IF NOT EXISTS idx_city_date
    ON weather_entries (city, entry_date);
```

**You (follow-up):**
> "What is the index for?"

**Claude Code:**
> "Without an index, SQLite reads every row when you search by city or date. The index lets it jump directly to matching rows — it makes searches dramatically faster as your table grows. For a personal app with hundreds of entries it probably does not matter, but it is a good habit."

**You (follow-up):**
> "What if the user wants to store multiple entries for the same city on the same date?"

**Claude Code:**
> "The current schema already allows that — there is no UNIQUE constraint on (city, entry_date). Each row gets a unique `id`, so multiple entries for the same city and date are fine. If you wanted to prevent duplicates, you would add: `UNIQUE(city, entry_date)`."

---

## Follow-up questions worth asking

After Claude Code gives you a schema, ask:

- "Should [column] be TEXT, INTEGER, or REAL?" — understand the data types
- "What does AUTOINCREMENT do?" — Claude Code will explain primary keys
- "When would I add a UNIQUE constraint?" — understand data integrity
- "What index should I add to make searches fast?" — understand performance
- "How do I handle [edge case] in this schema?" — probe your assumptions
- "Show me what an INSERT statement for this table would look like" — get a preview of how you will use it

---

## Common schema patterns

### Pattern 1: Entries with timestamps (most common)
Good for: notes, journal entries, habit logs, to-do items, weather records

```sql
CREATE TABLE IF NOT EXISTS entries (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    content    TEXT    NOT NULL,
    created_at TEXT    NOT NULL  -- ISO 8601: '2026-02-17T19:30:00'
);
```

### Pattern 2: User-defined items with status
Good for: reading lists, task trackers, wish lists

```sql
CREATE TABLE IF NOT EXISTS items (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    status     TEXT    NOT NULL DEFAULT 'pending',
    notes      TEXT    DEFAULT '',
    created_at TEXT    NOT NULL,
    updated_at TEXT
);
```

### Pattern 3: Key-value settings store
Good for: user preferences, app configuration

```sql
CREATE TABLE IF NOT EXISTS settings (
    key        TEXT PRIMARY KEY,
    value      TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
```

---

## Writing your schema to a file

Once you have agreed on a schema with Claude Code, write it to a `schema.sql` file in your project folder:

> "Write the final agreed schema to a file called schema.sql in my project folder."

This file serves two purposes:
1. Documentation — anyone (or any AI agent) can read it to understand your data model
2. A reference when you need to recreate the database — useful if you ever want to reset or migrate

Commit it:
```bash
git add schema.sql
git commit -m "Add schema.sql for Project 2 database design"
```
