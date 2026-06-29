# GadgetGlobe E-commerce

<u>**OSTAD Exam Project:**</u> A single vendor e-commerce (_GadgetGlobe_) for budget PCs, AI workstations, servers, laptops including other technology products. It's a server-side rendering app developed in the monolith architecture.

## How to Setup

<u>**Setup Python Virtual Environment**</u>

\# Create virtual environment inside the project directory.

    python -m venv env

\# Activate the virtual enviroment.

    Windows (CMD): .\env\Scripts\activate

    Windows (bash): source env/Scripts/activate

    MacOS/Linux: source env/bin/activate

\# Install the dependencies from "**requirements.txt**" file.

    pip install -r requirements.txt

<u>**Setup Dockerized PostgreSQL Server**</u>

⚠️ **Required:** Docker

\# Download the latest docker image for PostgreSQL.

    docker pull postgres:latest

\# Use the following command to spin up a dockerized PostgreSQL server with required credentials.

    docker run -d
        --name gadget-globe
        -e POSTGRES_DB=gadget_globe
        -e POSTGRES_USER=gadget_globe_admin
        -e POSTGRES_PASSWORD=secret
        -p 5430:5432
        -v "path/to/host/machine/:/var/lib/postgresql"
        postgres:latest

💡 <u>**Note:**</u> <br/>

1. To avoid any port conflict with PostgreSQL running inside the host machine (_if any_), we mapped the container's port to a different host port (_5430_). <br/>
2. Check if the dockerized PostgreSQL is successfully configured. [<u>**APPENDIX-1**</u>](#1-health-check-of-a-dockerized-postgresql)

<u>**Configure .env File**</u>

\# Create a ".env" file inside the project's base directory.

\# Define the values accordingly to the following keys inside the file.

    # Django
    SECRET_KEY=""
    DEBUG=

    # Database
    DB_ENGINE=""
    DATABASE=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=

<u>**Run Development Server**</u>

\# Run the "**run_changes.sh**" bash script in the terminal for automating the execution of database migration commands & eventually run the server in development mode at **port 8080** in the host machine.

    bash run_changes

\# Navigate to a browser and enter the following URL to view the web application.

    http://127.0.0.1:8080/

## High Level Design (HLD)

1. Entity-Relationship (ER) diagram | [Link](./doc-resources/diagrams/erd.md)

## Low Level Design (LLD)

## Future Upgrades

## Objectives

## Technical Requirements

1. **Language:** Python 3.8 or latest

2. **Framework:** Django

3. **Containerization:** Docker

4. **Database:** PostgreSQL

5. **Security:** All secret keys (_i.e. Django SECRET_KEY, Stripe keys_) should be stored in a "**.env**" file inside the project directory and list it in **.gitignore**.

6. **Dependencies:** A requirements.txt file enlisted all dependencies.

## Submission Requirements

- You have to upload the project code to a GitHub repository.
- Include a **README.md** explaining how to set up and run the project locally (install steps,
  how to add the Stripe test keys, and how to run migrations and start the server).
- Make sure your .env file (with real keys) is NOT committed. Instead, provide a .env.example
  file showing which variables are required.
- **Optional:** You can deploy the project and submit the live project link. - Deployment can be done using OnRender or PythonAnywhere, but it is not
  mandatory.
- Submit at least:
  - GitHub Repository Link
  - If deployed, submit the Live Deployed Website Link as well.

## Evaluation Criteria

Your submission will be evaluated on the following:

- Working authentication (register / login / logout).
- Correct product, category, cart, and order models and relationships.
- A fully working Stripe test payment that creates an order only on success.
- Correct stock handling and order history for the logged-in user.
- Clean code, a working Admin panel, and a clear, usable frontend.
- Secrets kept out of the repository (no hard-coded Stripe/Django keys).

## APENDIX

### [1] Health check of a dockerized PostgreSQL

- Inside the terminal, execute the following `docker exec` command with extra parameters to enter into the PostgreSQL server inside the docker container.

        docker exec -it gadget-globe psql -U gadget_globe_admin -d gadget_globe

  Docker CLI will prompt for the password. Provide the password defined in the section "**Setup Dockerized PostgreSQL Server**".

If the PostgreSQL docker container is accessible using the aforementioned command, it ensures the docker container is created successfully.
