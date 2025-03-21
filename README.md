# Flask Application

This is a basic Flask application designed for deployment on Azure Web App.

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   └── routes.py
├── requirements.txt
├── runtime.txt
├── web.config
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application locally, use the following command:
```
flask run
```

### Deployment

Follow the Azure documentation to deploy the application to Azure Web App. Ensure that the `runtime.txt` and `web.config` files are correctly configured for your environment.

### License

This project is licensed under the MIT License - see the LICENSE file for details.