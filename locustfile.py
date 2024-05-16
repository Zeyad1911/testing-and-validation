from locust import HttpUser, between, task, run_single_user

base_url = 'http://localhost:5000'

class RegisterUser(HttpUser):
  wait_time = between(1,7)
  host = "http://localhost:5000"
  
  @task
  def register(self):
    name = "John Doe"
    email = "johndoe@example.com"
    password = "12345"
    
    response = self.client.post(f"/register", json={"name": name, "email": email, "password": password})
    if response.status_code == 200:
      print(f"Registration successful for {name} {email} {password} ")
    else:
      print(f"Status: {response.status_code}")  
      
      
user = 10
spawn_rate = 1      
if __name__ == "__main__":
  run_single_user(RegisterUser, user,spawn_rate)