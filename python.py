# import pandas as pd
# import re

# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Email': ['alice@email.com', 'bob@work.com', 'charlie@home.com'],
#         'Feature':[10, 20, 30]}
# df= pd.DataFrame (data)

# def mask_email(email):
#     return re.sub(r'(?<=.{2}).(?=.*@)', '*', email)
# df ['Email'] = df ['Email'].apply(mask_email)
# print (df)

# import numpy as np
# salaries = np.array([50000, 60000, 1000000, 55000])  # 1M is an outlier

# def add_laplace_noise(data, sensitivity, epsilon):
#     beta = sensitivity / epsilon
#     noise = np.random.laplace(0, beta, len(data))
#     return data + noise

# sensitive_avg = np.mean(salaries)
# private_avg = np.mean(add_laplace_noise(salaries, sensitivity=1000000, epsilon=1))

# print(f"True Average: {sensitive_avg}")
# print(f"Private Average: {private_avg}")

# from art.estimators.classification import KerasClassifier
# from art.attacks.evasion import FastGradientMethod
# import numpy as np

# classifier = KerasClassifier(model=model, clip_values=(min_pixel_value, max_pixel_value))  # clip values depend on your data
# attack = FastGradientMethod(estimator=classifier, eps=0.2)
# x_test_adv = attack.generate(x=x_test)
# predictions = classifier.predict(x_test_adv)
# accuracy = np.sum(np.argmax(predictions, axis=1) == np.argmax(y_test, axis=1)) / len(y_test)
# print(f"Accuracy on adversarial samples: {accuracy*100}%")

# import datetime
# user_consent = True
# consent_purpose = "Marketing"
# data_collection_purpose = "Marketing"

# def process_user_data(user_id, data, purpose, consent):
#     if not consent or purpose != data_collection_purpose:
#         print("Error: Purpose mismatch or no consent.")
#         return None
#     print(f"Processing data for {purpose}...")
#     return {"user_id": user_id, "data": data, "timestamp": datetime.datetime.now()}
# user_data = {"name": "Alice", "email": "alice@example.com"}
# processed = process_user_data("123", user_data, "Marketing", user_consent)

# raw_data = {
#     "username": "user1",
#     "password_hash": "...",
#     "email": "user@example.com",
#     "location": "GPS_COORDINATES",
#     "age": 25
# }
# def minimize_data(data):
#     minimized = {k: v for k, v in data.items() if k in ["username", "email", "age"]}
#     return minimized

# minimized_data = minimize_data(raw_data)
# print(minimized_data)

# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# sensitive_data = b"User Sensitive Data"

# encrypted_data = cipher_suite.encrypt(sensitive_data)
# print(f"Encrypted: {encrypted_data}")

# decrypted_data = cipher_suite.decrypt(encrypted_data)
# print(f"Decrypted: {decrypted_data.decode('utf-8')}")

# database = {
#     "user1": {"name": "Alice", "data": "..."},
#     "user2": {"name": "Bob", "data": "..."}
# }
# def delete_user_data(user_id):
#     if user_id in database:
#         del database[user_id]
#         print(f"User {user_id} data deleted.")
#     else:
#         print("User not found.")
# delete_user_data("user1"import pandas as pd

# import pandas as pd
# import numpy as np

# # Create a hypothetical raw dataset
# data = {
#     'UserID': [1, 2, 3, 4, 5],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 32, 18, 47, 30],
#     'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eve@example.com'],
#     'PurchaseHistory': [150.00, 45.50, 0.00, 1200.00, 210.25],
#     'Location': ['NY', 'CA', 'TX', 'NY', 'CA'],
#     'IPAddress': ['192.168.1.1', '10.0.0.2', '172.16.0.3', '192.168.1.4', '10.0.0.5']
# }
# df_raw = pd.DataFrame(data)

# # Minimize data: Only keep necessary fields using dict comprehension
# def minimize_data(data_input):
#     # Fixed keys to match the dictionary case and names
#     minimized = {k: v for k, v in data_input.items() if k in ["Name", "Email", "Age"]}
#     return minimized

# # Running the function on your raw dictionary
# minimized_dict = minimize_data(data)
# print("Minimized Dictionary:", minimized_dict)

# # Alternatively, minimizing the Pandas DataFrame directly:
# df_minimized = df_raw[["Name", "Email", "Age"]]
# print("\nMinimized DataFrame:\n", df_minimized)

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# from fairlearn.metrics import MetricFrame, demographic_parity_difference
# from fairlearn.datasets import make_adult_df

# df = make_adult_df()
# X = df.drop("income", axis=1)
# y = df["income"]
# sensitive_features = df[['age']]
# sensitive_features['age_group'] = sensitive_features['age'].apply(lambda x: 'old' if x >= 40 else 'young')

