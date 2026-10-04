from clients.base_api_client import BaseApiClient


class PostsApi:
    """API client for JSONPlaceholder Posts endpoints."""

    def __init__(self, client: BaseApiClient):
        self.client = client

    def get_posts(self):
        """Get all posts."""
        return self.client.get("/posts")

    def get_post(self, post_id: int):
        """Get a specific post."""
        return self.client.get(f"/posts/{post_id}")

    def create_post(self, payload: dict):
        """Create a new post."""
        return self.client.post("/posts", json=payload)

    def update_post(self, post_id: int, payload: dict):
        """Update an existing post."""
        return self.client.put(f"/posts/{post_id}", json=payload)

    def patch_post(self, post_id: int, payload: dict):
        """Partially update an existing post."""
        return self.client.patch(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id: int):
        """Delete a post."""
        return self.client.delete(f"/posts/{post_id}")