# LeetTracker
> Excellence demands effort and planned, deliberate practice of increasing  difficulty. -K. Anders Ericsson

Solved countless hard Leetcode problems but can't get past the FAANG assessments? Ever had the feeling where you have seen a problem before, but forgot the approach and thought process behind it? Introducing LeetTracker! LeetTracker is a web application designed to help users track their progress and record notes on coding challenges, specifically from LeetCode. The application allows users to create, edit, and manage their coding problem entries, organize them by topic, and review their solutions and notes. Users can filter and sort problems based on difficulty and solved status, and even revise a random problem directly from the dashboard.

## Distinctiveness and Complexity

### Distinctiveness
LeetTracker is an original idea developed from scratch, and is distinct in its functionality compared to the other CS50W projects, as it as a progress-tracking/note-recording webapp. There are brand new features that are not seen before, such as the ability to filter problem entries by their characteristics, and some that were inspired by previous projects (retrieving a random instance for the user) but modified to suit the context of the project both for the user and the project structure. The application provides a user-friendly interface for organizing problems by topics, which are dynamically created by users. The problem display includes features like a collapsible topic section and sorting/filtering functionality.

### Complexity
LeetTracker exhibits complexity through various aspects:
- **Dynamic Content:** The application handles dynamically generated topics and allows users to filter, sort, and view problems based on specific criteria.
- **JavaScript Integration:** The app integrates JavaScript for functionalities like dropdowns, sorting, filtering, and fetching random problems, ensuring a seamless user experience.
- **Custom Problem Display:** The detailed problem display page includes a solution section with code formatting, complexity analysis, and notes, all styled consistently for readability.
- **Session Management:** User authentication and session management allow personalized interaction with the app, maintaining user-specific data like saved problems and session states.

## File Structure and Details

### Backend
#### `leettracker/`
- **`views.py`**: Contains all the view functions for rendering templates, handling form submissions, and managing user interactions.
- **`urls.py`**: Maps URLs to view functions, defining the different routes within the application.
- **`models.py`**: Contains the database models, representing the problem and topic entities.

### Frontend
#### `leettracker/`
- **`static/leettracker`**: Contains all JavaScript files for handling dynamic behaviors such as filtering, sorting, dropdowns and tab displaying, and CSS files that dictate the styling and strcuture of aesthetic elements in the UI.
- **`templates/leettracker/`**: Contains all the HTML templates, including:
    - `displayproblem.html`: The page template for displaying a single problem entry in detail, similar to LeetCode's style to introduce fmailiarity and readability.
    - `formbase.html`: The page template for displaying the form when keying in a new entry or  editing an entry. This is inherited by:
        - `editproblem.html`
        - `newentry.html`
    - `index.html`: The home page template with the random problem revision feature.
    - `layout.html`: Base template that includes common elements like navigation and scripts.
    - `login.html`: Page structure for the login page.
    - `myproblems.html`: Displays the list of problems the user has saved, and features the dynamic filtering and sorting features which is achieved with JavaScript.
    - `problem_display_partial.html`: Template for displaying problem details in a collapsible format for the random problem feature.
    - `problemsbytopic.html`: Template for displaying problem entries for specific topics.
    - `register.html`: Page structure for the register page.
    - `selectbytopic.html`: Page template for displaying all available, navigable topic pages.

## How to Run the Application

1. **Install Dependencies**: Make sure you have Django installed. You can install the necessary packages using:
    ```pip install -r requirements.txt```

2. Clone this repository on your Desktop. cd into the directory using:
    ```cd Desktop/LeetTracker```

3. **Run migrations to set up the Database**: First, run:
    ```python manage.py makemigrations```
    Then, run:
    ```python manage.py migrate```

4. **Run the server**:
   ```python manage.py runserver```

5. Go to the link provided on your command terminal, and start LeetTracking!

## Additional Information

