###########################  Q1  ###############################

# 1) multiple inheritance:

# class addition:
#     def add(self,a,b):
#         print(f"sum = {a+b}")

# class difference:
#     def subtract(self,a,b):
#         print(f"differance = {a-b}")

# class math(addition,difference):
#     def operations (self,a,b):
#         print(f" addition and subtraction: ")

# s = math()

# s.operations(3,4)
# s.add(3,4)
# s.subtract(3,4)


# # 2) multilevel inheritance:

# class animal :
#     def eat(self):
#         print("animal eating")

# class mammal (animal) :
#     def birth(self):
#         print("this mammal does not lie eggs")

# class dog(mammal) :
#     def sound(self):
#         print("woof")

# poppy = dog()
# poppy.eat()
# poppy.birth()
# poppy.sound()



###########################  Q2  ###############################



from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data
USER_DATA = {
    "username": "admin",
    "password": "1234"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USER_DATA["username"] and password == USER_DATA["password"]:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)



###########################  Q3  ###############################


