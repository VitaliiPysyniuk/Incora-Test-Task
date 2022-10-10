![example workflow](https://github.com/VitaliiPysyniuk/Incora-Test-Task/actions/workflows/build.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/VitaliiPysyniuk/Incora-Test-Task/branch/main/graph/badge.svg?token=38hXXP3noF)](https://codecov.io/gh/VitaliiPysyniuk/Incora-Test-Task)
# Incora Test Task
<hr style="margin-top: 0"/>
<h3>Description</h3>
This is a simple REST API that provides endpoints to create new, list all and update existing users.
Almost all endpoints are protected with Bearer token authentication.<br/>
Also was used <code><b>python-socketio</b></code> package to implement Socket.io protocol in the application.
This protocol was implemented by adding the Socket.io server application wrapper of the Django application. 
This Socket.io server sends an event about user updating to all connected Socket.io clients.
<hr style="margin-top: 0"/>
<h3>Used technologies</h3>
<dl>
  <li>Django + Django REST Framework</li>
  <li>Simple JWT</li>
  <li>Socker.io</li>
  <li>PostgreSQL</li>
  <li>Docker + Docker Compose</li>
  <li>Pytest + Coverage</li>
</dl>

<hr style="margin-top: 0"/>
<h3>Requirements</h3>
Before running the application on your machine you need to have docker and docker-compose installed. 
The installation guide you can find <a href="https://docs.docker.com/desktop/">here</a>.
<br>Also you need to add .env and .env.db file to the root directory of the project.
<br>Example of <code><b>.env</b></code> file:
<pre>
<code><b>
TIME_ZONE=Europe/Kiev #your timezone
DEBUG=True 
SECRET_KEY='your-secret-key'
</b></code></pre>
Example of <code><b>.env.db</b></code> file:
<pre>
<code><b>
POSTGRES_DB=itt_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1111
POSTGRES_HOST=itt_database #this parameter must be the same because it refers to the docker container where the database will be running
POSTGRES_PORT=5432
</b></code>
</pre>
<hr style="margin-top: 0"/>
<h3>How to run application</h3>
To run application and its database in docker containers (you can add <code><b>-d</b></code> flag to run them in background)
<pre>
<code><b>docker-compose up </b></code>
</pre>
To stop and remove the docker containers where the application and its database run
<pre>
<code><b>docker-compose down</b></code>
</pre>
<hr style="margin-top: 0"/>
<h3>How to run tests</h3>
To run tests you have to create a virtual environment where all needed packages will be installed. Create virtual 
environment with the following command (provided example for the Linux OS):
<pre>
<code><b>python3 -m venv venv</b></code>
</pre>
Then activate it:
<pre>
<code><b>source venv/bin/activate</b></code>
</pre>
Install all packages from requirements.txt file:
<pre>
<code><b>pip install -r requirements.txt</b></code>
</pre>
Run tests with PyTest:
<pre>
<code><b>pytest</b></code>
</pre>
<hr style="margin-top: 0"/>
