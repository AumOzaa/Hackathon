import FigmaPy  # Assuming figmapy is installed and imported correctly 
from FigmaPy import FigmaPy  # Note: Capital 'F' and 'P' 

class FigmaService:
    def __init__(self, access_token):
        # self.figma = FigmaPy(access_token)
        self.client = FigmaPy(access_token)

    # def get_file(self, file_key):
    #     return self.figma.get_file(file_key)  # Returns the full Figma file JSON

    def get_file(self, file_key):
        """Get Figma file data"""
        try:
            return self.client.get_file(file_key)
        except Exception as e:
            print(f"Figma API Error: {str(e)}")
            raise

    def get_styles(self, file_key):
        # Note: figmapy doesn't directly support styles endpoint, so we use raw requests
        import requests
        url = f"https://api.figma.com/v1/files/{file_key}/styles"
        headers = {"X-Figma-Token": self.figma.access_token}
        response = requests.get(url, headers=headers)
        return response.json()