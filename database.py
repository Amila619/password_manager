import pyrebase

from customMessageBox import CustomMessageBox


class Database:
    def __init__(self):
        # Initialize Pyrebase
        firebaseConfig = {
            "apiKey": "AIzaSyAMNI_HmsZFk-3PZwhqFpbF1MeAzos5JqY",
            "authDomain": "practisefirebase-2511d.firebaseapp.com",
            "databaseURL": "https://practisefirebase-2511d-default-rtdb.firebaseio.com",
            "projectId": "practisefirebase-2511d",
            "storageBucket": "practisefirebase-2511d.appspot.com",
            "messagingSenderId": "1089512548282",
            "appId": "1:1089512548282:web:a146c6a93e6435fd9fdf83",
            "measurementId": "G-79WT4S4FFG"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)

        self.auth = firebase.auth()
        self.database = firebase.database()

    def add_user_and_make_db_entry(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            self.database.child("users").child(uid).set({
                "password_db": ''
            })
        except:
            pass

    def sign_in_and_verify(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except:
            msg_box = CustomMessageBox(msg="Error", pop_up_text="Invalid username or password")
            msg_box.call_window()

    def add_new_entry(self, entry, username, password, user_id):
        try:
            self.database.child("users").child(user_id).child("password_db").push({
                    "Entry": entry,
                    "Username": username,
                    "pass_word": password
            })
        except:
            msg_box = CustomMessageBox(msg="Error", pop_up_text="Sorry something went wrong")
            msg_box.call_window()

    def update_data_entry(self, id_, entry_, uname, pw, user_id):
        self.database.child("users").child(user_id).child("password_db").child(id_).update({
                "Entry": entry_,
                "Username": uname,
                "pass_word": pw
            })

    def delete_all_entry(self, user_id):
        try:
            self.database.child("users").child(user_id).update({"password_db": ""})
        except:
            pass

    def delete_selected_entry(self, id_, user_id):
        try:
            self.database.child("users").child(user_id).child("password_db").child(id_).remove()
        except:
            pass

    def return_user_db_data(self, user_id):
        try:
            result = self.database.child("users").child(user_id).child("password_db").get()
            return result
        except:
            pass

# d = Database()
#
# v = d.return_user_db_data("OJZRS5rrCvSdBYLbSt9xs6KAJ6x2")
# for instance in v.each():
#         item = instance.val()
#         if item == None:
#             continue
#         print(item)

# d.delete_all_entry()
# d.delete_selected_entry()
