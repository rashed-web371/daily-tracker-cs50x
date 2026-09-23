# Daily Tracker

#### Video Demo: https://youtu.be/6NvFqLllS_4

#### Description:
Daily Tracker is a comprehensive yet minimal web-based task management application designed to help individuals maintain focus, organize their daily routines, and keep track of productive habits. In an era where modern task management tools are often overloaded with complex settings, integrations, and distracting elements, Daily Tracker aims to provide a clean, distraction-free environment that prioritizes speed, usability, and essential functionality.

### Project Motivation and Background
The motivation behind developing Daily Tracker was to address personal productivity challenges. Many existing to-do applications require complicated initial configurations, multiple workspaces, and cumbersome navigation. The goal here was to design a single-page web dashboard where a user can enter a task, assign it to a category, mark it as done, or delete it in just a few clicks. This project serves as my capstone implementation for CS50x, applying the core programming paradigms learned throughout the course, including backend development with Python, web server architecture using Flask, structured relational database storage with SQLite, and responsive front-end interface design using HTML, CSS, and Bootstrap.

### Project Architecture and File Structure
The project is structured into distinct, modular files that separate backend logic, data persistence, presentation templates, and styling:

* **`app.py`**:
  This is the core Python backend of the application built on the Flask framework. It establishes the database connection, handles HTTP requests, and directs data flow through several primary routes:
  * `@app.route("/")`: Queries the SQLite database to fetch all existing tasks ordered from newest to oldest, and passes the resulting records directly to the dashboard template.
  * `@app.route("/add", methods=["POST"])`: Processes form submissions. It validates user inputs to ensure neither the task description nor category is empty, inserts the new record into the database, and redirects back to the index view.
  * `@app.route("/toggle/<int:item_id>", methods=["POST"])`: Finds the task by its unique identifier and flips its completion state (from pending to completed, or vice versa), allowing users to mark tasks done or re-open them.
  * `@app.route("/delete/<int:item_id>", methods=["POST"])`: Permanently removes the selected record from the database table based on its primary key.

* **`final.db`**:
  A lightweight SQLite database containing the main `items` table. It tracks every submitted task with fields for a unique integer primary key (`id`), the task string (`task`), its selected category (`category`), a boolean flag (`completed`), and an automated timestamp (`created_at`).

* **`templates/layout.html`**:
  The foundational Jinja base template that provides standard HTML5 boilerplate markup, page metadata, viewport configurations for mobile responsiveness, and imports Bootstrap 5 via CDN. It defines the main content block that downstream templates extend.

* **`templates/index.html`**:
  The user-facing dashboard template. It extends `layout.html` and implements the card-based user interface. It contains the interactive task creation form with category selectors (such as Health, Work, Study, and General), dynamic alerts, and an iteration loop over all stored tasks, presenting action buttons for toggling and deleting items.

* **`static/styles.css`**:
  A lightweight custom CSS stylesheet that enhances Bootstrap's default styles. It fine-tunes margins, borders, button states, strikethrough decorations for completed tasks, and layout spacing to achieve a modern and balanced visual aesthetic.

* **`requirements.txt`**:
  Specifies the external Python dependencies required to run the application within an isolated environment, primarily `Flask` and the `cs50` library.

### Design Choices and Considerations
During development, several key design decisions were made to prioritize performance and maintainability:
* **Bootstrap 5 Framework**: Chosen over writing purely custom CSS to ensure robust responsive layout behavior across smartphones, tablets, and desktop browsers without unnecessary styling bloat.
* **CS50 SQL Wrapper**: Leveraged the `cs50` SQL module to ensure clean query parameterization, effectively preventing SQL injection vulnerabilities while keeping database interactions clear and readable.
* **Single-Dashboard User Flow**: Rather than splitting creation, editing, and listing across separate pages, all actions redirect to the main view, providing immediate visual feedback and a streamlined user experience.

### How to Run the Application
1. Ensure all required Python dependencies are installed:
   ```bash
   pip install -r requirements.txt

Start the Flask application server:

Bash
flask run

Open the generated local development server URL in any web browser to access and interact with the application.
