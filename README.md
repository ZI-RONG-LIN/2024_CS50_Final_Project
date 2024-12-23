# Gym Member Management System
#### Video Demo:  https://youtu.be/uWWgx2XZvuw
#### Description:
Due to the wide range of facilities and multiple fitness trainers that gyms often provide for members to choose from, training plans for members usually rely on communication and collaboration among trainers. However, this approach can easily lead to inconsistencies or missing information, which may disrupt training continuity and affect the member experience.

To address these issues, I designed the Gym Member Management System, a membership management tool specifically created for gym managers and fitness trainers. This system offers a centralized platform where trainers can record members’ personal information, training programs, and progress. Not only does it effectively reduce the time spent on communication among trainers, but it also maintains a comprehensive record of each member’s training history. This enables trainers to create personalized training plans tailored to individual members' needs and historical data.

This system aims to enhance the professionalism and efficiency of trainer services, improve member satisfaction, and ultimately boost the operational efficiency and customer experience of the gym.

## Function
* **Register**: Administrators or trainers can register a new account.
* **Login**：Administrators or trainers can log in by providing their account credentials.
* **Member Data Management**：Administrators or trainers can add new member profiles, as well as view and delete existing members' basic information.
* **Training History**：Displays each member's past training plans, schedules, and activities.
* **Training Records**：After a member completes a training session, administrators can record the relevant date and activities, facilitating ongoing tracking of training progress.

## Installation

1. Clone the repository：
    ```bash
    git clone https://github.com/123/gym-member-management.git
    ```

2. Start the Flask server：
    ```bash
    python app.py
    ```

3. Open your browser to access the application

## Technical Details and Architecture
This system utilizes a combination of robust backend and frontend technologies to deliver an efficient and user-friendly experience:

* Backend: Built with Flask, the system handles CRUD (Create, Read, Update, Delete) operations for managing account data, member data and training records.

* Database: SQLite is used as the database to store account information, member profiles, training history, and other related information securely.

* Frontend: The user interface and system functionality are implemented using HTML, CSS, and JavaScript, enhanced by Bootstrap to ensure responsive design and visually appealing layouts across devices.

## HTML Page Design Concepts
The system features a thoughtful design for each major module:
* **Register**: When the user enters a username, the system checks if the username is already in use. If it exists in the database, a red warning message is displayed to notify the user.

* **Login Page:**
A clean form is designed with input fields for username and password, along with a login button. The background features a gradient color scheme to create a more dynamic and engaging look.

* **HomePage:**
    * Displays a member list with "Add member" and "Delete" buttons. When hovered over, the buttons darken for intuitive interaction.

    * A confirmation mechanism is implemented to prevent accidental deletion of member data.

    * Hovering over member names underlines them to aid navigation.

    * A logout button is added in the top-right corner for easy exit after completing tasks.

* **Member Page:**
The upper section displays member-related information, while the lower section shows past training records, including dates, activities, targeted areas, weights, repetitions, and sets. Each training session is separated into cards for easy identification. Buttons for adding new training activities and returning to the member list are included for seamless operation.

* **Add Member Page:**
Collects four fields: name, date of birth, gender, and contact information. The date of birth can be selected via a calendar, and gender is chosen from a dropdown menu to ensure consistent formatting. All fields are mandatory, with reminders appearing for any missing data when the "Add Member" button is clicked.

* **Add Training Activity Page:**
Records training details, including date, activity, targeted areas, weights, repetitions, and sets. Drop-down menus are provided for most fields, except for weights and sets, to reduce input complexity and ensure uniformity. Missing fields trigger reminders to guide users.

## Future Development Plans
To further improve the system, the following features could be added:

* **Detailed Analytics:** Create pages with visual charts analyzing member participation rates and trainer workloads.

* **API Integration:** Provide an API for integration with other systems or mobile app development.

* **Data Edit:** Enable users to edit member information or training records.

## Use Cases
* "Trainer A records Member B’s training progress. If Trainer A is unavailable, Trainer C can quickly review the member’s capabilities and needs, ensuring continuity in training plans."

* "The gym manager uses the system to track member participation trends and analyze popular training programs, enabling optimized services and new offerings."

## Lessons Learned and Challenges
* **User Experience (UX)**

While CSS and Bootstrap facilitate a more visually appealing design, significant time was spent fine-tuning elements and verifying their appearance. Small features, such as button color changes and underlines, though simple, brought immense satisfaction upon completion.

* **Database Design**

Initially, I failed to clearly define the fields needed for each page, resulting in frequent adjustments to the database schema. This inefficiency highlighted the importance of thorough requirements analysis before starting development.

This project has been a valuable learning experience, especially as someone new to system development. Despite challenges, the process of creating this system has been both educational and rewarding.
