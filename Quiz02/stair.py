class Activity:
    def __init__(self, id, arrival_time, deadline):
        self.id = id
        self.arrival_time = arrival_time
        self.deadline = deadline

def greedy_schedule(activities):
    # Sort activities by their deadlines (earliest first)
    activities.sort(key=lambda x: x.deadline)
    
    # Initialize the current time
    current_time = 0
    scheduled_activities = []

    # Iterate through each activity
    for activity in activities:
        # Check if the activity can be completed before its deadline
        if activity.arrival_time >= current_time and activity.arrival_time <= activity.deadline:
            scheduled_activities.append(activity)
            current_time = activity.arrival_time  # Update the current time after scheduling
            print(f"Scheduled: {activity.id} at time {current_time}")
        else:
            print(f"Skipped: {activity.id} (Cannot be completed before deadline)")
    
    return scheduled_activities

# Define activities
activities = [
    Activity("A", 0, 20),
    Activity("B", 0, 10),
    Activity("C", 10, 20),
    Activity("D", 20, 60),
    Activity("E", 40, 50),
    Activity("F", 60, 100),
    Activity("G", 80, 90),
    Activity("H", 90, 100)
]

# Run the greedy scheduling algorithm
scheduled = greedy_schedule(activities)

# Output the scheduled activities
print("\nScheduled Activities:")
for activity in scheduled:
    print(f"Activity {activity.id} - Arrival: {activity.arrival_time}, Deadline: {activity.deadline}")
