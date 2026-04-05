# https://docs.python.org/3/library/sqlite3.html

import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    print("\nList of Videos:")
    for video in videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()




def main():
    while True:
        print("\n YouTube Video Manager app with DB")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            # Add video to DB
            # cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
            # conn.commit()   
            add_video(name, time)

        elif choice == '3':
            video_id = int(input("Enter video ID to update: "))
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            # Update video in DB
            # cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
            # conn.commit() 
            update_video(video_id, name, time)    


        elif choice == '4':
            video_id = int(input("Enter video ID to delete: "))
            # Delete video from DB
            # cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
            # conn.commit()
            delete_video(video_id)

        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")  
    conn.close()          

if __name__ == "__main__":
    main()
