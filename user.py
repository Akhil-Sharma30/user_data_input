class User:

    # init is executed automatically when the object of that class is created
    # self refer to the current instance of the class
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")


app_user_one = User("nn@gmail.com", "akhil", "asd", "webdev")
app_user_one.get_user_info()
