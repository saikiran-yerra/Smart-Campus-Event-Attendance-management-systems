# smart-campus-Event-Attendance-Management-System

# Project Proposal

# Sai Kiran Yerramaneni

# Software Testing Principles & Techniques

# Harrisburg University

# Prof. Khalid Lateef

# May 26, 2026

# Smart Campus Event & Attendance Management System

# System Overview and Problem Definition

The proposed system is a Smart Campus Event & Attendance Management System for
colleges and universities to plan events, register students, maintain attendance and suggest
intelligent suggestions for events. There are still many educational institutions using a
spreadsheet, paper attendance sheets, or standalone applications to organize workshops,
seminars, technical events and student activities. These approaches can result in conflicts,
inaccurate attendance, ineffective communication, and reduced student involvement. The system
will offer centralized platform for efficient interaction between administrators, faculty
coordinators and students. Students will be able to view events, register online, get reminders
and view participation history. Faculty and administrators can create events, approve
registrations, keep track of attendance, and report. Later versions also feature recommendations
based on AI, which enhance the participation process and keep students engaged by
recommending events based on their interests and participation history.
The intended users include:
• College administrators
• Faculty event coordinators
• Students
• Department heads
The project scope is realistic for semester development because the system can be implemented
incrementally while demonstrating meaningful software evolution across versions.
# Major System Features

# 1. User Authentication and Role Management

Students and administrators will be able to register and log in securely in the system. Each role
will have access to various permissions in the system. For instance, administrators can create and
run events, students can only register for events and view their participation history. This is
crucial for providing access control and safeguarding sensitive student or event information.
# 2. Create and schedule events

Administrators and faculty coordinators will be able to add events with the following
information: event title, venue, time, category, capacity, and description. Upcoming events will
be organized on a dashboard displayed in the system. This feature helps in resolving the
scheduling and communication issues by enabling the institution to have a centralized workflow
for managing events (Ricci et al., 2022).
# 4. Notifications & Reminders System

Automated notifications and reminders will be sent via email or SMS APIs for upcoming events,
registration deadlines and schedule changes. This feature enhances students' engagement and
helps in prompt communications between student and administration.
# 5. AI-powered Event Recommendation Engine

The advanced version of the system will feature intelligent recommendations, which will
recommend events to the students based on their department, interests, and previous usage. The
recommended module can be provided with basic machine learning or third-party AI APIs. This
feature makes the system “smart” as it offers adaptive decision support and personalized
recommendations, not just static data processing.
# 6. Analytics and Reporting Dashboard

Administrators will have access to reports that will provide attendance information, participation
trends, popular event categories, and levels of student engagement. This feature is useful for the
institutional decision making and for the department to assess the effectiveness of the campus
activities.
Versioning and Incremental Development
Version 1 – Core Event Management System
The first version will focus on building the foundational workflows required for campus event
management.
# Features Included

• User authentication and role management
• Event creation and scheduling
• Student event registration
• Basic attendance tracking
• Event dashboard and search functionality
Purpose of Version 1
This version establishes the primary operational workflow of the system. Users will already be
able to manage events digitally and replace manual registration processes.
Testing for Version 1
Complete system testing will include:
• Login and authentication testing
• Registration workflow testing
• Event creation validation
• Attendance tracking accuracy testing
• Database integration testing
The testing complexity in Version 1 is moderate because the system mainly handles CRUD
operations and user interactions (Ricci et al., 2022).
Version 2 – Intelligent Automation and Analytics
The second version will introduce advanced functionality that significantly changes system
behavior and improves decision-making capabilities.
# New Features Added

• AI-based event recommendation engine
• Automated notification and reminder system
• Analytics and reporting dashboard
• Participation trend analysis
• Enhanced attendance verification using QR codes
Purpose of Version 2
This version transforms the system from a basic management application into an intelligent
engagement platform. The workflow becomes more adaptive because the system actively assists
users through recommendations and automation.
Testing for Version 2
# Complete system testing will include:

• Recommendation accuracy testing
• Notification delivery testing
• QR code attendance validation
• Performance and scalability testing
• Security and API integration testing
Testing complexity increases significantly because Version 2 introduces AI-assisted logic,
external APIs, and automation features that require integration and performance validation.
Smart / Intelligent System Justification
The system qualifies as an intelligent system because it includes AI-assisted recommendations
and automated communication features. Instead of simply storing event data, the software
analyzes user behavior and participation history to recommend relevant events. External APIs
may also be used for email notifications and machine learning support. These intelligent features
improve user engagement and help students discover activities aligned with their interests and
academic goals.
Engineering Practices
Project Risks
Several project risks have been identified:
• Integration issues between frontend, backend, and database systems
• Notification API reliability problems
• Security risks related to student data storage
• Limited training data for recommendation accuracy
# Version-Specific Risk

A major Version 2 risk involves the AI recommendation engine. Recommendation quality may
be poor if participation data is insufficient or inconsistent. This could reduce the usefulness of
intelligent suggestions. Risk mitigation strategies include using simplified recommendation
algorithms initially and testing with sample datasets (Dennis et al., 2020).
# Version Control and Change Management

The project will use Git and a GitHub repository for version control. All major changes will be
committed with descriptive commit messages, and separate branches will be used for feature
development and testing.
The change control process will include:
1. Feature planning
2. Development in a separate branch
3. Testing before merge
4. Code review and documentation updates
5. Final integration into the main branch
The instructor will be granted repository access to review progress, version history, and project
evolution throughout the semester.
# Conclusion

The Smart Campus Event & Attendance Management System addresses important
challenges in campus event coordination, attendance management, and student engagement. The
project demonstrates meaningful incremental development through two clearly defined versions,
each introducing substantial new functionality. The proposal also reflects awareness of testing
complexity, project risks, AI-assisted features, and software engineering best practices (Dennis et
al., 2020).
##  References

> **Ricci, F., Rokach, L., & Shapira, B. (2022).**  
> *Recommender Systems Handbook* (3rd ed.). Springer.

> **Dennis, A., Wixom, B. H., & Tegarden, D. (2020).**  
> *Systems Analysis and Design: An Object-Oriented Approach with UML* (6th ed.). Wiley.
