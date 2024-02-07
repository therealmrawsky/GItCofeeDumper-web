
# GitDumper-web

GitDumper is a Flask application that allows you to download the contents of a Git repository as a password-protected zip file via transfer.sh. It's a simple tool for securely sharing Git repository contents.
Features

   -	Download the contents of a Git repository.
   -	Password protect the downloaded contents.
   -	Upload the zip file to transfer.sh for easy sharing.
   -	Simple API endpoint for processing Git URLs.

## Usage

To use GitDumper, simply provide the URL of the Git repository you want to download. The application will handle the rest, providing you with a password to access the zip file and a download link.
API Endpoint

You can also use the provided API endpoint to programmatically process Git URLs:

`curl -X GET "http://localhost:5000/process_git_url?url=<git_url>"`
Replace <git_url> with the URL of the Git repository you want to process.
Setup

   Clone this repository to your local machine.
   Install the required dependencies using.
    `pip install -r requirements.txt`
   Run the Flask application using.
   `python main.py`
   Access the application at http://localhost:5000.

## Dependencies

    Flask
    Flask-CORS
    Requests
## Web User Interface

GitCoffeeDumper comes with a simple and intuitive web user interface (UI) for conveniently dumping .git files online. The UI allows users to easily process Git repository URLs and download the contents as a password-protected zip file.

### Features

-   Input field for providing the URL of the Git repository.
-   Clickable button to initiate the download process.
-   Live feedback on processing status.
-   Direct download link for the zip file.
-   Copy-to-clipboard functionality for the generated password.

### How to Use

1.  Open the provided HTML file (`index.html`) in a web browser.
2.  Enter the URL of the Git repository you want to download in the input field.
3.  Click the "Download" button to start the download process.
4.  Wait for the processing message to indicate completion.
5.  Once processed, you can directly download the zip file using the provided download link, don't forget to copy the password to archive.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](https://github.com/therealmrawsky/GitDumper-web?tab=GPL-3.0-1-ov-file#readme) file for details.

Feel free to customize this README to include more detailed information about your project, installation instructions, usage examples, and any other relevant details
