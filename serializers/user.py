from models.user import User

def serialize_user(user: User) -> dict:
  return {
      "id": user.id,
      "first_name": user.first_name,
      "last_name": user.last_name,
      "email": user.email,
      "dob": user.dob,
      "gender": user.gender,
      "is_active": user.is_active,
      "full_name": f"{user.first_name} {user.last_name}",
      "status": "active" if user.is_active else "inactive"
  }

def serialize_user_with_blogs(user: User) -> dict:
  return {
    "id": user.id,
    "first_name": user.first_name,
    "last_name": user.last_name,
    "email": user.email,
    "dob": user.dob,
    "gender": user.gender,
    "is_active": user.is_active,
    "full_name": f"{user.first_name} {user.last_name}",
    "status": "active" if user.is_active else "inactive",
    "blogs": [
          {
              "id": blog.id,
              "title": blog.title,
              "content": blog.content,
              "published": blog.published,
              "user_id": blog.user_id
          }
          for blog in user.blogs
      ]
  }
  