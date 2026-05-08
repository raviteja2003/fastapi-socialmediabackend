from fastapi import FastAPI,HTTPException

app = FastAPI()

text_posts = {
    1: {
        "title": "New Post",
        "content": "This is my first post"
    },
    2: {
        "title": "Morning Thoughts",
        "content": "Starting the day with positive energy and focus."
    },
    3: {
        "title": "Learning FastAPI",
        "content": "FastAPI makes backend development fast and simple."
    },
    4: {
        "title": "Workout Update",
        "content": "Completed a 5km run and strength training session today."
    },
    5: {
        "title": "Tech News",
        "content": "AI tools are transforming software development rapidly."
    },
    6: {
        "title": "Weekend Plans",
        "content": "Planning to work on personal projects and relax."
    },
    7: {
        "title": "Coding Journey",
        "content": "Consistency in coding helps improve problem-solving skills."
    },
    8: {
        "title": "Travel Diary",
        "content": "Visited a beautiful beach and enjoyed the sunset."
    },
    9: {
        "title": "Book Recommendation",
        "content": "Atomic Habits is a great book for building discipline."
    },
    10: {
        "title": "Project Progress",
        "content": "Completed authentication module for the social media app."
    }
}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit :
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    return text_posts[id]
    


