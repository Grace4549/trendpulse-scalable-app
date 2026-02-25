#TrendPulse – Scalable Cloud Deployed Web Application
##Live Deployment

The application is currently deployed on AWS EC2 and accessible at:

http://100.48.79.103

HTTPS / SSL is not configured yet.

##Project Overview
I built TrendPulse as a scalable cloud-based web application to demonstrate real-world DevOps and infrastructure deployment practices.
The project is hosted on an AWS EC2 instance and runs in a production environment using:
-Gunicorn as the WSGI server
-Nginx as a reverse proxy
-Systemd for process management
This project reflects hands-on experience with cloud infrastructure, server configuration, and production deployment.

##Current Architecture
User
  ↓
HTTP (Port 80)
  ↓
Nginx Reverse Proxy
  ↓
Gunicorn (Systemd Service)
  ↓
Flask Application

I deployed the application on:
-AWS EC2 (Ubuntu Server)
-Production-grade service configuration
-Background process management with systemd

##Technologies I Used
-Python
-Flask
-Gunicorn
-Nginx
-Ubuntu Linux
-AWS EC2
-Git & GitHub

##Deployment Steps I Followed
1. Cloned the Repository
git clone https://github.com/Grace4549/trendpulse-scalable-app.git

2. Created a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Installed Dependencies
pip install -r requirements.txt

4. Ran the Application with Gunicorn
gunicorn -w 4 -b 127.0.0.1:8000 app.app:app

5. Configured Systemd Service
I configured a systemd service to run Gunicorn as a background process to ensure:
-Auto restart on failure
-Auto start on boot
-Stable production execution
-Service file located at:
/etc/systemd/system/trendpulse.service

6. Configured Nginx Reverse Proxy
I configured Nginx to forward traffic from: Port 80 → Gunicorn (8000). This enables public access via the EC2 public IP.

##Pending Improvements (To Be Added)

SSL Certificate with Let’s Encrypt (HTTPS) (To be added)

Custom Domain Integration (To be added)

Auto Scaling Group Setup (To be added)

Load Balancer Implementation (To be added)

Database Integration with AWS RDS (To be added)

Redis Caching Layer (To be added)

CI/CD Pipeline with GitHub Actions (To be added)

Monitoring & Logging System (To be added)

Docker Containerization (To be added)

#Security Improvements (To Be Added)

Domain-based SSL certificate

Firewall hardening

Restrict SSH access to specific IP

Secure environment variables


I built this project to demonstrate hands-on experience with:

Cloud Infrastructure

Production Server Deployment

DevOps Engineering Practices

Scalable Web Application Architecture
