from os import system, name
import numpy as np

# Print menu screen and get user input.
def menu():
    clear()
    print(
        "Multi-Stage Kinematics Intercept Calculator \n"
        "Select an option: \n"
        "1. Start the calculator \n"
        "2. Display the instructions \n"
        "3. View information \n"
        "4. Exit the calculator \n"
        )
    choice = input("Enter your choice: ")
    
    # If user selects 1, start the calculator.
    if choice == "1":
        clear()
        calculator()

    # If user selects 2, display the instructions.
    elif choice == "2":
        clear()
        print(
            "Instructions: \n"
            "Enter the values for the variables you know, for each specific phase. \n"
            "Enter 'u', 'unknown', or leave the space blank for variables that you do not know. \n"
            "You must know at least three variables to use the calculator. \n"
            "Units will be reported as SI, but you can input different units, just ignore the reported unit. \n"
            "Do not input time as 0, because that means that there is no motion during that phase. \n"
            )
        input("Press enter to return to the menu. \n")
        menu()

    # If user selects 3, view information.
    elif choice == "3":
        clear()
        print(
            "This is a calculator to find unknown variables using kinematics equations. \n"
            "The equations used are: \n"
            "Vf = V0 + at, or the final velocity is equal to the initial velocity plus acceleration multiplied by time. \n"
            "Vf^2 = V0^2 + 2aΔx, or the final velocity squared is equal to the initial velocity squared plus 2 multiplied by acceleration multiplied by the change in position. \n"
            "Δx = (Vf + V0)/2t, or the change in velocity is equal to both the final velocity plus the initial velocity divided by 2 multiplied by time. \n"
            "Δx = V0t + 1/2(at^2), or the change in position is equal to the initial velocity multiplied by time plus one half of acceleration multiplied by time squared. \n"
            "This calculator can solve for all of the unknowns in the equations, as long as there are at least three known variables. \n"
            "This calculator is capable of calculating up to 10 units of precision. \n"
            )
        input("Press enter to return to the menu. \n")
        menu()

    # If user selects 4, exit the calculator after confirmation.
    elif choice == "4":
        while True:
            exit_question = input("\nAre you sure you want to exit? \n\n")
            if exit_question.lower() in ["yes", "y"]:
                clear()
                exit()
            elif exit_question.lower() in ["no", "n"]:
                menu()
            else:
                continue

    # If user selects an invalid option, return to the menu.
    else:
        clear()
        print("Invalid option. \n")
        input("Press enter to return to the menu. \n")
        menu()

