# FastAPI Crypto Price Tracker

This is a FastAPI application that allows users to create an account and track prices of various cryptocurrencies. It utilizes JWT token authentication, SQLAlchemy for database management, and AIOHTTP for making asynchronous requests.

## Features

- User Registration: Users can create an account by providing a unique username and password.

- JWT Token Authentication: Registered users can obtain a JWT token by authenticating with their credentials. This token is used for subsequent API requests to authenticate and authorize the user.

- Cryptocurrency Price Tracking: Authenticated users can add cryptocurrencies to their watchlist and retrieve the latest prices of those cryptocurrencies.



## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/thiagoxavieraguilar/FastAPI-Crypto.git
   
   ```

2. Navigate to the project directory:

   ```shell
   cd FastAPI-Crypto/backend
   ```

3. Run the Makefile to set up the environment and dependencies, format the code, and run tests:

   ```shell
   make
   ```

4. The API will be accessible at `http://localhost:8000`.


## Dockerfile and Docker Compose

If you prefer to run the application using Docker, you can use the provided Dockerfile and Docker Compose files.

1. Build the Docker image:

   ```shell
   docker build -t fastapi-app-crypto .
   ```

2. Start the containers:

   ```shell
   docker-compose up
   ```
Please ensure that Docker and Docker Compose are installed and properly configured before running the above commands.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your forked repository.

5. Submit a pull request with a detailed description of your changes.



Feel free to customize and extend this application to meet your specific requirements.

If you have any questions or need further assistance, please feel free to reach out.
