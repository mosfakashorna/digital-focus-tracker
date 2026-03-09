import time
start_time = None
session_count = 0
total_focus_time = 0
focuses = []
sessions = []

print("""
========================================
     DIGITAL FOCUS TRAKER
========================================
1. Start focus session.
2. End focus session.
3. History of session and focus time.
4. total session and focus time.
5. Exit
________________________________________
""")

while True:
    choice = input("\nChoose an option: ")

    if choice == "1":
        start_time = int(time.time())
        print("Session started.")

    elif choice == "2":
        if start_time is None:
            print("No session has started yet.")
        else:
            end_time = int(time.time())
            session_time = round(end_time - start_time)

            total_focus_time += session_time
            session_count += 1

            print("Session ended.")
            print(f"In this session you focused: {session_time} seconds.")

            start_time = None

            focuses.append(session_time)
            sessions.append(session_count)

    elif choice == "3":
        for x in range(len(focuses)):
            print(
                f"In session {sessions[x]} you focused {focuses[x]} seconds.")

    elif choice == "4":
        print(f"Total session: {session_count}")
        print(f"Total focus: {total_focus_time}")

    elif choice == "5":
        print("Goodbye. Stay focused!")
        break

    else:
        print("To choose option enter any number between (1 - 5).")
