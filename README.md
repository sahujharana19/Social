# Social Video Upload – Django Project

## Project Overview
This is a **Django-based video upload application** designed to allow users to upload, manage, and store video files efficiently. The project demonstrates backend development skills, problem-solving abilities, secure file handling, and proper project configuration in Django. The codebase initially contained some issues, which were identified and resolved, highlighting practical debugging and maintenance experience.

---

## Features
- **Video Upload Functionality:** Users can upload video files via the web interface.
- **Database Integration:** Uses SQLite with Django ORM to store video metadata.
- **Secure File Handling:** Safe access to uploaded files prevents server crashes due to missing files.
- **Media Configuration:** Correctly configured `MEDIA_ROOT` and `MEDIA_URL` to serve media files during development.
- **CSRF Protection:** Proper usage of the `csrf_exempt` decorator to handle requests safely.
- **Error Handling:** Returns meaningful error responses when uploads fail or files are missing.

---

## Project Structure
social_project/
│
├── db.sqlite3 # Database file
├── manage.py # Django management script
├── requirements.txt # Required Python packages
├── media/ # Folder for uploaded video files
├── social_uploader/ # Django project settings
└── uploader/ # Django app containing models, views, and templates

Skills Demonstrated

Python & Django Development: Views, models, URL routing, CSRF handling

Database Management: SQLite with Django ORM and migrations

Secure File Handling: Preventing MultiValueDictKeyError and handling missing files

Media Management: Correct configuration of media files in Django

Debugging & Problem Solving: Identified and fixed CSRF, database, and media serving issues

Project Organization: Clean separation of apps, project settings, and static/media files

Outcome

The application successfully handles video uploads, stores files in the media folder, and maintains database entries for each upload. This project highlights practical experience with Django debugging, backend development, and full-stack application understanding.

Author

Jharana Sahu
Aspiring Frontend/Full-Stack Developer | Python & Django Enthusiast
