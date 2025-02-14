import requests
import psutil  
import schedule
import time

# API Details	
API_URL = "https://api.e2enetworks.com/myaccount/api/v1/kubernetes/update-cluster-custom-parameter/15201/"
API_KEY = "b6046693-2131-4c56-84fc-0531bf134a0e"
PROJECT_ID = "34417"
AUTH_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGSjg2R2NGM2pUYk5MT2NvNE52WmtVQ0lVbWZZQ3FvcXRPUWVNZmJoTmxFIn0.eyJleHAiOjE3Njg0ODExOTQsImlhdCI6MTczNjk0NTE5NCwianRpIjoiYWMyN2IwOTMtYmEwMi00NmI3LWI2NjYtNWNlZjRlNGI0YmVlIiwiaXNzIjoiaHR0cDovL2dhdGV3YXkuZTJlbmV0d29ya3MuY29tL2F1dGgvcmVhbG1zL2FwaW1hbiIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI1YTAxNTk3My00MzNlLTRlMjItYjYwZi0yYzJmZWRjMGU0YTMiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJhcGltYW51aSIsInNlc3Npb25fc3RhdGUiOiIwMzNiYzhiZC05ZmU3LTQwNWMtOTQwMi03Yjg2ZWYyYTZjZDMiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImFwaXVzZXIiLCJkZWZhdWx0LXJvbGVzLWFwaW1hbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjAzM2JjOGJkLTlmZTctNDA1Yy05NDAyLTdiODZlZjJhNmNkMyIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6IlkgUyIsInByaW1hcnlfZW1haWwiOiJ5cy5zcmVlcmFqQGUyZW5ldHdvcmtzLmNvbSIsImlzX3ByaW1hcnlfY29udGFjdCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoieXMuc3JlZXJhakBlMmVuZXR3b3Jrcy5jb20iLCJnaXZlbl9uYW1lIjoiWSIsImZhbWlseV9uYW1lIjoiUyIsImVtYWlsIjoieXMuc3JlZXJhakBlMmVuZXR3b3Jrcy5jb20ifQ.Fks9aBY_oDmrsJuhv_TEHhdNl0BL0bPlBICoGEIKhGJU6CiU3mvmEjxmZA-Dj8VsDVaXZy0E5ruRZdVY3DHAca-iSMeYYU89lrLgqaGem6wBsf1FZJ71HgFkvagcJGF5S08XayzYI3jTUqTrbzryjxoAWTlvopOeQbXbpByuFg8"

""" memory utilization """
MEMORY_THRESHOLD_HIGH = 50  
MEMORY_THRESHOLD_LOW = 25 

def get_memory_usage():
    """Returns current memory usage in percentage."""
    return psutil.virtual_memory().percent

def update_custom_parameter(value):
    """Updates the MEMORY_USAGES parameter """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    params = {
        "apikey": API_KEY,
        "project_id": PROJECT_ID
    }

    payload = {
        "name": "MEMORY_USAGES",
        "value": value
    }

    response = requests.put(API_URL, headers=headers, params=params, json=payload)

    if response.status_code == 200:
        print(f"Successfully updated MEMORY_USAGES to {value}%")
    else:
        print(f"Failed to update parameter. Status: {response.status_code}, Response: {response.text}")

def monitor_and_update():
    """Monitors memory usage and updates the parameter accordingly."""
    memory_usage = get_memory_usage()
    print(f"Current Memory Usage: {memory_usage}%")

    if memory_usage > MEMORY_THRESHOLD_HIGH:
        print("High memory usage detected, updating parameter to 90%...")
        update_custom_parameter(memory_usage) 
    
    elif memory_usage < MEMORY_THRESHOLD_LOW:
        print("Low memory usage detected, updating parameter to 50%...")
        update_custom_parameter(memory_usage) 

schedule.every(2).minutes.do(monitor_and_update)  # Check every minute

