import os
import requests
from urllib.parse import urlparse

def main():
    # Print welcome message
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ").strip()
    
    try:
        # Create directory for community sharing
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Respectful connection to web community
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Honor HTTP status codes
        
        # Verify content is an image
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            raise ValueError("URL does not point to an image resource")
        
        # Extract filename from URL or generate default
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = "community_image.jpg"
        
        # Prevent file overwrites
        filepath = os.path.join("Fetched_Images", filename)
        counter = 1
        name, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filename = f"{name}_{counter}{ext}"
            filepath = os.path.join("Fetched_Images", filename)
            counter += 1
        
        # Save image for future sharing
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # Success feedback
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()