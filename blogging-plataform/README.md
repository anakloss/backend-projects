# Blogging Plataform API
Bloging Plataform API is a simple RESTfull API that allows you to perform basic CRUD operations for a personal blogging plataform. CRUD stands for Create, Read, Update, and Delete.
Sample solution for the [blogging-plataform](https://roadmap.sh/projects/blogging-platform-api) challenge from [roadmap.sh](https://roadmap.sh/).


## 🚀 How to run
Clone the repository and run the following command:
```
git clone https://github.com/anakloss/backend-projects.git
cd backend-projects/blogging-plataform
```

Install dependecies
```
pip install -r requirements.txt
```

## 📘 API
Run the project:
```
py app.py
```

POST /posts
Create a new blog post.

* **URL**: /posts
* **Method**: POST
* **Body** Parameters:
    * title (String): Title of the post.
    * content (String): Content of the post.
    * category (String): Category of the post.
    * tags (Array of Strings): Tags for the post.

Responses:
**201 Created**: The created blog post object.
```
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```
**400 Bad Request**: Validation error messages.

PUT /posts/id
Update an existing blog post.

* **URL**: /posts/:id
* **Method**: PUT
* **URL** Parameters:
    * id (Int): ID of the post to update.
* **Body Parameters**:
    * title (String): Updated title.
    * content (String): Updated content.
    * category (String): Updated category.
    * tags (Array of Strings): Updated tags.

Responses:

**200 OK**: The updated blog post object.
```
{
  "id": 1,
  "title": "My Updated Blog Post",
  "content": "This is the updated content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:30:00Z"
}
```
**400 Bad Request**: Validation error messages.
**404 Not Found**: Blog post not found.

DELETE /posts/:id
Delete an existing blog post.

* **URL**: /posts/:id
* **Method**: DELETE
* **URL Parameters**:
    *id (String): ID of the post to delete.

Responses:

**204 No Content**: Blog deleted successfully.
**404 Not Found**: Blog post not found.

GET /posts/:id
Get a single blog post.

* **URL**: /posts/:id
* **Method**: GET
* **URL Parameters**:
    * id (String): ID of the post to retrieve.

Responses:

**200 OK**: The blog post object.
```
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```
**404 Not Found**: Blog post not found.

GET /posts or GET /posts?term=tech
Get all blog posts or filter by a search term.

* **URL**: /posts
* **Method**: GET
* **Query Parameters**:
    * term (String, optional): Search term for filtering.

Responses:

**200 OK**: An array of blog posts.
```
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:00:00Z"
  },
  {
    "id": 2,
    "title": "My Second Blog Post",
    "content": "This is the content of my second blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "createdAt": "2021-09-01T12:30:00Z",
    "updatedAt": "2021-09-01T12:30:00Z"
  }
]
```

## Notes
* Ensure that the .env file exists in the same directory as the script for it to function correctly.