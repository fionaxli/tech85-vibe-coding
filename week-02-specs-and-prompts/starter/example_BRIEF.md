# Project BRIEF: Daily Habit Tracker

## What I'm building
A personal web app where I can define a list of daily habits (e.g., "Drink 8 glasses of water," "Read for 20 minutes," "Walk 10,000 steps") and check them off each day. The app should show me a simple streak count — how many consecutive days I have completed each habit — so I can see my consistency over time. I will use it every morning on my laptop. No one else needs to log in.

## Core features (must-have)
- Add a new habit by typing its name and clicking a button
- See all my habits listed with a checkbox for today
- Check off a habit; that check should persist if I close and reopen the browser
- See the current streak (consecutive days completed) next to each habit
- Remove a habit I no longer want to track

## Out of scope (not building this)
- User accounts or login — this is just for me, no authentication needed
- Mobile app — desktop browser only
- Reminders or notifications
- Sharing or social features
- Historical charts or graphs — just the streak number is fine for now

## Example interaction
Input: I type "Meditate 10 minutes" into the text box and click the "Add Habit" button.
Output: A new row appears in my habit list with the text "Meditate 10 minutes," an unchecked checkbox, and "Streak: 0 days."

Another example:
Input: I check the checkbox next to "Read for 20 minutes."
Output: The checkbox shows as checked, the row updates to "Streak: 1 day." If I have checked it every day for 5 days, it shows "Streak: 5 days."

## Technical constraints
- Language: Python 3.10+
- UI: Streamlit
- Data: SQLite (one local file, `habits.db`) — no cloud database
- External services: none
- Must run: locally on my laptop AND deployed to Streamlit Cloud so I have a real URL

## Done means...
- I can add a habit and it appears in the list immediately
- After checking off a habit and refreshing the page, it is still checked
- If I close the app entirely, restart it, and open the browser again, all my habits and check states are still there
- The streak count increments correctly: 0 on day 1, 1 on day 2 (if I checked day 1), and resets to 0 if I miss a day
- I can delete a habit and it disappears from the list permanently
