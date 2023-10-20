from flask import Flask, request, jsonify

app = Flask(__name__)

students = {
    1: {"name": "Nidhi", "grade": "90"},
    2: {"name": "Hetvi", "grade": "92"},
}


# Generate a unique user ID
def generate_students_id():
    return max(students.keys()) + 1


# Create a new user
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    student_id = generate_students_id()
    new_student = {"name": data["name"], "grade": data["grade"]}
    students[student_id] = new_student
    return jsonify(new_student), 201





# Get a specific user by ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)
    if student is not None:
        return jsonify(student)
    return "student not found", 404


# Update a user by ID
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    student = students.get(student_id)
    if student is not None:
        student["name"] = data["name"]
        return jsonify(student)
    return "student not found", 404


# Delete a user by ID
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = students.pop(student_id, None)
    if student is not None:
        return "student deleted", 204
    return "stuent not found", 404


if __name__ == "__main__":
    app.run(port=5000, debug=True)