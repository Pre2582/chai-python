file = open("youtube.txt", "w")

try:
    file.write("This is a line in the file.")
finally:
    file.close()


with open("youtube.txt", "w") as file:
    file.write("This is a line in the file.")        




# while True:
#     try:
#         video_id = input("Enter a YouTube video ID (or 'exit' to quit): ")
#         if video_id.lower() == 'exit':
#             print("Exiting the YouTube manager.")
#             break
        
#         # Simulate fetching video details (replace with actual API call)
#         if len(video_id) != 11:
#             raise ValueError("Invalid YouTube video ID. It should be 11 characters long.")
        
#         # Simulate successful fetch
#         print(f"Successfully fetched details for video ID: {video_id}")
    
#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
