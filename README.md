# Full Stack Developer Test

Welcome to the AgVend Digital Solutions full stack developer test. Follow the instructions below to set up your development environment using GitHub Codespaces.

## Setup Instructions

# Instructions for Completing and Submitting the Full Stack Developer Test

## Completing the Test

1. **Create Your Repository from the Template:**
   - Go to the [template repository](https://github.com/zolfran/AgVend-Developer-Test).
   - Click on the green `Use this template` button.
   - Select `Create a new repository`.
   - Name your new repository and make it public or private as required.

2. **Open the Repository in GitHub Codespaces:**
   - Navigate to your newly created repository on GitHub.
   - Click the `Code` button.
   - Select `Open with Codespaces` from the dropdown menu.
   - If you do not see `Codespaces` as an option, click `New codespace` and select the appropriate branch (usually `main`).

3. **Work on the Tasks:**
   - The Codespace will automatically set up the environment based on the configuration files provided in the repository.
   - Complete the tasks outlined in the README.md.

4. **Commit Your Changes:**
   - As you complete each task, commit your changes to your repository.
   - Use meaningful commit messages to describe your changes.
<<<<<<< HEAD
=======
   - ** If you have trouble submitting commits, check your remote origin 
   - *** Run `git remote -v` to see the end branch URL (this should be blank)
   - *** Add your branch URL by running `git remote add origin https://github.com/<your-username>/<your-repository>.git`
   - *** Run `git push -u origin main`
   - *** Run `git fetch origin`
   - *** Run `git rebase origin/main`
>>>>>>> 9de3170455b831f7b1970eb85e8d5d42ffe568f6

5. **Push Your Changes:**
   - Push your commits to your GitHub repository.
     ```sh
     git add .
     git commit -m "Completed task XYZ"
     git push origin main
     ```

## Submitting Your Work

1. **Share the Repository Link:**
   - Once you have completed the tasks and pushed all your changes, share the link to your repository with us.
   - You can send the link via email or through any other communication method provided.

2. **Review:**
   - Our team will review your repository, including your commits, code changes, and any additional documentation you have provided.

Thank you for completing the test. We look forward to reviewing your work!

## Tasks

### Backend Development
- Implement the following API endpoints:
  - `POST /add-book` - Add a new book.
  - `GET /books/<isbn>` - Retrieve book details.
  - `PUT /books/<isbn>` - Update stock quantity.
  - `DELETE /books/<isbn>` - Delete a book.

### Frontend Development
- Create a user interface to interact with the above API endpoints.
  - Use Django templates or React.
  - Ensure the interface is user-friendly and responsive.

### Database Management
- Write SQL queries to:
  - Retrieve books by a specific author.
  - Find the top 5 most expensive books.
  - Update the price of a book by its ISBN.
  - Delete all books with zero stock.
- Explain how you would optimize the database for performance.

### Code Review and Debugging
- Review and fix the provided code snippet in `core/views.py`.
- Explain the issues and your fixes in a separate document.

## Environment Details

- **Python Version:** 3.9
- **Django Version:** 5.0.4
- **Database:** SQLite (for simplicity, replace with PostgreSQL if needed)

Feel free to reach out if you have any questions or encounter any issues.
