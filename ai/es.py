import time
from random import choice

# Knowledge base
knowledge_base = {
    "fall_detected": {
        "question": "Are you ok?",
        "responses": {
            "yes": "False alarm, take care please.",
            "no": "Attempting to call a family member...",
            "": "Attempting to call a family member...",
        },
        "next_step": "call_family",
    },
    "call_family": {
        "question": None,
        "responses": {
            "yes": "Family member will check on the patient.",
            "no": "Calling 911!!",
            "": "Calling 911!!",
        },
        "next_step": "call_911",
    },
    "call_911": {
        "question": None,
        "responses": {
            "yes": "911 has been called.",
            "no": "911 has been called.",
            "": "911 has been called.",
        },
        "next_step": None,
    },
}


# Simulate getting data from a camera and mic
def get_sensor_data():
    return choice(["fall", "no_fall"])


# Simulate getting a response from the patient
def get_patient_response():
    return choice(["yes", "no", ""])


# Inference engine
def inference_engine(sensor_data):
    if sensor_data == "fall":
        current_step = "fall_detected"
        while current_step:
            step_info = knowledge_base[current_step]
            if step_info["question"]:
                print(step_info["question"])
                response = get_patient_response()
                print(response)
            else:
                response = get_patient_response()
                print(response)

            print(step_info["responses"][response])
            if response == "no" or response == "":
                if current_step == "call_family":
                    time.sleep(2)  # Simulate time delay for calling
                elif current_step == "call_911":
                    time.sleep(2)  # Simulate time delay for calling 911
            else:
                return
            current_step = step_info["next_step"]
    else:
        print("No fall detected. All is well.")


# Main logic
def main():
    sensor_data = get_sensor_data()
    inference_engine(sensor_data)


if __name__ == "__main__":
    main()
