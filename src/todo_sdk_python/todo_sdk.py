"""Todo API Python SDK"""
import requests


class TodoClient:
    """Client for Todo API operations."""

    def __init__(self, base_url="http://localhost:8000"):
        """
        Initialize Todo client.

        Args:
            base_url: API base URL
        """
        self.base_url = base_url

    def get_todo(self, todo_id: int) -> dict:
        """
        Get a todo by ID.

        Args:
            todo_id: The todo's ID

        Returns:
            Todo dictionary with id and title

        Example:
            >>> client = TodoClient()
            >>> client.get_todo(1)
            {'id': 1, 'title': 'Sample'}
        """
        return requests.get(f"{self.base_url}/todos/{todo_id}").json()

    def create_todo(self, todo_id: int, title: str) -> dict:
        """
        Create a new todo.

        Args:
            todo_id: Todo ID
            title: Todo title

        Returns:
            Created todo object

        Example:
            >>> client = TodoClient()
            >>> client.create_todo(1, "Buy milk")
            {'id': 1, 'title': 'Buy milk'}
        """
        return requests.post(
            f"{self.base_url}/todos",
            json={"id": todo_id, "title": title}
        ).json()
