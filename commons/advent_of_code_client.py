import requests
import os


class AdventOfCodeClient:
    def __init__(self, year: int):
        self.year = year
        self.session_token = os.getenv("AOC_SESSION_TOKEN")
        self.base_url = f"https://adventofcode.com/{self.year}/day/"

        self.headers = {
            "Cookie": f"session={self.session_token}",
            "User-Agent": "Python AOC Client"
        }

        if not self.session_token:
            raise ValueError("AOC session token is required. Set AOC_SESSION_TOKEN environment variable.")
    
    def _make_request(self, method: str, resource_path: str, **kwargs) -> requests.Response:
        """
        Makes an HTTP request with error handling.

        Args:
            method: HTTP method (GET, POST, PATCH, etc.)
            resource_path: Resource path of the request
            **kwargs: Additional arguments for requests

        Returns:
            Response object

        Raises:
            requests.HTTPError: In case of an HTTP error
        """
        response = requests.request(method, self.base_url + resource_path, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response
    
    def get_input(self, day: int) -> str:
        """
        Get the input data for a specific day.

        Args:
            day: Day number (1-25)

        Returns:
            Input data as string
        """
        response = self._make_request("GET", f"{day}/input")
        return response.text
    
    def submit_answer(self, day: int, level: int, answer: str) -> str:
        """
        Submit an answer for a specific day and level.

        Args:
            day: Day number (1-25)
            level: Level (1 or 2)
            answer: The answer to submit

        Returns:
            Response text from the server
        """
        data = {
            "level": str(level),
            "answer": str(answer)
        }
        
        response = self._make_request("POST", f"{day}/answer", data=data)
        return response.text

if __name__ == "__main__":
    client = AdventOfCodeClient(year=2025)
    day = 1
    # Example of submitting an answer
    # response = client.submit_answer(day, level=2, answer="42")
    # print(f"Submission response:\n{response}")