

# SmartHospital

**SmartHospital** is an intelligent health monitoring platform built with Django, designed for use in hospitals and clinics. This system enables healthcare professionals to monitor patients’ vital signs in real-time using data from devices like smartwatches. It also sends automatic alerts to the medical team when anomalies are detected, helping to prevent health crises and optimize patient care.

<img width="1680" alt="Capture d’écran 2024-10-24 à 10 40 27 PM" src="https://github.com/user-attachments/assets/64e544f2-56d2-4880-8b13-46f0252056b0">


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

**SmartHospital** centralizes and analyzes data such as heart rate, blood pressure, blood oxygen level, and temperature, offering a complete and continuous view of the patient’s health. Leveraging Machine Learning, the system can predict medical emergencies and support data-driven clinical decisions.

<img width="1680" alt="Capture d’écran 2024-10-24 à 10 51 18 PM" src="https://github.com/user-attachments/assets/b4639f74-e0fd-4c72-ad5c-e3a55ef5a9ac">




---

## Features

- **Real-Time Monitoring**: Receives and displays patient data in real-time.
- **Automatic Alerts**: Notifies the medical team when any vital sign exceeds safe thresholds.
- **Health History Visualization**: Stores historical data for future reference.
- **Automated Reports**: Generates reports to support clinical analysis.
- **Health Crisis Prediction**: Uses AI algorithms to predict potential emergencies.



---

## Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL or MySQL
- **Frontend**: Django Templates (or React.js/Vue.js for a more interactive interface)
- **API for Device Communication**: Django REST Framework
- **Machine Learning**: AI models for predictive data analysis

---
<img width="1680" alt="Capture d’écran 2024-10-24 à 10 54 19 PM" src="https://github.com/user-attachments/assets/aac11999-c54b-47fc-bb07-1dca2b60b668">

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/SmartHospital.git
   cd SmartHospital
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**: Create the database in PostgreSQL or MySQL, and configure the credentials in the `settings.py` file.

<img width="1680" alt="Capture d’écran 2024-10-24 à 10 43 01 PM" src="https://github.com/user-attachments/assets/78d7555e-3cbf-4a3c-9ca9-5519d175b09d">



5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the server**:
   ```bash
   python manage.py runserver
   ```

---

## Configuration

1. **Device Configuration**: To receive data from devices, set up the REST API module using Django REST Framework and integrate it with the device’s API.
2. **AI Configuration**: Load or configure Machine Learning models in the dedicated AI module for predictive analysis.

---

## Usage

1. **Access the Dashboard**: Log in to the admin interface (`http://localhost:8000/admin`) to manage the system and view data.
2. **Patient Monitoring**: Access the monitoring dashboard to track patients’ vital signs.
3. **Alerts**: Receive real-time alerts and view AI-based recommendations.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b my-feature`).
3. Commit your changes (`git commit -m 'Add my new feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

This README provides a detailed overview of **SmartHospital** and includes installation, configuration, usage, and contribution guidelines.