# Start the calculator.
def calculator():
    while True:
        intercept = input("Are you calculating an intercept of objects? \n\n")
        clear()
        if intercept.lower() in ["y", "yes"]:
            object_number = input("How many objects are you calculating? \n\n")
            print()
        elif intercept.lower() in ["n", "no"]:
            object_number = 1
        object_list = list(range(1, int(object_number) + 1))
        clear()
        for object_iteration, i, in enumerate(object_list, start=1):
            object_iter = "object " + str(object_iteration)
            phase_number = input("How many phases of motion does " + object_iter + " have? \n\n")
            phase_list = list(range(1, int(phase_number)+1))
            clear()
            for iteration, i in enumerate(phase_list, start=1):
                iter = "of the motion in Phase " + str(iteration) + ": "
                initial_velocity = (input("Initial velocity " + iter))
                final_velocity = (input("Final velocity " + iter))
                acceleration = (input("Acceleration " + iter))
                time = (input("Elapsed time " + iter))
                change_in_position = (input("Change in position " + iter))
                print("\n")
                # If the user knows the final velocity, acceleration, and time, calculate the initial velocity.
                if final_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and time not in ["","u", "unknown"]:
                    initial_velocity = float(final_velocity) - float(acceleration) * float(time)
                # If the user knows the final velocity, acceleration, and change in position, calculate the initial velocity.
                elif final_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    initial_velocity = np.sqrt(float(final_velocity)**2 - 2 * float(acceleration) * float(change_in_position))
                # If the user knows the final velocity, time, and change in position, calculate the initial velocity.
                elif final_velocity not in ["","u", "unknown"] and time not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: initial_velocity = (2 * float(change_in_position) - float(final_velocity) * float(time)) / float(time)
                    except ZeroDivisionError:
                        initial_velocity = 0
                # If the user knows the acceleration, time, and change in position, calculate the initial velocity.
                elif acceleration not in ["","u", "unknown"] and time not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: initial_velocity = (2 * float(change_in_position) - float(acceleration) * float(time)**2) / float(time)
                    except ZeroDivisionError:
                        initial_velocity = 0
                # If the user knows the initial velocity, acceleration, and time, calculate the final velocity.
                if initial_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and time not in ["","u", "unknown"]:
                    final_velocity = float(initial_velocity) + float(acceleration) * float(time)
                # If the user knows the initial velocity, acceleration, and change in position, calculate the final velocity.
                elif initial_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    final_velocity = np.sqrt(float(initial_velocity)**2 + 2 * float(acceleration) * float(change_in_position))
                # If the user knows the initial velocity, time, and change in position, calculate the final velocity.
                elif initial_velocity not in ["","u", "unknown"] and time not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: final_velocity = (2 * float(change_in_position) - float(initial_velocity) * float(time)) / float(time)
                    except ZeroDivisionError:
                        final_velocity = 0
                # If the user knows the acceleration, time, and change in position, calculate the final velocity.
                elif acceleration not in ["","u", "unknown"] and time not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: final_velocity = (2 * float(change_in_position) - float(acceleration) * float(time)**2) / float(time)
                    except ZeroDivisionError:
                        final_velocity = 0
                # If the user knows the initial velocity, final velocity, and time, calculate the acceleration.
                if initial_velocity not in ["","u", "unknown"] and final_velocity not in  ["","u", "unknown"] and time not in ["","u", "unknown"]:
                    try: acceleration = (float(final_velocity) - float(initial_velocity)) / float(time)
                    except ZeroDivisionError:
                        acceleration = 0
                # If the user knows the initial velocity, final velocity, and change in position, calculate the acceleration.
                elif initial_velocity not in ["","u", "unknown"] and final_velocity not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: acceleration = (float(final_velocity)**2 - float(initial_velocity)**2) / (2 * float(change_in_position))
                    except ZeroDivisionError:
                        acceleration = 0
                # If the user knows the initial velocity, time, and change in position, calculate the acceleration.
                elif initial_velocity not in ["","u", "unknown"] and time not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: acceleration = (2 * float(change_in_position) - float(initial_velocity) * float(time)) / float(time)**2
                    except ZeroDivisionError:
                        acceleration = 0
                # If the user knows the final velocity, time, and change in position, calculate the acceleration.
                elif final_velocity not in ["","u", "unknown"] and time not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: acceleration = (2 * float(change_in_position) - float(final_velocity) * float(time)) / float(time)**2
                    except ZeroDivisionError:
                        acceleration = 0
                # If the user knows the initial velocity, final velocity, and acceleration, calculate the time.
                if initial_velocity not in ["","u", "unknown"] and final_velocity not in  ["","u", "unknown"] and acceleration not in ["","u", "unknown"]:
                    try: time = (float(final_velocity) - float(initial_velocity)) / float(acceleration)
                    except ZeroDivisionError:
                        pass
                # If the user knows the initial velocity, final velocity, and change in position, calculate the time.
                elif initial_velocity not in ["","u", "unknown"] and final_velocity not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: time = (float(final_velocity) - float(initial_velocity)) / float(acceleration)
                    except ZeroDivisionError:
                        pass
                # If the user knows the initial velocity, acceleration, and change in position, calculate the time.
                elif initial_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: time = (2 * float(change_in_position) - float(initial_velocity) * float(time)) / float(time)**2
                    except ZeroDivisionError:
                        pass 
                # If the user knows the final velocity, acceleration, and change in position, calculate the time.
                elif final_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and change_in_position not in ["","u", "unknown"]:
                    try: time = (2 * float(change_in_position) - float(final_velocity) * float(time)) / float(time)**2
                    except ZeroDivisionError:
                        time = 0
                # If the user knows the initial velocity, final velocity, and time, calculate the change in position.
                if initial_velocity not in ["","u", "unknown"] and final_velocity not in  ["","u", "unknown"] and time not in ["","u", "unknown"]:
                    try: change_in_position = (float(initial_velocity) + float(final_velocity)) / 2 * float(time)
                    except ZeroDivisionError:
                        change_in_position = 0
                # If the user knows the initial velocity, acceleration, and time, calculate the change in position.
                elif initial_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and time not in ["","u", "unknown"]:
                    try: change_in_position = float(initial_velocity) * float(time) + 1/2 * float(acceleration) * float(time)**2
                    except ZeroDivisionError:
                        change_in_position = 0
                # If the user knows the initial velocity, final velocity, and acceleration, calculate the change in position.
                elif initial_velocity not in ["","u", "unknown"] and final_velocity not in  ["","u", "unknown"] and acceleration not in ["","u", "unknown"]:
                    try: change_in_position = (float(final_velocity)**2 - float(initial_velocity)**2) / (2 * float(acceleration))
                    except ZeroDivisionError:
                        change_in_position = 0
                # If the user knows the final velocity, acceleration, and time, calculate the change in position.
                elif final_velocity not in ["","u", "unknown"] and acceleration not in  ["","u", "unknown"] and time not in ["","u", "unknown"]:
                    try: change_in_position = float(final_velocity) * float(time) - 1/2 * float(acceleration) * float(time)**2
                    except ZeroDivisionError:
                        change_in_position = 0
                
                # If the user does not input at least three variables, restart the calculator.
                else:
                    clear()
                    input("You must know at least three variables to use the calculator. Press enter to go back to the main menu. \n")
                    menu()
                
                # Print the results.
                print(
                    f"\033[FPhase {iteration} Metrics: \n"
                    f"Initial Velocity: {round(float(initial_velocity), 10)} m/s. \n"
                    f"Final Velocity: {round(float(final_velocity), 10)} m/s. \n"
                    f"Acceleration: {round(float(acceleration), 10)} m/s^2. \n"
                    f"Elapsed Time: {round(float(time), 10)} s. \n"
                    f"Change in Position: {round(float(change_in_position), 10)} m. \n"
                    )
                
                # Save the last phase's results.
                global last_phase_initial_velocity
                last_phase_initial_velocity = initial_velocity
                global last_phase_final_velocity
                last_phase_final_velocity = final_velocity
                global last_phase_acceleration
                last_phase_acceleration = acceleration
                global last_phase_time
                last_phase_time = time
                global last_phase_change_in_position
                last_phase_change_in_position = change_in_position
                global average_velocity
                global average_acceleration
                global total_time
                global total_distance

                # Set total value variables.
                if iteration == 1:
                    average_velocity = (float(initial_velocity) + float(final_velocity)) / 2
                    average_acceleration = float(acceleration)
                    total_time = float(time)
                    total_distance = float(change_in_position)
                    if object_iteration == 1:
                        with open('results.txt', 'w') as f:
                            f.write("Kinematic Equation Calculator Results \n\n")
                    with open('results.txt', 'a') as f:
                        f.write(
                        f"Object {object_iteration} Results: \n\n"
                        f"Phase {i} Metrics: \n\n"
                        f"Initial Velocity: {round(float(initial_velocity), 10)} m/s. \n"
                        f"Final Velocity: {round(float(final_velocity), 10)} m/s. \n"
                        f"Acceleration: {round(float(acceleration), 10)} m/s^2. \n"
                        f"Elapsed Time: {round(float(time), 10)} s. \n"
                        f"Change in Position: {round(float(change_in_position), 10)} m. \n"
                        )
                else:
                    total_time = total_time + float(time)
                    total_distance = total_distance + float(change_in_position)
                    average_velocity = total_distance / total_time
                    average_acceleration = total_distance / total_time**2
                    with open('results.txt', 'a') as f:
                        f.write(
                        f"\nPhase {i} Metrics: \n\n"
                        f"Initial Velocity: {round(float(initial_velocity), 10)} m/s. \n"
                        f"Final Velocity: {round(float(final_velocity), 10)} m/s. \n"
                        f"Acceleration: {round(float(acceleration), 10)} m/s^2. \n"
                        f"Elapsed Time: {round(float(time), 10)} s. \n"
                        f"Change in Position: {round(float(change_in_position), 10)} m. \n"
                        )

                # Print the total results.
                if iteration == int(phase_number):
                    print(
                        f"Total Metrics of Object {object_iteration}: \n"
                        f"Average Velocity: {round(float(average_velocity), 10)} m/s. \n"
                        f"Average Acceleration: {round(float(average_acceleration), 10)} m/s^2. \n"
                        f"Total Time: {round(float(total_time), 10)} s. \n"
                        f"Total Distance: {round(float(total_distance), 10)} m. \n"
                        )
                        
                    if object_iteration == int(object_number):
                        input("Press enter to return to the main menu. \n")
                    else:
                        continue
                else:
                    input("\nPress enter to continue calculations. \n")
                    continue
            
            # Save the total results to a file.
            with open('results.txt', 'a') as f:
                f.write(
                "\nTotal Metrics: \n\n"
                f"Average Velocity: {round(float(average_velocity), 10)} m/s. \n"
                f"Average Acceleration: {round(float(average_acceleration), 10)} m/s^2. \n"
                f"Total Time: {round(float(total_time), 10)} s. \n"
                f"Total Distance: {round(float(total_distance), 10)} m. \n\n"
                )

            # If the user has calculated all objects, return to the main menu or calculate intercepts.
            if object_iteration == int(object_number):
                if object_iteration == 1:
                    menu()
                else:
                    # Set all kinematic equations equal to each other and solve for the intercept.
                    if object_iteration == 2:
                        if last_phase_final_velocity == 0:
                            intercept = last_phase_change_in_position
                        else:
                            intercept = last_phase_change_in_position - last_phase_final_velocity**2 / 2 / last_phase_acceleration

            else:
                continue

# Clear the screen.
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    # Print the calculator menu.
    menu()

if __name__ == '__main__':
    main()