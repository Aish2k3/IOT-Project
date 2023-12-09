# IoT Project for Checking Infestation Level in Trees

## Overview

This IoT project is designed to monitor and assess infestation levels in trees. The system utilizes Flask for the backend, React for the frontend, and MongoDB as the database. Docker is implemented for streamlined deployment and hosting. The primary objective of this application is to provide a user-friendly interface for visualizing sensor data, enabling users to gauge the infestation levels accurately. Additionally, the project facilitates the uploading of sensor data from an ESP32 device using Postman.

## App Stack

- Flask
- React
- MongoDB

## Deployment

The application is containerized using Docker for straightforward deployment. To install and run the application, follow the steps below.

### Prerequisites

- Docker
- Git

### Installation

1. Clone the Git repository:

   ```bash
   git clone https://github.com/Aish2k3/IOT-Project
   ```

2. Navigate to the project directory:

   ```bash
   cd IOT-Project
   ```

3. Use the `docker-compose.yml` file to compose and run the application:

   ```bash
   docker-compose up -d
   ```

   This will download the necessary images, build the containers, and start the application.

### Usage

Access the web application by navigating to:

- Website: [http://localhost:8000](http://localhost:8000)

To upload sensor data via ESP32, use Postman:

- Postman URL: [Collection](https://drive.google.com/file/d/1_sSjuzkiFKvGsJOgwJBam1Yct58eC8qK/view?usp=sharing)

### Additional Information

- The MongoDB database is employed for storing and managing sensor data.
- The Flask backend serves the React frontend to offer a seamless user experience.
- The application is hosted using Docker, ensuring consistent deployment across different environments.

Feel free to explore the codebase and customize it to suit your requirements. If you encounter any issues, refer to the project's documentation or open an issue on the [GitHub repository](https://github.com/Aish2k3/IOT-Project).

Happy coding!
